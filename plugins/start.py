from telethon import events

@events.register(events.NewMessage(outgoing=True, pattern=r"^\.فحص"))
async def ping(event):
    await event.edit("**🚀 سورس تيليثون يعمل بنجاح!**\n**💎 نظام الملفات المقسمة: نشط**")
