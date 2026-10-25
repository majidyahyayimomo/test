# app.py — OMID v14.0 · نقطه‌ی ورود (Launcher) برای KataBump و هاست‌های مشابه
# چون relay_vless.py و xhttp_siz10.py از main ایمپورت می‌کنند، اجرای مستقیم
# «python main.py» باعث ImportError حلقه‌ای می‌شود. این فایل main را به‌عنوان
# ماژول واقعی «main» لود می‌کند تا حلقه‌ی ایمپورت سالم بماند.

import os

from main import app   # ← main اینجا به‌عنوان ماژول لود می‌شود (نه __main__)

if __name__ == "__main__":
    import uvicorn
    # PORT را می‌خواند؛ اگر نبود پورت تخصیصی پنل (SERVER_PORT)؛ در نهایت 10251
    port = int(os.environ.get("PORT") or os.environ.get("SERVER_PORT") or 10251)
    print(f"omid launcher → starting on 0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
    
