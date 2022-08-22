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
from MessageAs import MSG
import settings as st

TOKEN = st.TOKEN

# --- Bot ---
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class Mainling(StatesGroup):
    mail = State()
    accept = State()


class SetProd(StatesGroup):
    prod = State()
    accept = State()


class DelProd(StatesGroup):
    prod = State()
    accept = State()


# --- DataBase's ---
user_db = sqlite3.connect('user.db')
prod_db = sqlite3.connect('product.db')

user_cur = user_db.cursor()
prod_cur = prod_db.cursor()

user_cur.execute('''CREATE TABLE IF NOT EXISTS users(
                name TEXT NOT NULL,
                user_id BIGINT);
''')

prod_cur.execute('''CREATE TABLE IF NOT EXISTS products(
                name TEXT NOT NULL,
                taste TEXT NOT NULL,
                strength INTEGER,
                price INTEGER,
                place TEXT NOT NULL);
''')

prod_db.commit()
user_db.commit()

admins = [7440902180, 8105455190]


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


def presentForDb(data: str) -> list:
    data = data.split(' ')

    if len(data) != 5:
        return []

    if not data[2].isdigit() or not data[3].isdigit():
        return []

    for val_i in range(len(data)):
        if "-" in data[val_i] or "_" in data[val_i]:
            print(1)
            #data[val_i] = data[val_i].replace("-", " ")
            data[val_i] = data[val_i].replace("_", " ")

    data[2] = int(data[2])
    data[3] = int(data[3])
    data[4] = data[4].upper()

    return data


def presentForUser(_place: str) -> str:
    """     """
    cur_name = ''
    isNameUse = False

    prod_cur.execute(f"SELECT * FROM products WHERE place = (?) ORDER BY name", _place)
    all_prod = prod_cur.fetchall()

    if len(all_prod) == 0:
        return "Сожалеем... Пока в этом районе нет товара в наличии."

    pres_str = "ЖИДКОСТИ 👇🏻\n"
    for val in all_prod:
        if val[0] != cur_name:
            cur_name = val[0]
            isNameUse = False

        if isNameUse:
            pres_str += val[1] + "\n"
        else:
            pres_str += fmt.hbold("\n➖ " + val[0] + " ➖ \n")
            pres_str += fmt.hbold("Цена: " + str(val[3]) + "р\n\n") + "Вкусы: \n"
            pres_str += val[1] + '\n'
            isNameUse = True

    pres_str += "\n Сделать заказ 👇"

    return pres_str

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    if isAdmin(msg.from_user.id):
        await msg.answer("Здравствуйте, {0.first_name}!".format(msg.from_user), reply_markup=kb.admin_kb)
    else:
        user_cur.execute('''SELECT user_id FROM users ''')
        if not isUserExists(msg.from_user.id, user_cur):
            user_cur.execute(f'''INSERT INTO users VALUES (?, ?)''', (str(msg.from_user.first_name), msg.from_user.id))
            user_db.commit()
            print("111")
        await msg.answer("Добро пожаловать, {0.first_name}!\nЗдесь вы можете ознакомится с ассортиментом товара и ценами нашего магазина💥".format(msg.from_user), reply_markup=kb.main_kb)



@dp.message_handler(commands=["cancel"], state="*")
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("-- Главное меню --", reply_markup=kb.main_kb)

@dp.message_handler()
async def media(msg: types.Message):
    if msg.text == "📲 Соц. сети":
        await msg.answer("Найти вы нас можете тут:", reply_markup=kb.media_inline_kb)
    if msg.text == "🧑🏼‍💻 Менеджер":
        await msg.answer("Сделать заказ:", reply_markup=kb.manage_inline_kb)
    if msg.text == '🛒 Ассортимент':
        await msg.answer(MSG, parse_mode=types.ParseMode.HTML)
    if msg.text == 'Назад':
        await msg.answer('Главное меню', reply_markup=kb.main_kb)

    if msg.text == "Левый берег":
        await msg.answer(presentForUser("Л"), reply_markup=kb.manage_inline_l_kb, parse_mode="HTML")
    if msg.text == "Правый берег":
        await msg.answer(presentForUser('П'), reply_markup=kb.manage_inline_r_kb, parse_mode="HTML")


    if msg.text == 'Создать рассылку':
        if isAdmin(msg.from_user.id):
            await Mainling.mail.set()
            await msg.answer("Введите текст рассылки:")
    if msg.text == "Показать все строки":
        if isAdmin(msg.from_user.id):
            for value in prod_cur.execute("SELECT *, rowid FROM products"):
                await msg.answer(value)
    if msg.text == "Добавить строку":
        if isAdmin(msg.from_user.id):
            await SetProd.prod.set()
            await msg.answer("Введите данные: \n *Пример* Название Вскус Крепкость Цена Район(Ц/Б/Д/C/К)")
    if msg.text == "Удалить строку":
        if isAdmin(msg.from_user.id):
            await DelProd.prod.set()
            await msg.answer("Введите номер строки, которую хотите удалить")

    if msg.text == "111":
        for value in user_cur.execute('''SELECT * FROM users'''):
            print(value)
    if msg.text == "222":
        presentForUser("П")



@dp.message_handler(state=DelProd.prod)
async def process_del_data(msg: types.Message, state: FSMContext):
    await state.update_data(prod=msg.text)
    await DelProd.next()
    yesButton = KeyboardButton("Да!")
    noButton = KeyboardButton("Нет")
    accept_kb_prod = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(yesButton, noButton)
    await msg.answer("Подтвердить?", reply_markup=accept_kb_prod)


@dp.message_handler(state=DelProd.accept)
async def process_accept(msg: types.Message, state: FSMContext):
    if msg.text == "Да!":
        prod_data = await state.get_data()
        dell = prod_data['prod']
        prod_cur.execute(f"DELETE FROM products WHERE rowid = '{dell}'")
        prod_db.commit()
        await state.finish()
        await msg.answer("Запись успешно удалена!", reply_markup=kb.admin_kb)
    else:
        await state.finish()
        await msg.answer("Главное меню: ", reply_markup=kb.admin_kb)


@dp.message_handler(state=SetProd.prod)
async def prosess_get_data(msg: types.Message, state: FSMContext):
    await state.update_data(prod=msg.text)
    await SetProd.next()
    yesButton = KeyboardButton("Да!")
    noButton = KeyboardButton("Нет")
    accept_kb_prod = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(yesButton, noButton)
    await msg.answer("Подтвердить?", reply_markup=accept_kb_prod)


@dp.message_handler(state=SetProd.accept)
async def process_accept(msg: types.Message, state: FSMContext):
    if msg.text == "Да!":
        prod_data = await state.get_data()
        if not presentForDb(prod_data['prod']):
            await msg.answer("Некорректный ввод, попробуйте еще раз!")
            await SetProd.prod.set()
        else:
            prod_cur.execute(f"INSERT INTO products VALUES (?, ?, ?, ?, ?)", (presentForDb(prod_data['prod'])))
            prod_db.commit()
            await msg.answer("Запись добавлена!", reply_markup=kb.admin_kb)
            await state.finish()
    else:
        await state.finish()
        await msg.answer("Главное меню: ", reply_markup=kb.admin_kb)


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
        await msg.answer("Главное меню: ", reply_markup=kb.admin_kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
