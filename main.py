import os
import sys
import subprocess
from telethon import events

# أمر التحديث
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_bot(event):
    await event.edit("⏳ **جاري فحص التحديثات من جيت هاب...**")
    
    try:
        # جلب التحديثات من المستودع المرتبط
        pull = subprocess.check_output(["git", "pull"]).decode("utf-8")
        
        if "Already up to date." in pull:
            return await event.edit("✅ **السورس محدث بالفعل إلى آخر إصدار.**")
        
        await event.edit(f"✅ **تم جلب التحديثات بنجاح!**\n\n`{pull}`\n\n🔄 **جاري إعادة تشغيل السورس...**")
        
        # إعادة تشغيل العملية (سيقوم هيروكو بإعادة التشغيل تلقائياً عند انتهاء العملية)
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    except Exception as e:
        await event.edit(f"❌ **حدث خطأ أثناء التحديث:**\n`{str(e)}`")
        
