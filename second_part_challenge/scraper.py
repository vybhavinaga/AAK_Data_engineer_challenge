import requests
from bs4 import BeautifulSoup
import json
import pycountry
import time

# Indicators to fetch
INDICATORS = {
    "Population": "SP.POP.TOTL",
    "GDP Growth (%)": "NY.GDP.MKTP.KD.ZG",
    "Life Expectancy": "SP.DYN.LE00.IN",
    "Internet Usage (%)": "IT.NET.USER.ZS"
}

# Get ISO alpha-3 country code
def get_country_code(name):
    try:
        cleaned_name = name.replace(", The", "").strip()
        return pycountry.countries.lookup(cleaned_name).alpha_3
    except:
        return None

# Fetch indicator data
def fetch_indicators(code):
    result = {}
    for label, indicator in INDICATORS.items():
        url = f"http://api.worldbank.org/v2/country/{code}/indicator/{indicator}?format=json&per_page=100"
        res = requests.get(url)
        data = res.json()

        if isinstance(data, list) and len(data) > 1 and data[1]:
            for entry in data[1]:
                if entry["value"] is not None:
                    result[label] = {
                        "value": entry["value"],
                        "year": entry["date"]
                    }
                    break
        else:
            result[label] = None
    return result

# Scrape countries and enrich where possible
def scrape_countries():
    url = "https://data.worldbank.org/country"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    countries = []

    for link in soup.select("a[href^='/country/']"):
        name = link.get_text(strip=True)
        href = link.get("href")
        full_url = "https://data.worldbank.org" + href

        code = get_country_code(name)

        country_data = {
            "name": name,
            "url": full_url,
            "code": code
        }

        if code:
            indicators = fetch_indicators(code)
            country_data.update(indicators)

        countries.append(country_data)
        time.sleep(0.5)

    return countries

# Save result
if __name__ == "__main__":
    all_data = scrape_countries()
    with open("countries_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)
    print(f"\nSaved {len(all_data)} total countries to countries_data.json")
