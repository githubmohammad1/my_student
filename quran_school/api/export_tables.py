import sqlite3
import pandas as pd
from pathlib import Path

# اختر اسم القاعدة
db_file = Path("db.sqlite3")  # أو db_remote.sqlite3

if not db_file.exists():
    raise FileNotFoundError(f"لم أجد الملف: {db_file}")

# الاتصال بقاعدة البيانات
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# جلب جميع أسماء الجداول
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]

print(f"الجداول الموجودة في {db_file.name}: {tables}")

# تصدير كل جدول إلى CSV وExcel
for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    csv_name = f"{table}.csv"
    xlsx_name = f"{table}.xlsx"
    df.to_csv(csv_name, index=False, encoding="utf-8-sig")
    # df.to_excel(xlsx_name, index=False)
    print(f"✅ تم حفظ {table} → {csv_name} ")

conn.close()
