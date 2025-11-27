from fastapi import FastAPI
from threading import Thread
import uvicorn
import asyncio
import bot

app = FastAPI()

@app.get("/")
def home():
    return {"status": "EAU Confession Bot Running"}

def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8080)

def start_telegram_bot():
    asyncio.run(bot.start_bot())

Thread(target=start_fastapi).start()
Thread(target=start_telegram_bot).start()
