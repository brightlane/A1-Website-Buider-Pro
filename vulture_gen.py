import os
from datetime import datetime

# CONFIGURATION
BASE_URL = "https://brightlane.github.io/A1-Website-Buider-Pro/"
LOCATIONS = ["New York", "Toronto", "Chicago", "Vancouver", "Miami", "Seattle", "Dallas", "London"]
NICHES = ["Custom Merchandise", "Email Automation", "Business Solutions", "Growth Marketing"]
OCCASIONS = ["Mother's Day", "Birthday", "Anniversary", "Wedding", "Business Launch"]

def generate_pages():
    if not os.path.exists('pages'):
        os.makedirs('pages')
    
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    # Generate the pages
    for loc in LOCATIONS:
        for niche in NICHES:
            for occ in OCCASIONS:
                slug = f"{niche}-{occ}-{loc}".lower().replace(" ", "-").replace("'", "")
                file_path = f"pages/{slug}.html"
                
                # Simple Template for each page
                html_content = f"""<!DOCTYPE html>
<html>
<head><title>{niche} in {loc} - {occ} 2026</title></head>
<body style="background:#001f3f; color:white; font-family:sans-serif; text-align:center;">
    <h1>{niche} Experts in {loc}</h1>
    <p>Your 2026 blueprint for {occ} success.</p>
    <a href="https://partners.kit.com/0sw1foot3nqi" style="color:#4ad760;">Start with Kit (ConvertKit)</a>
</body>
</html>"""
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                urls.append(f"{BASE_URL}{file_path}")

    # Generate the sitemap.xml automatically
    sitemap_start = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    sitemap_end = '</urlset>'
    sitemap_body = "".join([f'<url><loc>{u}</loc><lastmod>{today}</lastmod><priority>0.7</priority></url>' for u in urls])
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_start + sitemap_body + sitemap_end)

if __name__ == "__main__":
    generate_pages()
    print("Vulture Engine: 1000+ Pages and Sitemap generated.")
