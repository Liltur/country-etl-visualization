import requests
import json

# API URL
url = "https://restcountries.com/v3.1/all"

# Fetch data from the API
response = requests.get(url)
if response.status_code == 200:
    countries_data = response.json()
    
    import pandas as pd
    # Parse data and select required attributes
    data = []
    for country in countries_data:
        data.append({
            "name": country.get("name", {}).get("common", ""),
            "capital": country.get("capital", [""])[0] if country.get("capital") else "",
            "region": country.get("region", ""),
            "subregion": country.get("subregion", ""),
            "population": country.get("population", 0),
            "area": country.get("area", 0),
            "languages": ", ".join(country.get("languages", {}).values()) if country.get("languages") else "",
            "timezones": ", ".join(country.get("timezones", [])) if country.get("timezones") else ""
        })

    countries_df = pd.DataFrame(data)
    print(countries_df.head())

    # Saving
    countries_df.to_csv("./data/raw_data/countries.csv", index=False, encoding="utf-8", errors="ignore")
    print(f"Saving secceed.")

else:
    print("Failed to connect to the API")

# file_path = f"./data/raw_data/raw_data.json"
# with open(file_path,'w') as file:
#     json.dump(countries_data, file_path, indent=4)
    
# print(f"Saved raw data successfully in ./data/raw_data/raw_data.json")
    
