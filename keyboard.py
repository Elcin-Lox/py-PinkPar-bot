from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

mainMenuBtn = KeyboardButton("🔙 Главное меню")

# ---Main menu---
rangeButton = KeyboardButton("🛒 Ассортимент")
messengerButton = KeyboardButton("🧑🏼‍💻 Менеджер")
mediaButton = KeyboardButton("📲 Соц. сети")
aboutButton = KeyboardButton("О нас")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(rangeButton)
main_kb.row(messengerButton)
main_kb.insert(mediaButton)

# --- Smt menu ---
smt1btn = KeyboardButton("Ассортимент здесь")
smt2btn = KeyboardButton("Гугл таблица")
smt_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(smt1btn)
smt_kb.add(smt2btn)
smt_kb.add(mainMenuBtn)

# --- Choose menu ---
LiqBtn = KeyboardButton("Жидкости 🧪")
VapeBtn = KeyboardButton("Под-Системы 💨")
ConsBtn = KeyboardButton("Расходники ⚙")
OSVapeBtn = KeyboardButton("Одноразовые электронные сигареты 😶‍🌫️")
choose_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(LiqBtn)
choose_kb.row(VapeBtn)
choose_kb.insert(ConsBtn)
choose_kb.row(OSVapeBtn)
choose_kb.row(mainMenuBtn)

# --Media--
media_buttons = [InlineKeyboardButton(text="👨🏻‍💻Вконтакте", url="https://vk.com/pinkpar73"),
                 InlineKeyboardButton(text="✈ Telegram", url="https://t.me/Pink_PaR_73"),
                 ]
media_inline_kb = InlineKeyboardMarkup(row_width=1)
media_inline_kb.add(*media_buttons)

# --Manage buttons--
manage_buttons = [InlineKeyboardButton(text="Менеджер", url="t.me/sqdmiller"),
                  InlineKeyboardButton(text="Менеджер НГ", url="t.me/manager_pinkpar"),
                  ]
manage_inline_kb = InlineKeyboardMarkup(row_width=1)
manage_inline_kb.add(*manage_buttons)

# ---Admin menu---
setMainMsg = KeyboardButton("Задать новое главное сообщение")
mailingButton = KeyboardButton("Создать рассылку")
statsButton = KeyboardButton("Статистика")
admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_kb.add(setMainMsg)
admin_kb.add(mailingButton)
admin_kb.add(statsButton)

# --- SetMess menu ---
setLiqMess = KeyboardButton('Задать сообщение "Жидкости"')
setVapeMess = KeyboardButton('Задать сообщение "Под-системы"')
setConsMess = KeyboardButton('Задать сообщение "Расходники"')
setOSVapeMess = KeyboardButton('Задать сообщение "Одноразовые"')
setMess_kb = ReplyKeyboardMarkup(resize_keyboard=True)
setMess_kb.add(setLiqMess)
setMess_kb.add(setVapeMess)
setMess_kb.add(setConsMess)
setMess_kb.add(setOSVapeMess)
setMess_kb.add(mainMenuBtn)
