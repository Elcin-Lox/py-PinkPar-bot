from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# ---Main menu---
rangeButton = KeyboardButton("🛒 Ассортимент")
messengerButton = KeyboardButton("🧑🏼‍💻 Менеджер")
mediaButton = KeyboardButton("📲 Соц. сети")
aboutButton = KeyboardButton("О нас")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(rangeButton)
main_kb.row(messengerButton)
main_kb.insert(mediaButton)

# --Media--
media_buttons = [InlineKeyboardButton(text="👨🏻‍💻Вконтакте", url="https://vk.com/pinkpar73"),
                 InlineKeyboardButton(text="✈ Telegram", url="https://t.me/Pink_PaR_73"),
                 ]
media_inline_kb = InlineKeyboardMarkup(row_width=1)
media_inline_kb.add(*media_buttons)

# --Manage buttons--
manage_buttons = [InlineKeyboardButton(text="Менеджер", url="t.me/sqdmiller"),
                  InlineKeyboardButton(text="Менеджер НГ", url="t.me/Evrey_Evrey"),
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
