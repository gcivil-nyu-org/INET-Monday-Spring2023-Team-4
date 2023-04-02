# -*- coding: utf-8 -*-

import pandas as pd
import json

dataURL = "datasets/Food_Scrap_Drop-Off_Locations_in_NYC.csv"
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
            # add row data if the field is not empty else keep it as empty string
            "hosted": row["Hosted_By"] if row["Hosted_By"] else "",
            "hours": row["Day_Hours"] if row["Day_Hours"] else "",
            "notes": row["Notes"] if row["Notes"] else "",
            "website": row["Website"] if row["Website"] else "",
            "bin": row["BIN"] if row["BIN"] else "",
            "lat": float(row["Latitude"]) if row["Latitude"] else 0.0,
            "lon": float(row["Longitude"]) if row["Longitude"] else 0.0,
        },
    }
    fixtures.append(fixture)

# Write the list of fixtures to a JSON file
with open("../fixtures/dashboard.json", "w") as f:
    json.dump(fixtures, f, indent=2)
