import random
import requests
import os

# Configuration
BASE_URL = "https://brightlane.github.io/A1-Website-Buider-Pro/"
KIT_URL = "https://partners.kit.com/0sw1foot3nqi"

# Load your niches and locations from affiliate.json
locations = ["New York", "Toronto", "Chicago", "Vancouver", "Miami", "Seattle", "Dallas", "London"]
niches = ["Custom Merchandise", "Email Automation", "Business Solutions", "Growth Marketing"]

def generate_daily_post():
    loc = random.choice(locations)
    niche = random.choice(niches)
    
    # Create the URL for the specific page
    slug = f"{niche}-{loc}".lower().replace(" ", "-")
    page_url = f"{BASE_URL}pages/{slug}.html"
    
    post_text = f"🚀 Scaling {niche} in {loc} for 2026! \n\nCheck out our latest automation blueprint. Plus, see why we use Kit to own our audience: {KIT_URL} \n\nFull Guide: {page_url} #2026Business #Automation"
    
    return post_text

# If using Buffer API (Free for 3 channels)
def post_to_buffer(text):
    # You would need your Buffer Access Token in GitHub Secrets
    token = os.getenv("BUFFER_ACCESS_TOKEN")
    profile_ids = os.getenv("BUFFER_PROFILE_IDS").split(",")
    
    for p_id in profile_ids:
        payload = {
            "text": text,
            "profile_ids[]": p_id,
            "shorten": True
        }
        requests.post("https://api.bufferapp.com/1/updates/create.json", data=payload, headers={"Authorization": f"Bearer {token}"})

if __name__ == "__main__":
    content = generate_daily_post()
    print(f"Post Generated: {content}")
    # post_to_buffer(content)
