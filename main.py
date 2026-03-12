import asyncio
from telegram import Bot

# --- التكوين (أبو صالح) ---
TOKEN = '8727974026:AAF62vrpNtmoNLiTAw_Q_HRuaS55Bof-gvY'
CHAT_ID = -1002625499772 
MESSAGE = "اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبِيِّنَا مُحَمَّدٍ ﷺ ✨"

async def send_periodic():
    bot = Bot(token=TOKEN)
    # رسالة تظهر في سجلات الموقع (Logs) لتعرف أن البوت بدأ
    print("🚀 البوت بدأ العمل بنجاح..")
    
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
            print("✅ تم إرسال الذكر إلى المجموعة.")
        except Exception as e:
            print(f"❌ حدث خطأ: {e}")
        
        # الانتظار لمدة ساعتين (7200 ثانية)
        await asyncio.sleep(7200)

if __name__ == "__main__":
    asyncio.run(send_periodic())
