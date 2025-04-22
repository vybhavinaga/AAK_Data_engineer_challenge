
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import json

# Create FastAPI app
app = FastAPI(title="World Bank Country Data API")

# Loading country data from json file

with open("countries_data.json", "r") as f:
    countries=json.load(f)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage with links and search form
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>World Bank Country Data API</h2>
    <p>Welcome! Try these routes:</p>
    <ul>
        <li><a href="/countries">/countries</a> - List all countries</li>
        <li><a href="/docs">/docs</a> - Swagger UI</li>
        <li><a href="/chart">/chart</a> - Country Initials Chart</li>
    </ul>
    <hr>
    <h3> Search for a country</h3>
    <form action="/country" method="get">
        <input type="text" name="name" placeholder="e.g. India" required>
        <button type="submit">Search</button>
    </form>

    <h3>Partial Match search</h3>
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="e.g. ind" required>
        <button type="submit">Search</button>
    </form>
    """

    
# Get all countries
@app.get("/countries",response_class=HTMLResponse)
def get_all_countries():
    html = """<h2>List of all Countries</h2><ul>"""
    for country in countries:
        html += f"""
        <li>
            <strong>{country['name']}</strong> -
            <a href='/country/{country['name']}'>View Details</a> |
            <a href='{country['url']}' target='_blank'>World Bank page</a>
        </li>
        """
    html +="""</ul><br><a href='/'>Back to Home</a>"""
    return html

# Redirect search form to country specific page
@app.get("/country")
def redirect_from_query(name:str):
    return RedirectResponse(url=f"/country/{name}")

# Get a specific country data by name
@app.get("/country/{name}", response_class=HTMLResponse)
def get_country(name: str):
    for country in countries:
        if country["name"].lower() == name.lower():
            return f"""
            <h2>Country Details</h2>
            <ul>
                <li><strong>Name:</strong>{country["name"]}</li>
                <li><strong>URL:</strong><a href="{country["url"]}" target="_blank">{country["url"]}</a></li>
            </ul>
            <a href="/">Back to home</a>
            """
    raise HTTPException(status_code=404, detail="Country not Found")


# Search countries by partial name
@app.get("/search", response_class=HTMLResponse)
def search_countries(query:str):
    results=[ c for c in countries if query.lower() in c["name"].lower()]
    if not results:
        return f"<h3>No results found for '{query}'</h3><a href='/'>Back to home</a>"
    # Create a HTML kist with links to /country/{name}
    html = f"<h3>Search results for '{query}':</h3><ul>"
    for c in results:
        html += f"<li><a href='/country/{c['name']}'>{c['name']}</a></li>"
    html +="<ul><a href='/'>Back to home</a>"
    

    return html

# Serve the chart image
@app.get("/chart")
def show_chart():
    return FileResponse("static/chart.png", media_type="image/png")
