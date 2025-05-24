Error while getting Updates: Conflict: terminated by other

بله! در تصویری که در ساعت **02:44** فرستادی (تصویر با پیام "There is no active deployment for this service")، Railway پیام زیر رو نوشته:

> **There is no active deployment for this service.**  
> **Deploy the repo alireza1465/Gold-signal-telegram-bot**

این یعنی آخرین نسخه‌ای که Deploy کرده بودی، توسط خودت **پاک شده (Deleted)** و الان هیچ سرویس فعالی وجود نداره.

در بخش پایین هم مشخصه که وضعیت همه نسخه‌ها اینه:

- `Update main.py` → **REMOVED**
- یعنی خودت اون نسخه‌ها رو پاک کردی (Deleted).

---

### راه‌حل سریع

برای اینکه دوباره رباتت اجرا بشه:

1. وارد این لینک شو:  
   [https://railway.app/project](https://railway.app/project)

2. روی پروژه `ravishing-enthusiasm` کلیک کن.

3. در تب `Deployments`، روی دکمه **"Deploy the repo alireza1465/Gold-signal-telegram-bot"** بزن.

4. صبر کن تا Deployment کامل بشه و حالت `ACTIVE` سبز ظاهر بشه.

5. اگر هنوز سیگنال نمی‌فرسته، به من بگو تا فایل `main.py` یا تنظیمات دیگر رو بررسی کنیم.

اگر خواستی خودم یک نسخه سالم از `main.py` برات بفرستم همین الان.
