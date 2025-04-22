import requests
from bs4 import BeautifulSoup
import json


def scrape_countries():
    url = "https://data.worldbank.org/country"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    countries = []
    base = "https://data.worldbank.org"

    # loop through all country links on the page
    for link in soup.select("a[href^='/country/']"):
        name = link.get_text(strip=True)
        href = link['href']
        full_url = base + href
        
        if name and href:
            # Store country name and its world bank url.
            countries.append({
                "name":name,
                "url":full_url,
            })

            
    # Save data to JSON file        
    with open("countries_data.json", "w") as f:
        json.dump(countries, f, indent=2)
    print(f"Scrapped {len(countries)} countries.")

if __name__ == "__main__":
    scrape_countries()
                
