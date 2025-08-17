import requests
import shutil
from datetime import datetime
from pathlib import Path

# ====== إعداداتك ======
TOKEN = "1234567890"  # غيّرها لتطابق التوكن في السيرفر
URL = f"https://mohammadpythonanywher1.pythonanywhere.com/api/v1/backup-db/?token={TOKEN}"
SAVE_DIR = Path(r"C:\Users\mohammad\database_backups")  # المسار الذي تريد حفظ النسخ فيه
BASE_NAME = "db.sqlite3"  # اسم القاعدة على السيرفر
# ======================

# التأكد أن مجلد الحفظ موجود
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# إنشاء اسم ملف بتاريخ ووقت التحميل
now_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{BASE_NAME.replace('.sqlite3', '')}_{now_str}.sqlite3"
file_path = SAVE_DIR / filename

print(f"⏳ جاري تنزيل قاعدة البيانات وحفظها باسم: {file_path.name} ...")

# تنفيذ الطلب وتنزيل الملف
response = requests.get(URL, stream=True)
if response.status_code == 200:
    with open(file_path, "wb") as f:
        shutil.copyfileobj(response.raw, f)
    print(f"✅ تم التنزيل بنجاح وحفظ النسخة في: {file_path}")
else:
    print(f"❌ فشل التحميل - كود الاستجابة: {response.status_code}")
    print(response.text)
