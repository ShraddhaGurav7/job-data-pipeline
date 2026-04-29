# 🚀 Job Market Data Pipeline
Built an ETL pipeline using API data ingestion and SQL to analyze job market trends
---

## 📌 Overview
This project builds a modular ETL pipeline that ingests job postings from an API, processes unstructured data, and stores it in a structured format for analysis.

---

## 🎯 Problem Statement
Job seekers often lack visibility into:
- In-demand skills  
- Hiring trends  
- Job distribution across locations  

This project converts raw job postings into structured insights.

---

## 🧱 Architecture

Adzuna API → ETL (Python) → MySQL → CSV → Analysis

---

## ⚙️ Tech Stack

- Python (pandas, requests)
- MySQL
- REST API (Adzuna)

---

## 🔄 Pipeline Workflow

### Extract
- Fetch job postings from API  
- Handle pagination for batch ingestion  

### Transform
- Clean missing data  
- Process unstructured job descriptions  
- Extract key skills (Python, SQL, Excel, Power BI, AWS)  

### Load
- Store data in MySQL  
- Export cleaned dataset as CSV  

---

## 📊 Key Features

- End-to-end ETL pipeline  
- API-based data ingestion  
- Skill extraction from text data  
- Modular design (etl.py, db.py, main.py)  

---

## 📁 Project Structure

job-data-pipeline/
│── main.py  
│── etl.py  
│── db.py  
│── data/  
│   └── final_jobs_with_skills.csv  

---

## ▶️ How to Run

1. Install dependencies:
pip install pandas requests mysql-connector-python  

2. Add API credentials in etl.py  

3. Setup MySQL database  

4. Run:
python main.py  

---

## 🚀 Future Improvements

- Add Power BI dashboard for visualization  
- Implement duplicate handling in database  
- Automate pipeline execution  

---

## 🧠 Learnings

- Built modular ETL pipeline  
- Worked with API-based data ingestion  
- Performed data cleaning and transformation  
- Integrated Python with MySQL  

---

## 👩‍💻 Author

Shraddha Gurav  
GitHub: https://github.com/ShraddhaGurav7  
LinkedIn: https://www.linkedin.com/in/shraddhagurav  
