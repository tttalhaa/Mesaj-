from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
	filters.command("start")
	& filters.private
	)
async def start(client: Client, message: Message):
	await message.reply_text(f"Merhaba {message.from_user.mention}, ben [Luci Oyun Bot](https://t.me/LuciOyun_Bot) 'unun reklam sipariş verme ve bilgi için hazırlanan bir botum!\n\nFiyat Bilgi: /bilgi\nKullanım: /req \nDetaylı kullanım videosu: /kullanim\n\n#DİKKAT#\n/req komutu duyuru kanalına katılmadan çalışmaz.",
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"kanal", url="https://t.me/LuciOrjinalBotlari"
						)
				],
				[
					InlineKeyboardButton(
						"➕ Luci Oyun Botu Bir Gruba Ekle ➕", url="https://t.me/LuciOyun_Bot?startgroup=true"
						)
				]
			]
		)
	)
