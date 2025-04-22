import json
import matplotlib.pyplot as plt
from collections import Counter
import os

def generate_chart():
    # Load the country data from JSON file

    with open("countries_data.json", "r") as f:
        countries = json.load(f)

    # Count number of countries by first letter

    initials = [c["name"][0].upper() for c in countries if c["name"]]
    counts = Counter(initials)

    # Create a bar chart

    plt.figure(figsize=(10,6))
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("First letter of Country name")
    plt.ylabel("Number of Countries")
    plt.title("Number of Countries by First letter")
    plt.tight_layout()

    # Save chart image to static folder

    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()

    print(" Chart saved to static/chart.png")

if __name__ == "__main__":
    generate_chart()


