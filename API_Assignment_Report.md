# REST API & JSON — Data Extraction

**Endpoint:** `GET https://jsonplaceholder.typicode.com/users` (public test API; no authentication required).

**Observed response:** JSON array with 10 demo user objects, containing nested `address` and `company` objects. The `api_response_sample.json` included here is a **selected-field transcription** of the public response inspected on 21 October 2026, **not** the unmodified complete response. The included `api_data.csv` is flattened from those selected fields.

**Reproducibility:** Run `python -m pip install -r requirements.txt` then `python API_Data_Extraction/api_extraction.py` from the repository root. This performs a fresh live GET request, saves the **full** JSON to `api_response_full.json`, and overwrites `api_data.csv` with the extracted rows.

**Columns:** id, name, username, city, company_name. Nested JSON fields are flattened into columns for analysis.

**Inspection:** 10 users; 10 distinct IDs; the demo dataset is synthetic, not real customer data.

**Concepts:** GET retrieves data; POST submits data; query parameters filter or shape responses where supported; `raise_for_status()` catches HTTP errors; timeouts prevent indefinite waits; API keys should be stored securely when needed.

**Documentation:** https://github.com/typicode/jsonplaceholder/blob/master/public/guide.html
