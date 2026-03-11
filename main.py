import os
import importlib
from glob import glob
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# جلب المتغيرات من هيروكو
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

def load_plugins():
    # البحث عن كل ملفات بايثون في مجلد الأوامر
    path = "plugins/*.py"
    files = glob(path)
    for name in files:
        module_spec = importlib.util.spec_from_file_location("name", name)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        print(f"✅ تم تحميل الإضافة: {name}")

print("⏳ جاري بدء تشغيل السورس...")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث"))
async def restart(event):
    await event.edit("🔄 جاري إعادة تشغيل السورس وتحميل الأوامر...")
    load_plugins()

if __name__ == "__main__":
    load_plugins()
    client.start()
    client.run_until_disconnected()
