# World Bank Country Data API - Challenge Submission

## Overview
This project scrapes a list of countries from the World Bank website and exposes the data through a FASTAPI web API. It supports listing countries, viewing country details, performing partial searches, and visualising country initials in a bar chart. A clean, browser-friendly interface is included along with interactive Swagger docs.

---

## How to run the Application

### 1. Clone or download this repository to the local machine.

### 2. Install Dependencies
'''
pip install -r requirements.txt
'''

### 3. Scrape Country Data
'''
python scraper.py
'''

### 4. Generate Chart
'''
python chart_generator.py
'''

### 5. Start the API Server
'''
Unicorn main:app --reload
'''

Then open the link that is generated in the browser. Usually, it should be something like [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

| Endpoint                    |         Description                                 |
|-----------------------------|-----------------------------------------------------|                                                                               
| '/'                         | Homepage with exact and partial search forms        |
| '/countries'                | List of all countries with links                    |
| '/country/{name}'           | Exact country details page                          |
| '/search?query=...'         | Partial name search                                 |
| '/chart'                    | Bar chart of countries by first letter              |
| '/docs'                     | Swagger UI for testing and docs                     |

---

## Technologies used

- FASTAPI
- Unicorn
- Requests
- BeautifulSoup
- Matplotlib
- PyCountry

---

I used the requests library to fetch HTML content of the World Bank country listing page , and BeautifulSoup to parse and extract data. The scraped data is transformed into a list of dictionaries and saved locally to countries_data.json file. The fastapi app reads this file when serving API requests. This makes data persistent across sessions and allows quick reloading  without re-scraping.

Additionally, each country is dynamically enriched using the official World Bank API for indicators like GDP growth, population, life expectency, and internet usage (if a matching ISO country code is available). These values are shown in the API response and UI.

---

## ETL Approach

- **Extract**: Scraped country names and URL's from the World Bank country listing.
- **Transform**: Parsed the HTML and enriched the data using the World Bank Indicators API.
- **Load**: Saved it to 'countries_data.json' and used it in the API.

## Bonus Features

- Partial name search with clickable links
- Bar chart visualisation of countries by first letter
- Dynamic enrichment of countries using World Bank API
- User-friendly HTML formatting for all pages

---

## Key Note

The instruction said to scrape "any data you see relevant to each country". After inspecting the World Bank website, the only consistent static data available in the HTML was name and its link to the world bank data page. Other fields like income level and all were not available in the raw HTML and are loaded via JavaScript.

To meet this requirement, I used official World Bank API to fetch real-time indicators for countries with valid ISO codes. This provided country-level statistics.

---

## Result

A lightweight, well-structured API demonstrating scraping, ETL processing, search functionality, visualisation, and clean presentation - built entirely from scratch using real data.



 