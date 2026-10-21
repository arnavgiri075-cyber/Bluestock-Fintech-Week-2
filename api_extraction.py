"""Retrieve public demo user data and export nested JSON to CSV."""
import json
from pathlib import Path
import requests
import pandas as pd

BASE = Path(__file__).resolve().parent
URL = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(URL, timeout=20)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("Expected a JSON list")
    (BASE / "api_response_full.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    records = [{"id": u.get("id"), "name": u.get("name"),
                "username": u.get("username"),
                "city": u.get("address", {}).get("city"),
                "company_name": u.get("company", {}).get("name")} for u in payload]
    df = pd.DataFrame(records)
    df.to_csv(BASE / "api_data.csv", index=False)
    print(f"HTTP {response.status_code}; saved {len(df)} rows to api_data.csv")
    print(df.head())
except (requests.RequestException, ValueError, KeyError) as exc:
    print(f"API extraction failed: {exc}")
    raise
