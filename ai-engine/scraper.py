import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime

# MongoDB connect karo
MONGO_URL = "mongodb+srv://amantripathi7550_db_user:D9L1RpYChCvpBpGj@ai-internship-portal.ftfkc7h.mongodb.net/?appName=ai-internship-portal"
client = MongoClient(MONGO_URL)
db = client["internship-portal"]
collection = db["internships"]

def scrape_and_save():
    url = "https://internshala.com/internships/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    print("Internshala se data la raha hoon...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Saare internship cards dhundo
    cards = soup.find_all("div", class_="individual_internship")
    print(f"Mili internships: {len(cards)}")

    saved = 0
    for card in cards:
        try:
            # Title nikalo
            title_tag = card.find("h3")
            title = title_tag.text.strip() if title_tag else "N/A"

            # Company nikalo
            company_tag = card.find("p", class_="company-name")
            if not company_tag:
                company_tag = card.find("a", class_="link_display_like_text")
            company = company_tag.text.strip() if company_tag else "N/A"

            # Location nikalo
            location_tag = card.find("p", class_="location-names")
            if not location_tag:
                location_tag = card.find("a", class_="location_link")
            location = location_tag.text.strip() if location_tag else "Remote"

            # Stipend nikalo
            stipend_tag = card.find("span", class_="stipend")
            stipend = stipend_tag.text.strip() if stipend_tag else "Unpaid"

            # Apply link nikalo
            apply_tag = card.find("a", class_="view_detail_button")
            apply_link = "https://internshala.com" + apply_tag["href"] if apply_tag else "N/A"

            # MongoDB mein save karo
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

            # Duplicate check — same title + company already hai toh skip karo
            exists = collection.find_one({
                "title": title,
                "company": company
            })

            if not exists:
                collection.insert_one(internship)
                saved += 1
                print(f"✅ Saved: {title} | {company} | {location} | {stipend}")
            else:
                print(f"⏭ Already exists: {title}")

        except Exception as e:
            print(f"Error: {e}")
            continue

    print(f"\n🎉 Kaam khatam! {saved} nai internships MongoDB mein save hui!")

# Run karo
scrape_and_save()