import requests
from bs4 import BeautifulSoup

def scrape_internships():
    url = "https://internshala.com/internships/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Saare internship cards dhundo
    cards = soup.find_all("div", class_="individual_internship")
    print(f"Mili internships: {len(cards)}")
    
    for card in cards[:5]:
        try:
            # Title
            title = card.find("h3", class_="job-internship-name")
            # Company
            company = card.find("h4", class_="company-name")
            # Location  
            location = card.find("div", id=lambda x: x and "location_names" in x)
            
            print("---")
            print(f"Title: {title.text.strip() if title else 'N/A'}")
            print(f"Company: {company.text.strip() if company else 'N/A'}")
            print(f"Location: {location.text.strip() if location else 'N/A'}")
        except Exception as e:
            print(f"Error: {e}")

scrape_internships()