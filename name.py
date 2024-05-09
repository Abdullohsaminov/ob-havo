from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from weather import obhavo
api = '6400569785:AAEkblkrlYyhhuD5KE53AcL7AK1dYUvAFuY'
bot = Bot(api)
dp = Dispatcher(bot)

kurslarbutoon = InlineKeyboardMarkup()
kurslarbutoon.add(
    InlineKeyboardButton(text='Istanbul', callback_data='kurs_istanbul'),
    InlineKeyboardButton(text='Tashkent', callback_data='kurs_tashkent'),
    InlineKeyboardButton(text='Ankara', callback_data='kurs_ankara'),
    InlineKeyboardButton(text='Dubai', callback_data='kurs_dubai'),
    InlineKeyboardButton(text="Qoqon", callback_data="kurs_qoqon"),
    InlineKeyboardButton(text="Fargona", callback_data="kurs_fargona"),
    InlineKeyboardButton(text="Andijon", callback_data="kurs_andijon"),
    InlineKeyboardButton(text="Washington", callback_data="kurs_washington"),
    InlineKeyboardButton(text="Moskva", callback_data="kurs_moskva"),
    InlineKeyboardButton(text="London", callback_data="kurs_london"),

)
@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    name=message.from_user.full_name
    await bot.send_message(chat_id=chatid,text=f"Assalomu aleykum {name} Ob-havo malumotlarni bilish uchun quyidagi shaharlardan birini tanlang👇👇👇👇", reply_markup=kurslarbutoon)

@dp.callback_query_handler(lambda call: 'kurs' in call.data)
async def kurslar(callback: CallbackQuery):
    chatid = callback.message.chat.id
    text = callback.data.split('_')[1]
    royxat = {'istanbul': 'istanbul',
              'tashkent': 'tashkent',
              'ankara': 'ankara',
              'dubai': 'dubai',
              "qoqon": "qoqon",
              "fargona": "fargona",
              "andijon": "andijon",
              "washington": "washington",
              "moskva": "moskva",
              "london": "london",}
    for kurs, qiymat in royxat.items():
        if kurs == text:
            test=obhavo(qiymat)
            await bot.send_message(chat_id=chatid, text=test,reply_markup=kurslarbutoon)
async def notify_start(dp: Dispatcher):
    await bot.send_message(chat_id=6878861160, text='Bot ishga tushdi')
executor.start_polling(dp, skip_updates=True, on_startup=notify_start)
