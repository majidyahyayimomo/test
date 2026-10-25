import os
import sys

print("=== Starting Setup for Sanaei Panel ===")

base_dir = os.getcwd()
x_ui_dir = os.path.join(base_dir, "x-ui")

# ۱. دانلود آخرین نسخه x-ui در صورت عدم وجود
if not os.path.exists(x_ui_dir):
    print("Downloading x-ui binary...")
    os.system("curl -sL https://github.com/mhsanaei/3x-ui/releases/latest/download/x-ui-linux-amd64.tar.gz -o x-ui.tar.gz")
    os.system("tar -zxvf x-ui.tar.gz")
    os.system("rm -f x-ui.tar.gz")

# ۲. اعطای دسترسی‌های لازم
os.system(f"chmod +x {x_ui_dir}/x-ui {x_ui_dir}/bin/xray-linux-* 2>/dev/null")

# ۳. ساخت پوشه‌های محلی برای دیتابیس و لاگ‌ها جهت جلوگیری از خطای Read-only
db_dir = os.path.join(base_dir, "db")
log_dir = os.path.join(base_dir, "logs")
os.makedirs(db_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

# تنظیم متغیرهای محیطی برای هدایت مسیر دیتابیس و لاگ 3x-ui به داخل پوشه پروژه
os.environ["XUI_DATABASE_PATH"] = db_dir
os.environ["XUI_LOG_PATH"] = log_dir

# ۴. تغییر مسیر به پوشه x-ui و اجرای پنل
print("=== Launching 3x-ui Core ===")
if os.path.exists(x_ui_dir):
    os.chdir(x_ui_dir)
    os.execv("./x-ui", ["./x-ui"])
else:
    print(f"Error: Directory {x_ui_dir} not found!")
    sys.exit(1)