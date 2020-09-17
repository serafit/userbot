from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

app = Client("my_account")

#echoes 

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Поиск в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 успешно взломанo!")
    sleep(3)
 
    msg.edit("Поиск данных ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Поиск данных ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Найдены данные!")

@app.on_message(filters.command("KillerQueen", prefixes=".") & filters.me)
def KillerQueen(_, msg):

    chat = msg.text.split(".KillerQueen ", maxsplit=1)[1]
 
    members = [
    	x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Sheer-heart-attack!... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=int(chat),
                user_id=str(members[i].user.id),
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Был взорван " + members[i].user.first_name)
        except FloodWait as e:
            print("> ждите", e.x, "секунд.")
            time.sleep(e.x)
 
    app.send_message(chat, "Сюда смотри!")

@app.on_message(filters.command("Sheer-heart-attack", prefixes=".") & filters.me)
def sheer(_, msg):
	

app.run()

