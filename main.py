from etl import extract_data, transform_data
from db import insert_data
import os

def main():
    print(" Starting Job Data Pipeline...\n")

    # =========================
    # 🔹 Extract Data
    # =========================
    raw_jobs = extract_data()

    if not raw_jobs:
        print("No data extracted. Exiting...")
        return

    # =========================
    # 🔹 Transform Data
    # =========================
    df = transform_data(raw_jobs)

    if df.empty:
        print(" DataFrame is empty after transformation. Exiting...")
        return

    # =========================
    # 🔹 Create data folder (if not exists)
    # =========================
    if not os.path.exists("data"):
        os.makedirs("data")

    # =========================
    # 🔹 Save CSV
    # =========================
    file_path = "data/final_jobs_with_skills.csv"
    df.to_csv(file_path, index=False)

    print(f" CSV saved at: {file_path}")

    # =========================
    # 🔹 Load into MySQL
    # =========================
    insert_data(df)

    print("\nPipeline completed successfully!")


# =========================
# 🔹 Entry Point
# =========================
if __name__ == "__main__":
    main()