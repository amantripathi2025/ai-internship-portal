import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime

MONGO_URL = "mongodb+srv://amantripathi7550_db_user:D9L1RpYChCvpBpGj@ai-internship-portal.ftfkc7h.mongodb.net/?appName=ai-internship-portal"
client = MongoClient(MONGO_URL, tlsAllowInvalidCertificates=True)
db = client["internship-portal"]
collection = db["internships"]

# Saari categories
URLS = [
    "https://internshala.com/internships/",
    "https://internshala.com/internships/computer-science-engineering-internship",
    "https://internshala.com/internships/python-internship",
    "https://internshala.com/internships/web-development-internship",
    "https://internshala.com/internships/java-internship",
    "https://internshala.com/internships/marketing-internship",
    "https://internshala.com/internships/finance-internship",
    "https://internshala.com/internships/graphic-design-internship",
    "https://internshala.com/internships/content-writing-internship",
    "https://internshala.com/internships/mechanical-engineering-internship",
    "https://internshala.com/internships/civil-engineering-internship",
    "https://internshala.com/internships/data-science-internship",
    "https://internshala.com/internships/machine-learning-internship",
    "https://internshala.com/internships/android-development-internship",
    "https://internshala.com/internships/business-development-internship",
]

def scrape_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="individual_internship")
    
    saved = 0
    for card in cards:
        try:
            title_tag = card.find("h3")
            title = title_tag.text.strip() if title_tag else "N/A"

            company_tag = card.find("p", class_="company-name")
            if not company_tag:
                company_tag = card.find("a", class_="link_display_like_text")
            company = company_tag.text.strip() if company_tag else "N/A"

            location_tag = card.find("p", class_="location-names")
            if not location_tag:
                location_tag = card.find("a", class_="location_link")
            location = location_tag.text.strip() if location_tag else "Remote"

            stipend_tag = card.find("span", class_="stipend")
            stipend = stipend_tag.text.strip() if stipend_tag else "Unpaid"

            apply_tag = card.find("a", class_="view_detail_button")
            apply_link = "https://internshala.com" + apply_tag["href"] if apply_tag else "N/A"

            internship = {
                "title": title,
                "company": company,
                "location": location,
                "stipend": stipend,
                "applyLink": apply_link,
                "source": "Internshala",
                "scrapedAt": datetime.now(),
                "requiredSkills": [],
                "duration": "N/A",
                "description": f"{title} at {company}"
            }

            exists = collection.find_one({
                "title": title,
                "company": company
            })

            if not exists:
                collection.insert_one(internship)
                saved += 1
                print(f"✅ {title} | {company}")
            else:
                print(f"⏭ Skip: {title}")

        except Exception as e:
            print(f"Error: {e}")
            continue
    
    return saved

# Saari URLs scrape karo
total = 0
for url in URLS:
    print(f"\n🔍 Scraping: {url}")
    saved = scrape_url(url)
    total += saved
    print(f"Saved: {saved}")

print(f"\n🎉 Total nayi internships saved: {total}")