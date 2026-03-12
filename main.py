<!-- end list -->
import asyncio
import os
from telegram import Bot
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- التكوين المحدث (أبو صالح) ---
TOKEN = '8727974026:AAF62vrpNtmoNLiTAw_Q_HRuaS55Bof-gvY'
CHAT_ID = -1002625499772 
MESSAGE = "اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبِيِّنَا مُحَمَّدٍ ﷺ ✨"

# سيرفر وهمي لإبقاء البوت حياً على Render
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

async def send_periodic():
    bot = Bot(token=TOKEN)
    print("🚀 أحمد يحييك.. البوت بدأ العمل بالرمز الجديد.")
    
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
            print("✅ تم إرسال الذكر إلى المجموعة.")
        except Exception as e:
            print(f"❌ خطأ في الإرسال: {e}")
        
        # الانتظار لمدة ساعتين (7200 ثانية)
        await asyncio.sleep(7200)

if __name__ == "__main__":
    # تشغيل سيرفر الويب في الخلفية
    threading.Thread(target=run_health_server, daemon=True).start()
    # تشغيل البوت الأساسي
    asyncio.run(send_periodic())
