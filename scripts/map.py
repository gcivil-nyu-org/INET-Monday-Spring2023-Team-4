import pandas as pd
import json

dataURL1 = "./datasets/nyc_sites.csv"
#dataURL1 = "~/Users/agnespark/Desktop/INET-Monday-Spring2023-Team-4/scripts/datasets/nyc_sites.csv"
data1 = pd.read_csv(dataURL1)

dataURL2 = "./datasets/nyc_hosts.csv"
#dataURL2 = "~/Users/agnespark/Desktop/INET-Monday-Spring2023-Team-4/scripts/datasets/nyc_hosts.csv"
data2 = pd.read_csv(dataURL2)

dataURL3 = "./datasets/nyc_site_hosts.csv"
#dataURL3 = "~/Users/agnespark/Desktop/INET-Monday-Spring2023-Team-4/scripts/datasets/nyc_site_hosts.csv"
data3 = pd.read_csv(dataURL3)


# Convert the dataframe to a list of dictionaries, with each dictionary representing a row
rows1 = data1.to_dict("records")
rows2 = data2.to_dict("records")
rows3 = data3.to_dict("records")

# Convert each dictionary to a fixture object and add it to a list of fixtures
# The enumerate() function adds a counter to an iterable and returns it
nyc_sites = []
for i, row in enumerate(rows1):
    site = {
        "model": "dropoff_locator.Site",
        "pk": row["OID"],
        "fields": {
            "borough": row["Borough"],
            "name": row["SiteName"],
            "address": row["SiteAddr"],
            "schedule": row["Open_Month"],
            "season_start": row["Season_Start"] if row["Open_Month"] == "Seasonal" else "n/a", 
            "season_end": row["Season_End"] if row["Open_Month"] == "Seasonal" else "n/a", 
            "lat": float(row["Latitude"]) if row["Latitude"] else 0.0,
            "lon": float(row["Longitude"]) if row["Longitude"] else 0.0,
            "type": row["Type"],
            "notes": row["Notes"],
        },
    }
    nyc_sites.append(site)

nyc_hosts = []
for i, row in enumerate(rows2):
    host = {
        "model": "dropoff_locator.NYCHost",
        "pk": i + 1,
        "fields": {
            "name": row["Name"],
            "url": row["URL"],
        },
    }
    nyc_hosts.append(host)

nyc_site_hosts = []
for i, row in enumerate(rows3):
    site_host = {
        "model": "dropoff_locator.NYCSiteHost",
        "pk": i + 1,
        "fields": {
            "site": row["OID"],
            "host": row["Hosted_By"],
        },
    }
    nyc_site_hosts.append(site_host)

# Write the list of fixtures to JSON files
with open("../fixtures/nyc_sites.json", "w") as f1:
    json.dump(nyc_sites, f1, indent=2)

with open("../fixtures/nyc_hosts.json", "w") as f2:
    json.dump(nyc_hosts, f2, indent=2)

with open("../fixtures/nyc_site_hosts.json", "w") as f3:
    json.dump(nyc_site_hosts, f3, indent=2)
