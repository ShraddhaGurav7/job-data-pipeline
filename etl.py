import requests
import pandas as pd

# 🔑 API Credentials
APP_ID = "a2a8cfcd"
APP_KEY = "f7250bbbff52e91d4563cf645c4f59e4"


# =========================
# 🔹 Extract Data (API)
# =========================
def extract_data():
    all_jobs = []

    for page in range(1, 4):  # Fetch 3 pages (~150 jobs)
        url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"

        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 50,
            "what": "data engineer"
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"❌ Error on page {page}: {response.status_code}")
            continue

        data = response.json()
        all_jobs.extend(data.get('results', []))

    print(f"✅ Total jobs fetched: {len(all_jobs)}")

    return all_jobs


# =========================
# 🔹 Transform Data
# =========================
def transform_data(raw_jobs):
    jobs = []

    for job in raw_jobs:
        jobs.append({
            "title": job.get('title'),
            "company": job.get('company', {}).get('display_name'),
            "location": job.get('location', {}).get('display_name'),
            "salary": job.get('salary_max', 0),
            "description": job.get('description')
        })

    df = pd.DataFrame(jobs)

    if df.empty:
        print("⚠️ No data to process")
        return df

    # =========================
    # 🔹 Data Cleaning
    # =========================
    df.dropna(inplace=True)
    df['salary'] = df['salary'].fillna(0)

    # =========================
    # 🔹 Skill Extraction
    # =========================
    skills = ["python", "sql", "excel", "power bi", "aws"]

    df['description'] = df['description'].str.lower()

    for skill in skills:
        df[skill] = df['description'].str.contains(skill, na=False)

    print("✅ Data transformed successfully")

    return df