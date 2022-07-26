from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, ChatPermissions
import os
import time
import datetime
from komutlar.donate import *

PM = 938113608

CH = -1001462385390

@Client.on_message(
    filters.private
    & filters.command("cvb")
    )
async def cvb(client, message):
    id = int(message.command[1])
    text = " ".join(message.command[2:])
    try:
        await client.send_message(chat_id=id, text=f"{message.from_user.mention} dan reklam hakkında bir mesajın var.\nMesaj;\n{text}\n\nYanıt vermek için: /ilet mesaj")
        await message.reply_text("Mesajın başarıyla iletildi.")
    except:
        await message.reply_text("Sanırım bir sorunla karşılaştım olası durumlar;\n\n-Kullanıcı botu engellemiş olabilir.\n-İlk önce id yi yazmamış veya yanlış id girilmiş olabilir.\n-FloodWait")
        
        
@Client.on_message(
    filters.private
    & filters.command("ilet")
    )
async def il(client, message):
    text = " ".join(message.command[1:])
    try:
        await client.send_message(chat_id=PM, text=f"{message.from_user.mention} dan bir yanıt var.\nMesaj: {text}\n\nKullanıcı id: {message.chat.id}")
        await message.reply_text("Mesajınız başarıyla iletildi.")
    except:
        await message.reply_text("Sanırım bir sorun çıktı lütfen tekrar veya daha sonra deneyin.")
