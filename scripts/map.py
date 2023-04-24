import pandas as pd
import json

sites_path = "scripts/datasets/nyc_sites.csv"
schedules_path = "scripts/datasets/nyc_day_hours.csv"
hosts_path = "scripts/datasets/nyc_hosts.csv"
site_hosts_path = "scripts/datasets/nyc_site_hosts.csv"

sites_data = pd.read_csv(sites_path)
schedules_data = pd.read_csv(schedules_path)
hosts_data = pd.read_csv(hosts_path)
site_hosts_data = pd.read_csv(site_hosts_path)

# Convert the dataframe to a list of dictionaries, with each dictionary representing a row
sites_rows = sites_data.to_dict("records")
schedules_rows = schedules_data.to_dict("records")
hosts_rows = hosts_data.to_dict("records")
site_hosts_rows = site_hosts_data.to_dict("records")

# Convert each dictionary to a fixture object and add it to a list of fixtures
# The enumerate() function adds a counter to an iterable and returns it
sites = []
seasons = []
for i, row in enumerate(sites_rows):
    site = {
        "model": "dropoff_locator.Site",
        "pk": row["OID"],
        "fields": {
            "name": row["SiteName"],
            "address": row["SiteAddr"],
            "borough": row["Borough"],
            "type": 'NYC Smart Bin' if (row["Type"] == 'Smart Bin') else 'NYC Community Site',
            "season": row["Open_Month"],
            "is_always_open": True if (row["Day_Hours"] == '24/7') else False,
            "lat": float(row["Latitude"]) if row["Latitude"] else 0.0,
            "lon": float(row["Longitude"]) if row["Longitude"] else 0.0,
            "notes": row["Notes"] if row["Notes"] != "0" else "",
        },
    }
    sites.append(site)

    if (site["fields"]["season"] == 'Seasonal'):
      season = {
        "model": "dropoff_locator.SiteSeason",
        "pk": row["OID"],
        "fields": {
            "start": row["Season_Start"],
            "end": row["Season_End"],
        }
      }
      seasons.append(season)

schedules = []
for i, row in enumerate(schedules_rows):
    schedule = {
        "model": "dropoff_locator.SiteSchedule",
        "fields": {
            "site": row["OID"],
            "mon": None if row["Mon"] == "0" else row["Mon"],
            "tues": None if row["Tues"] == "0" else row["Tues"],
            "wed": None if row["Wed"] == "0" else row["Wed"],
            "thurs": None if row["Thurs"] == "0" else row["Thurs"],
            "fri": None if row["Fri"] == "0" else row["Fri"],
            "sat": None if row["Sat"] == "0" else row["Sat"],
            "sun": None if row["Sun"] == "0" else row["Sun"],
        },
    }
    schedules.append(schedule)

# hosts = []
# for i, row in enumerate(hosts_rows):
# u = User. 

site_hosts = []
for i, row in enumerate(site_hosts_rows):
    site_host = {
        "model": "users.SiteHost",
        "pk": i + 1,
        "fields": {
            "site": row["OID"],
            "host": row["Host"],
        },
    }
    site_hosts.append(site_host)

# Write the list of fixtures to JSON files
with open("/Users/agnespark/INET-Monday-Spring2023-Team-4/fixtures/nyc_sites.json", "w") as f1:
    json.dump(sites, f1, indent=2)

with open("/Users/agnespark/INET-Monday-Spring2023-Team-4/fixtures/nyc_seasons.json", "w") as f2:
    json.dump(seasons, f2, indent=2)

with open("../fixtures/nyc_schedules.json", "w") as f3:
    json.dump(schedules, f3, indent=2)

with open("../fixtures/nyc_hosts.json", "w") as f2:
    json.dump(nyc_hosts, f2, indent=2)

with open("/Users/agnespark/INET-Monday-Spring2023-Team-4/fixtures/nyc_site_hosts.json", "w") as f3:
    json.dump(site_hosts, f3, indent=2)
