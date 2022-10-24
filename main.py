from aiogram import Bot, Dispatcher, executor, types
import keyboard as kb
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton
import aiogram.utils.markdown as fmt
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import sqlite3
from MessageAs import getMSG, setMSG
import settings as st
from datetime import datetime as dt

# --- Bot ---
TOKEN = st.TOKEN
admins = st.ADMINS

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class Mainling(StatesGroup):
    mail = State()
    accept = State()


class MainMsg(StatesGroup):
    mess = State()
    accept = State()


ToSeV = ""

# --- DataBase's ---
user_db = sqlite3.connect('user.db')

user_cur = user_db.cursor()

user_cur.execute('''CREATE TABLE IF NOT EXISTS users(
                name TEXT NOT NULL,
                user_id BIGINT,
                last_move DATETIME);
''')

user_db.commit()


def updateDB(user_id, cur, db):
    cur.execute("""UPDATE users SET last_move = ? WHERE user_id = ?""", (dt.now(), user_id))
    db.commit()


def isAdmin(user_id: str) -> bool:
    global admins
    if user_id in admins:
        return True
    return False


def isUserExists(_user_id: int, cur: sqlite3) -> bool:
    for user_id in cur.execute("SELECT user_id FROM users"):
        if user_id[0] == _user_id:
            return True
    return False


# -- Commands handlers --
@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    if isAdmin(msg.from_user.id):
        await msg.answer("Здравствуйте, {0.first_name}!".format(msg.from_user), reply_markup=kb.admin_kb)
    else:
        user_cur.execute('''SELECT user_id FROM users ''')
        if not isUserExists(msg.from_user.id, user_cur):
            user_cur.execute(f'''INSERT INTO users VALUES (?, ?, ?)''',
                             (str(msg.from_user.first_name), msg.from_user.id, dt.now()))
            print(dt.now().isoformat(sep='T'))
            user_db.commit()
        await msg.answer(
            "Добро пожаловать, {0.first_name}!\nЗдесь вы можете ознакомится с ассортиментом товара и ценами нашего "
            "магазина💥".format(msg.from_user), reply_markup=kb.main_kb)


@dp.message_handler(commands=["user"])
async def make_user_view(msg: types.Message):
    global admins
    if msg.from_user.id == 744090218 or msg.from_user.id == 810545519:
        if isAdmin(msg.from_user.id):
            admins.remove(msg.from_user.id)
            await msg.answer("-- Вид пользователя --", reply_markup=kb.main_kb)
        else:
            admins.append(msg.from_user.id)
            await msg.answer("-- Вид админа --", reply_markup=kb.admin_kb)


@dp.message_handler(commands=["cancel"], state="*")
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("-- Главное меню --", reply_markup=kb.admin_kb)


# -- Message handlers --
@dp.message_handler()
async def media(msg: types.Message):

    user_cur.execute('''SELECT user_id FROM users ''')
    if not isUserExists(msg.from_user.id, user_cur):
        user_cur.execute(f'''INSERT INTO users VALUES (?, ?, ?)''',
                         (str(msg.from_user.first_name), msg.from_user.id, dt.now()))
        print(dt.now().isoformat(sep='T'))
        user_db.commit()

    global ToSeV

    if msg.text == "📲 Соц. сети":
        await msg.answer("Найти вы нас можете тут:", reply_markup=kb.media_inline_kb)
    if msg.text == "🧑🏼‍💻 Менеджер":
        await msg.answer("Сделать заказ:", reply_markup=kb.manage_inline_kb)


    if msg.text == '🛒 Ассортимент':
        await msg.answer("Выберете", reply_markup=kb.smt_kb)
    if msg.text == "Ассортимент здесь 👇🏻":
        await msg.answer("Выберете", reply_markup=kb.choose_kb)
    if msg.text == "Гугл таблица 📝":
        await msg.answer("Гугл таблица \n https://docs.google.com/spreadsheets/d/1QPX7Qbq_Fp0cW6L3Sgql4ZZAkVEQjsRWH4YX9ImRT1M/edit#gid=0", reply_markup=kb.main_kb)

    if msg.text == "Жидкости 🧪":
        await msg.answer(getMSG("L"), parse_mode=types.ParseMode.HTML, reply_markup=kb.manage_inline_kb)
    if msg.text == "Под-Системы 💨":
        await msg.answer(getMSG("V"), parse_mode=types.ParseMode.HTML, reply_markup=kb.manage_inline_kb)
    if msg.text == "Расходники ⚙":
        await msg.answer(getMSG("C"), parse_mode=types.ParseMode.HTML, reply_markup=kb.manage_inline_kb)
    if msg.text == "Одноразовые электронные сигареты 😶‍🌫️":
        await msg.answer(getMSG("O"), parse_mode=types.ParseMode.HTML, reply_markup=kb.manage_inline_kb)

    if msg.text == 'Назад':
        await msg.answer('Главное меню', reply_markup=kb.main_kb)


    if msg.text == "Главное меню 🔙":
        if isAdmin(msg.from_user.id):
            await msg.answer("-- Главное меню -- ", reply_markup=kb.admin_kb)
        else:
            await msg.answer("-- Главное меню --", reply_markup=kb.main_kb)

    if msg.text == 'Создать рассылку':
        if isAdmin(msg.from_user.id):
            await Mainling.mail.set()
            await msg.answer("Введите текст рассылки:")

    if msg.text == "Задать новое главное сообщение":
        if isAdmin(msg.from_user.id):
            await msg.answer("Выберите тип задаваемого сообщения ->", reply_markup=kb.setMess_kb)

    if msg.text == 'Задать сообщение "Жидкости"':
        if isAdmin(msg.from_user.id):
            ToSeV = "L"
            await MainMsg.mess.set()
            await msg.answer("Введите новое сообщение, которое будет отображаться пользователям: ")

    if msg.text == 'Задать сообщение "Под-системы"':
        if isAdmin(msg.from_user.id):
            ToSeV = "V"
            await MainMsg.mess.set()
            await msg.answer("Введите новое сообщение, которое будет отображаться пользователям: ")

    if msg.text == 'Задать сообщение "Расходники"':
        if isAdmin(msg.from_user.id):
            ToSeV = "C"
            await MainMsg.mess.set()
            await msg.answer("Введите новое сообщение, которое будет отображаться пользователям: ")

    if msg.text == 'Задать сообщение "Одноразовые"':
        if isAdmin(msg.from_user.id):
            ToSeV = "O"
            await MainMsg.mess.set()
            await msg.answer("Введите новое сообщение, которое будет отображаться пользователям: ")


# -- State handlers --
@dp.message_handler(state=MainMsg.mess)
async def procces_MainMsg_data(msg: types.Message, state: FSMContext):
    await state.update_data(mess=msg.text)
    await MainMsg.next()
    yesButton = KeyboardButton("Да!")
    noButton = KeyboardButton("Нет")
    accept_kb_prod = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(yesButton, noButton)
    await msg.answer("Подтвердить?", reply_markup=accept_kb_prod)


@dp.message_handler(state=MainMsg.accept)
async def procces_accept(msg: types.Message, state: FSMContext):
    global ToSeV
    if msg.text == "Да!":
        new_msg = await state.get_data()
        print(ToSeV)
        setMSG(ToSeV, new_msg['mess'])
        await state.finish()
        await msg.answer('Все готово!', reply_markup=kb.admin_kb)
    else:
        await state.finish()
        await msg.answer("-- Главное меню --", reply_markup=kb.admin_kb)


@dp.message_handler(state=Mainling.mail)
async def process_mail(msg: types.Message, state: FSMContext):
    await state.update_data(mail=msg.text)
    await Mainling.next()
    yesButton = KeyboardButton("Да!")
    noButton = KeyboardButton("Нет")
    accept_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(yesButton, noButton)
    await msg.answer("Подтвердить?", reply_markup=accept_kb)


@dp.message_handler(state=Mainling.accept)
async def process_accept(msg: types.Message, state):
    if msg.text == 'Да!':
        user_data = await state.get_data()
        for user_id in user_cur.execute('SELECT user_id FROM users'):
            await bot.send_message(user_id[0], user_data['mail'])
        await msg.answer("Рассылка создана: ", reply_markup=kb.admin_kb)
        await state.finish()
    else:
        await state.finish()
        await msg.answer("-- Главное меню --", reply_markup=kb.admin_kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
