#!/usr/bin/env python3
"""
WordPress-optimized Publications Generator for EXO-RESTART
Creates responsive, full-width HTML suitable for WordPress embedding
"""

import requests
import json
from datetime import datetime
import argparse
import os

# Configuration
ADS_API_TOKEN = "rarbwpPjLNBCv2aT1L1IM2Y8oTeaaw3LulPsKUd0"
BASE_URL = "https://api.adsabs.harvard.edu/v1/search/query"

# Team members
AUTHORS = [
    "Trifonov, Trifon", "Trifonov, T.", 
    "Bozhilov, Vladimir", "Bozhilov, V.",
    "Zaharieva, Evelina", "Zaharieva, E.",
    "Stoeva, Denitza", "Stoeva, D.",
    "Minev, Milen", "Minev,M.",
    "Antonova, Desislava", "Antonova, D.",
    "Stefanov, Stefan", "Stefanov, S.",
]

ACKNOWLEDGMENTS = ["VIHREN-2021"]
COMBINE_AUTHORS = True


def fetch_papers(author_name, ack=None):
    """Fetches papers for a given author from NASA ADS."""
    headers = {"Authorization": f"Bearer {ADS_API_TOKEN}"}
    
    query = f'author:"{author_name}" collection:astronomy'
    if ack:
        ack_query = " OR ".join([f'ack:"{keyword}"' for keyword in ack] + 
                                [f'full:"{keyword}"' for keyword in ack])
        query = f'({query}) AND ({ack_query})'
    
    params = {
        "q": query,
        "fl": "title,author,year,doi,citation_count,bibcode,property",
        "rows": 1000,
        "sort": "year desc"
    }
    
    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json().get("response", {}).get("docs", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers for {author_name}: {e}")
        return []


def generate_wordpress_html(papers_by_author, combine_authors):
    """Generates WordPress-optimized HTML content."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # WordPress-friendly HTML (no <html> or <head> tags needed for embedding)
    html_content = f"""
<!-- EXO-RESTART Publications - Generated {timestamp} -->
<style>
.exo-publications {{
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, sans-serif;
}}

.exo-publications h2 {{
    color: #1e3a8a;
    font-size: 1.8em;
    margin-top: 2em;
    margin-bottom: 1em;
    border-bottom: 3px solid #3b82f6;
    padding-bottom: 0.5em;
}}

.exo-publications .update-time {{
    text-align: right;
    color: #666;
    font-size: 0.9em;
    font-style: italic;
    margin-bottom: 2em;
}}

.exo-publications .stats-summary {{
    background: #f0f9ff;
    border-left: 4px solid #3b82f6;
    padding: 1em 1.5em;
    margin-bottom: 2em;
    border-radius: 4px;
}}

.exo-publications .stats-summary p {{
    margin: 0.5em 0;
    font-size: 1.05em;
}}

.exo-publications ol {{
    padding-left: 2em;
    counter-reset: publication-counter;
    list-style: none;
}}

.exo-publications ol li {{
    counter-increment: publication-counter;
    margin: 2em 0;
    padding: 1.5em;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    position: relative;
    line-height: 1.7;
    font-size: 1.05em;
    transition: box-shadow 0.3s ease;
}}

.exo-publications ol li:hover {{
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}}

.exo-publications ol li::before {{
    content: counter(publication-counter) ".";
    position: absolute;
    left: -2em;
    font-weight: bold;
    color: #3b82f6;
    font-size: 1.1em;
}}

.exo-publications .citation {{
    font-style: italic;
    font-weight: 600;
    color: #1e293b;
    font-size: 1.1em;
    display: block;
    margin-bottom: 0.5em;
}}

.exo-publications .authors {{
    color: #475569;
    margin-bottom: 0.5em;
}}

.exo-publications .authors b {{
    color: #1e40af;
    font-weight: 600;
}}

.exo-publications .publication-meta {{
    margin-top: 0.8em;
    padding-top: 0.8em;
    border-top: 1px solid #e5e7eb;
    font-size: 0.95em;
}}

.exo-publications a {{
    color: #2563eb;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}}

.exo-publications a:hover {{
    color: #1d4ed8;
    text-decoration: underline;
}}

.exo-publications .stats {{
    color: #059669;
    font-weight: 500;
}}

.exo-publications .year {{
    color: #6b7280;
    font-weight: 600;
}}

/* Responsive design */
@media screen and (max-width: 768px) {{
    .exo-publications h2 {{
        font-size: 1.4em;
    }}
    
    .exo-publications ol li {{
        padding: 1em;
        margin: 1.5em 0;
        font-size: 0.95em;
    }}
    
    .exo-publications .citation {{
        font-size: 1em;
    }}
}}
</style>

<div class="exo-publications">
    <div class="update-time">Last updated: {timestamp}</div>
"""

    seen_bibcodes = set()

    if combine_authors:
        all_papers = []
        for papers in papers_by_author.values():
            all_papers.extend(papers)

        unique_papers = {paper['bibcode']: paper for paper in all_papers 
                        if paper['bibcode'] not in seen_bibcodes}
        seen_bibcodes.update(unique_papers.keys())
        
        refereed_papers = [p for p in unique_papers.values() 
                          if p.get("property") and "REFEREED" in p["property"]]
        
        # Sort by year (descending) and citation count
        refereed_papers.sort(key=lambda x: (x.get("year", ""), x.get("citation_count", 0)), reverse=True)
        
        total_citations = sum(p.get("citation_count", 0) for p in refereed_papers)
        
        html_content += f"""
    <div class="stats-summary">
        <p><strong>Total Refereed Publications:</strong> {len(refereed_papers)}</p>
        <p><strong>Total Citations:</strong> {total_citations}</p>
    </div>
    
    <h2>Refereed Publications</h2>
    <ol>
"""
        
        for paper in refereed_papers:
            html_content += format_paper_wordpress(paper, AUTHORS)
        
        html_content += "</ol>"
    else:
        for author, papers in papers_by_author.items():
            refereed = [p for p in papers 
                       if p.get("property") and "REFEREED" in p["property"]]
            
            html_content += f"<h2>Papers by {author} ({len(refereed)})</h2><ol>"
            
            for paper in refereed:
                html_content += format_paper_wordpress(paper, [author])
            
            html_content += "</ol>"

    html_content += "\n</div>\n<!-- End EXO-RESTART Publications -->"
    return html_content


def format_paper_wordpress(paper, highlight_authors):
    """Formats a single paper entry for WordPress."""
    title = paper.get("title", ["No title"])[0]
    authors_list = paper.get("author", ["Unknown author"])
    year = paper.get("year", "No year")
    doi = paper.get("doi", [""])[0]
    bibcode = paper.get("bibcode", "")
    ads_url = f"https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract"
    citations = paper.get("citation_count", 0)

    formatted_authors = []
    additional_authors = []

    for i, a in enumerate(authors_list[:20]):
        parts = a.split(", ")
        if len(parts) == 2:
            last_name, first_name = parts
            formatted_name = f"{last_name}, {first_name[0]}."
        else:
            formatted_name = a
        
        if any(author in a for author in highlight_authors):
            formatted_authors.append(f"<b>{formatted_name}</b>")
        else:
            formatted_authors.append(formatted_name)
    
    for a in authors_list[20:]:
        if any(author in a for author in highlight_authors):
            parts = a.split(", ")
            if len(parts) == 2:
                last_name, first_name = parts
                formatted_name = f"incl. <b>{last_name}, {first_name[0]}.</b>"
            else:
                formatted_name = f"incl. <b>{a}</b>"
            additional_authors.append(formatted_name)

    if len(authors_list) > 20:
        formatted_authors.append("et al.")
    
    formatted_authors.extend(additional_authors)
    authors_str = ", ".join(formatted_authors)

    return f"""
        <li>
            <span class="citation">{title}</span>
            <div class="authors">{authors_str}</div>
            <div class="publication-meta">
                <span class="year">{year}</span> | 
                <a href="https://doi.org/{doi}" target="_blank" rel="noopener">DOI</a> | 
                <a href="{ads_url}" target="_blank" rel="noopener">ADS</a> | 
                <span class="stats">Citations: {citations}</span>
            </div>
        </li>
"""


def main():
    parser = argparse.ArgumentParser(description='Generate WordPress-optimized publications list')
    parser.add_argument('-o', '--output', default='exorestart_publications_wordpress.html',
                       help='Output HTML file path')
    parser.add_argument('--no-ack', action='store_true',
                       help='Disable acknowledgment filtering')
    args = parser.parse_args()

    print("Fetching publications from NASA ADS...")
    papers_by_author = {}
    
    ack_filter = None if args.no_ack else ACKNOWLEDGMENTS
    
    for author in AUTHORS:
        print(f"  - Fetching papers for {author}")
        papers = fetch_papers(author, ack=ack_filter)
        sorted_papers = sorted(papers, key=lambda x: x.get("year", ""), reverse=True)
        papers_by_author[author] = sorted_papers
    
    print("Generating WordPress-optimized HTML...")
    html_content = generate_wordpress_html(papers_by_author, COMBINE_AUTHORS)
    
    output_path = args.output
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"✓ HTML page generated: {output_path}")
    print(f"✓ File size: {os.path.getsize(output_path)} bytes")
    print("\nTo use in WordPress:")
    print("1. Copy the contents of this file")
    print("2. In WordPress, add a 'Custom HTML' block")
    print("3. Paste the content")
    print("4. Publish!")


if __name__ == "__main__":
    main()
