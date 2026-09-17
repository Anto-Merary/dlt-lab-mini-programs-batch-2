"""Load a tourism CSV file and recommend destinations by budget and interests.

Optional CSV columns: destination, country, category, days, cost, rating.
The built-in records are used when tourism.csv is not available.
"""

import csv
from pathlib import Path

SAMPLE_DESTINATIONS = [
    {"destination": "Ooty", "country": "India", "category": "Nature", "days": "3", "cost": "9000", "rating": "4.6"},
    {"destination": "Goa", "country": "India", "category": "Beach", "days": "4", "cost": "15000", "rating": "4.5"},
    {"destination": "Jaipur", "country": "India", "category": "Heritage", "days": "3", "cost": "12000", "rating": "4.7"},
    {"destination": "Munnar", "country": "India", "category": "Nature", "days": "3", "cost": "10000", "rating": "4.8"},
]


def load_destinations(filename: str = "tourism.csv") -> list[dict[str, str]]:
    path = Path(filename)
    if not path.exists():
        return SAMPLE_DESTINATIONS
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main() -> None:
    destinations = load_destinations()
    print("Tourism Dataset Recommendation System")
    print("Available categories:", ", ".join(sorted({row["category"] for row in destinations})))
    category = input("Preferred category: ").strip().lower()
    budget = float(input("Maximum budget in INR: "))
    days = int(input("Maximum trip days: "))

    matches = [
        row for row in destinations
        if category in row["category"].lower() and float(row["cost"]) <= budget and int(row["days"]) <= days
    ]
    matches.sort(key=lambda row: float(row["rating"]), reverse=True)
    if not matches:
        print("No destination matches those preferences.")
        return
    print("\nRecommended destinations:")
    for row in matches:
        print(f"- {row['destination']}, {row['country']} | {row['category']} | {row['days']} days | INR {row['cost']} | {row['rating']}/5")


if __name__ == "__main__":
    main()
