# EXO-RESTART Publications Automation

This package helps you automatically fetch and display NASA ADS publications for the EXO-RESTART team on your WordPress website.

## Quick Answer to Your Question

**Can you integrate it directly into WordPress?**
- **Not directly** - WordPress doesn't natively run Python scripts
- **But** - You have several good automation options!

**Best approach depends on your hosting:**
- **VPS/Dedicated Server**: Use cron job (automatic daily updates)
- **Shared Hosting**: Use external service or manual updates
- **Local Computer**: Use the quick update scripts provided

## 📦 What's Included

1. `update_publications.py` - Improved Python script with better error handling
2. `quick_update.sh` - One-click update for Linux/Mac
3. `quick_update.bat` - One-click update for Windows
4. `WORDPRESS_INTEGRATION_GUIDE.md` - Detailed integration instructions
5. This README

## 🚀 Quickest Way to Get Started

### If you have a server with SSH access:

```bash
# 1. Upload files to your server
scp update_publications.py user@yourserver.com:~/scripts/

# 2. Set up daily cron job
crontab -e

# 3. Add this line (runs daily at 2 AM):
0 2 * * * python3 ~/scripts/update_publications.py -o /var/www/html/wp-content/uploads/exorestart_ads_papers.html

# 4. In WordPress, add this to a page:
# <iframe src="/wp-content/uploads/exorestart_ads_papers.html" width="100%" height="800px"></iframe>
```

### If you're on shared hosting or want manual control:

**Windows:**
1. Double-click `quick_update.bat`
2. Upload the generated `exorestart_ads_papers.html` to WordPress Media Library
3. Embed it in a page using Custom HTML block

**Linux/Mac:**
1. Run `./quick_update.sh`
2. Upload the generated `exorestart_ads_papers.html` to WordPress Media Library
3. Embed it in a page using Custom HTML block

## 📋 Requirements

- Python 3.6+
- `requests` library: `pip install requests`
- NASA ADS API token (already in the script)

## 🔄 Update Frequency Options

### Option A: Automatic (Server Cron Job)
✅ Updates daily automatically
✅ No manual work needed
❌ Requires server access

### Option B: Manual (Run When Needed)
✅ Simple to understand
✅ Works on any hosting
❌ Need to remember to run it

### Option C: External Service (PythonAnywhere/AWS Lambda)
✅ Automatic updates
✅ Works with shared hosting
❌ Slightly more complex setup

## 🎯 Recommended Approaches

### For Daily Updates (Best for active research):
**Use cron job** - See `WORDPRESS_INTEGRATION_GUIDE.md` Option 2

### For Weekly/Monthly Updates:
**Use quick update scripts** - Run manually when publications change

### For Maximum Automation on Shared Hosting:
**Use PythonAnywhere** - See `WORDPRESS_INTEGRATION_GUIDE.md` Option 4

## 🔧 Customization

Edit `update_publications.py` to change:

```python
# Team members
AUTHORS = ["Trifonov, Trifon", ...]

# Project acknowledgments to filter
ACKNOWLEDGMENTS = ["VIHREN-2021"]

# Display settings
COMBINE_AUTHORS = True  # Show all papers together
SIDE_MARGIN = '200px'   # Page margins
```

## 📖 Embedding in WordPress

### Method 1: Iframe (Recommended)
```html
<iframe src="/wp-content/uploads/exorestart_ads_papers.html" 
        width="100%" 
        height="800px" 
        frameborder="0">
</iframe>
```

### Method 2: Direct HTML
1. Copy the contents of the `<div class="content">` section
2. Paste into WordPress Custom HTML block

### Method 3: Shortcode
Add to functions.php (see guide for full code):
```php
add_shortcode('exorestart_pubs', 'exorestart_publications_shortcode');
```
Then use `[exorestart_pubs]` in any page.

## 🔒 Security Note

⚠️ The NASA ADS API token is currently in the script. For better security:

1. Create a config file:
```json
{
    "token": "your_token_here"
}
```

2. Modify script to load from config:
```python
import json
with open('config.json') as f:
    config = json.load(f)
    ADS_API_TOKEN = config['token']
```

3. Keep config file outside web-accessible directories

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install requests
```

### "Permission denied" error
```bash
chmod +x quick_update.sh
```

### Cron job not running
```bash
# Check cron logs
grep CRON /var/log/syslog

# Test command manually
python3 /path/to/update_publications.py
```

### HTML not showing in WordPress
- Check file permissions: `chmod 644 exorestart_ads_papers.html`
- Verify path in iframe matches uploaded location
- Try "File Manager" in cPanel to verify upload

## 📊 How It Works

1. Script queries NASA ADS API for each team member
2. Filters for refereed publications
3. Deduplicates results
4. Formats as HTML with citations, DOIs, and ADS links
5. Saves to file
6. WordPress displays the file

## 🆘 Need Help?

1. Read `WORDPRESS_INTEGRATION_GUIDE.md` for detailed instructions
2. Check you have Python 3 installed: `python3 --version`
3. Test the script manually first: `python3 update_publications.py`
4. Check the generated HTML opens in a browser

## 📝 License

Free to use and modify for the EXO-RESTART project.

---

**Last Updated:** January 2026
**Maintained by:** EXO-RESTART Team
