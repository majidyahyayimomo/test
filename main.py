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

# ۳. اجرای مستقیم باینری با بررسی راهنما یا پارامترهای اجرایی
print("=== Launching 3x-ui Core ===")
if os.path.exists(x_ui_dir):
    os.chdir(x_ui_dir)
    
    # تست اینکه آیا x-ui پارامتری برای مسیر دارد یا خیر، اگر نه با دستور مستقیم
    # در نسخه های جدید 3x-ui معمولا فایل کانفیگ یا سوییچ وجود دارد
    os.execv("./x-ui", ["./x-ui"])
else:
    print(f"Error: Directory {x_ui_dir} not found!")
    sys.exit(1)
