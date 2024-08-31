from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from knopkalar import asosiyknopka
storage = MemoryStorage()

bottoken = '6994564433:AAGYtbb-2YwAwntxggzC_I_uXqE3WJKWHBA'
bot = Bot(bottoken)
dp = Dispatcher(bot, storage=storage)


class RegistratsiyState(StatesGroup):
    ism = State()
    familya = State()
    manzil = State()
    yosh = State()
    telefon = State()

@dp.message_handler(commands='start')
async def start(message: Message):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Xush kelibsiz", reply_markup=asosiyknopka())


@dp.message_handler(text="Royxatdan o'tish")
async def getism(message: Message):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Ismingizni kiriting.")
    await RegistratsiyState.ism.set()


@dp.message_handler(state=RegistratsiyState.ism)
async def ismolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Ism qabul qilindi. Familiya kiriting.")
    text = message.text
    await state.update_data(
        {'ism': text}
    )
    await RegistratsiyState.familya.set()


@dp.message_handler(state=RegistratsiyState.familya)
async def familiyaolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Familya qabul qilindi. Manzil kiriting")
    text = message.text
    await state.update_data(
        {'familiya': text}
    )
    await RegistratsiyState.manzil.set()


@dp.message_handler(state=RegistratsiyState.manzil)
async def manzilolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Manzil qabul qilindi. Yoshingizni kiriting")
    text = message.text
    await state.update_data(
        {'manzil': text}
    )
    await RegistratsiyState.yosh.set()

@dp.message_handler(state=RegistratsiyState.yosh)
async def yosholish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Yosh qabul qilindi. Telefon raqam kiriting")
    text = message.text
    await state.update_data(
        {"yosh": text}
    )
    await RegistratsiyState.telefon.set()

@dp.message_handler(state=RegistratsiyState.telefon)
async def telefonolish(message: Message, state: FSMContext):
    userid = message.from_user.id
    await bot.send_message(chat_id=userid, text="Telefon raqam qabul qilindi. Siz bilan yaqin orada bog'lanamiz")
    data = await state.get_data()
    text = f"Ismi: {data['ism']}. Familiyasi: {data['familiya']}. Manzili: {data['manzil']}. Yoshi: {data['yosh']}. Telefon nomeri: {message.text}"
    await bot.send_message(chat_id=6829390664, text=text)
    await state.finish()

executor.start_polling(dp, skip_updates=True)