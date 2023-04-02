# -*- coding: utf-8 -*-

import pandas as pd
import json

dataURL = "https://github.com/gcivil-nyu-org/INET-Monday-Spring2023-Team-4/blob/develop/scripts/datasets/Food_Scrap_Drop-Off_Locations_in_NYC.csv"
data = pd.read_csv(dataURL, index_col=0)

# Convert the dataframe to a list of dictionaries, with each dictionary representing a row
rows = data.to_dict("records")

# Convert each dictionary to a fixture object and add it to a list of fixtures
fixtures = []
for i, row in enumerate(rows):
    fixture = {
        "model": "dashboard.dashboard",
        "pk": i + 1,
        "fields": {
            "borough": row["Borough"],
            "ntaname": row["NTAName"],
            "sitename": row["SiteName"],
            "siteaddr": row["SiteAddr"],
            "hosted": row["Hosted_By"],
            "hours": row["Day_Hours"],
            "notes": row["Notes"],
            "website": row["Website"],
            "bin": row["BIN"],
            "lat": float(row["Latitud"]),
            "lon": float(row["Longitude"]),
        },
    }
    fixtures.append(fixture)

# Write the list of fixtures to a JSON file
with open("../fixtures/dashboard.json", "w") as f:
    json.dump(fixtures, f, indent=2)
