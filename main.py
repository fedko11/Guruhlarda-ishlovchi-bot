import asyncio
import logging
import sys
from os import getenv
import time
from aiogram import Bot, Dispatcher, html,F,types,Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,and_f
from aiogram.types import Message
from config import BOT_TOKEN as TOKEN




dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    
    
@dp.message(F.text == "salom", F.chat.type == 'supergroup')
async def get_group(message:Message):
    await message.reply("Salom Firdavs men guruhda QO'RIQCHI🥷 botman")


@dp.message(F.text == "Guruh turi haqida malumot ber", F.chat.type == 'supergroup')
async def get_group(message:Message):
    await message.answer(f"🖋Guruh nomi: {message.chat.title}\n⌨️Guruh turi: {message.chat.type}\n🆔Guruh ID: {message.chat.id}\n🆔Your ID: @{message.from_user.username}")


@dp.message(and_f(F.chat.type == 'supergroup' , F.new_chat_members))
async def get_new_chat(message: Message):
    for new_chat in message.new_chat_members:
        await message.answer(f"Assalomu alaykum Guruhga xush kelibsiz @{new_chat.username}")
        await message.delete()


@dp.message(and_f(F.chat.type == 'supergroup' , F.left_chat_member))
async def get_left_chat(message: Message):
    await message.answer(f"Xayr @{message.left_chat_member.username} bekor chiqdiz lekin😃️️️️️️")
    
    
@dp.message(F.chat.type == 'supergroup', and_f(F.text == "Yozishni chekla" , F.reply_to_message))
async def get_banned_chat(message: Message):
    user_id = message.reply_to_message.from_user.id
    permissions = types.ChatPermissions(can_send_message = False)
    await message.chat.restrict(user_id , permissions)
    await message.answer(f"@{message.reply_to_message.from_user.username}da yozish vaqtinchalik cheklab qo'yildi🛑")
    time.sleep(60)
    permissions = types.ChatPermissions(can_send_message = True)
    await message.chat.restrict(user_id , permissions)
    await message.answer(f"Adminga gap qaytarmang xurmatli @{message.reply_to_message.from_user.username}!\nQaytganingizdan xursandmiz😜️️️️️️!")


@dp.message(F.chat.type == 'supergroup', and_f(F.text == "Yozishni och" , F.reply_to_message))
async def get_banned_chat(message: Message):
    user_id = message.reply_to_message.from_user.id
    permissions = types.ChatPermissions(can_send_message = True)
    await message.chat.restrict(user_id , permissions)
    await message.answer(f"Adminga gap qaytarmang xurmatli @{message.reply_to_message.from_user.username}!\nQaytganingizdan xursandmiz😜️️️️️️!")
    

@dp.message(F.chat.type == 'supergroup',and_f(F.text == "ban ber",F.reply_to_message))
async def get_ban_chat(message:types.Message):
    user_id= message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"Siz guruhdan haydaldingiz xurmatli🛑 @{message.reply_to_message.from_user.username}")
    
    
@dp.message(F.chat.type == 'supergroup',and_f(F.text == "bandan chiqar",F.reply_to_message))
async def get_ban_chat(message:types.Message):
    user_id= message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"Siz guruhga yana qo'shildingiz xurmatli😃️️️️️️ @{message.reply_to_message.from_user.username}")
    





@dp.message()
async def echo_handler(message: Message) -> None:
        await message.send_copy(chat_id=message.chat.id)



async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())