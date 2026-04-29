import mysql.connector

def insert_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="job_data"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO jobs 
            (title, company, location, salary, python, sql_skill, excel, power_bi, aws)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['title'],
            row['company'],
            row['location'],
            row['salary'],
            int(row['python']),
            int(row['sql']),
            int(row['excel']),
            int(row['power bi']),
            int(row['aws'])
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Data inserted into MySQL")