
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import json
import os

# Create FastAPI app
app = FastAPI(title="World Bank Country Data API")

# Load enriched country data
with open("countries_data.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage with links and search form
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>World Bank Country Data API</h2>
    <p>Welcome! Try these routes:</p>
    <ul>
        <li><a href="/countries">/countries</a> – List all countries</li>
        <li><a href="/chart">/chart</a> – Bar chart of countries by first letter</li>
        <li><a href="/docs">/docs</a> – Swagger API Docs</li>
    </ul>
    <hr>
    <h3>Search for a country</h3>
    <form action="/country" method="get">
        <input type="text" name="name" placeholder="e.g., India" required>
        <button type="submit">Search</button>
    </form>
    <br>
    <h3>Partial search</h3>
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="e.g., In" required>
        <button type="submit">Search</button>
    </form>
    """
# Get all countries
@app.get("/countries", response_class=HTMLResponse)
def list_countries():
    html = "<h2>List of Countries</h2><ul>"
    for country in countries:
        html += f'<li><a href="/country/{country["name"]}">{country["name"]}</a></li>'
    html += """</ul><br><a href='/'>Back to Home</a>"""
    return html

# Redirect search form to country specific page
@app.get("/country")
def redirect_to_country(name: str):
    return RedirectResponse(url=f"/country/{name}")

# Get a specific country data by name
@app.get("/country/{name}", response_class=HTMLResponse)
def get_country(name: str):
    for country in countries:
        if country["name"].lower() == name.lower():
            html = f"<h2>{country['name']}</h2>"
            html += f"<p><strong>World Bank Page:</strong> <a href='{country['url']}' target='_blank'>{country['url']}</a></p>"
            html += f"<p><strong>ISO Code:</strong> {country.get('code', 'N/A')}</p>"

            # Display indicators
            for label in ["GDP Growth (%)", "Population", "Life Expectancy", "Internet Usage (%)"]:
                data = country.get(label)
                if isinstance(data, dict):
                    html += f"<p><strong>{label}:</strong> {data['value']} (Year: {data['year']})</p>"
                else:
                    html += f"<p><strong>{label}:</strong> N/A</p>"

            html += """</ul><br><a href='/'>Back to Home</a>"""
            return html

    raise HTTPException(status_code=404, detail="Country not found")


# Search countries by partial name
@app.get("/search", response_class=HTMLResponse)
def partial_search(query: str):
    matches = [c for c in countries if query.lower() in c["name"].lower()]
    if not matches:
        return f"<p>No countries found matching '{query}'</p>"

    html = f"<h2>Search results for '{query}':</h2><ul>"
    for country in matches:
        html += f'<li><a href="/country/{country["name"]}">{country["name"]}</a></li>'
    html += """</ul><br><a href='/'>Back to Home</a>"""
    return html


# Serve the chart image
@app.get("/chart", response_class=HTMLResponse)
def show_chart():
    if not os.path.exists("static/chart.png"):
        return "<p>Chart not found. Please run chart_generator.py to generate it.</p>"
    return """
    <h2>Countries by First Letter</h2>
    <img src="/static/chart.png" alt="Chart">
    """
