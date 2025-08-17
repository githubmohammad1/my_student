
import requests
import shutil
import sqlite3
import pandas as pd

URL = "https://mohammadpythonanywher1.pythonanywhere.com/api/v1/backup-db/?token=1234567890"

LOCAL_DB_PATH = "db.sqlite3"
conn = sqlite3.connect("db.sqlite")
def download_db() :
    print("⏳ جاري تنزيل قاعدة البيانات...")
    response = requests.get(URL, stream=True)

    if response.status_code == 200:
      
      with open("db_remote.sqlite3", "wb") as f:
        shutil.copyfileobj(response.raw, f)
      print("✅ تم تنزيل نسخة من قاعدة البيانات (db_remote.sqlite3)")

    # استبدال القاعدة المحلية
      shutil.copy("db_remote.sqlite3", LOCAL_DB_PATH)
      print("✅ تم استبدال القاعدة المحلية بالنسخة الجديدة")
    else:
      
      print("❌ فشل التحميل:", response.status_code, response.text)






# افتح قاعدة البيانات
def exctrack_db():
    

# اختر الجدول الذي تريد تصديره
    df = pd.read_sql_query("SELECT * FROM  student", conn)

# حفظ كـ CSV
    df.to_csv("النتيجة.csv", index=False, encoding="utf-8-sig")

# أو حفظ كـ Excel
    df.to_excel("النتيجة.xlsx", index=False)

    conn.close()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
