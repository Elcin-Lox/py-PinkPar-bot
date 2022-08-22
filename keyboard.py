from aiogram.types import  \
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

media_buttons = [InlineKeyboardButton(text="👨🏻‍💻Вконтакте", url="https://vk.com/pinkpar73"),
                  InlineKeyboardButton(text="✈ Telegram", url="https://t.me/Pink_PaR_73"),
                  ]
media_inline_kb = InlineKeyboardMarkup(row_width=1)
media_inline_kb.add(*media_buttons)

manage_btn_1 = InlineKeyboardMarkup(text="Менеджер", url="t.me/sqdmiller")
manage_btn_2 = InlineKeyboardMarkup(text="Менеджер", url="t.me/sqdmiller")

manage_inline_l_kb = InlineKeyboardMarkup(row_width=1).add(manage_btn_1)
manage_inline_r_kb = InlineKeyboardMarkup(row_width=1).add(manage_btn_2)

manage_buttons = [InlineKeyboardButton(text="Менеджер", url="t.me/sqdmiller"),
                 InlineKeyboardButton(text="Менеджер НГ", url="t.me/Evrey_Evrey"),
                 ]
manage_inline_kb = InlineKeyboardMarkup(row_width=1)
manage_inline_kb.add(*manage_buttons)

# ---Range menu---
buttons = ["Левый берег", "Правый берег",  "Назад"]
range_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(*buttons)


# ---Admin menu---
seeAllButton = KeyboardButton("Показать все строки")
addStrButton = KeyboardButton("Добавить строку")
removeSrtByIdButton = KeyboardButton("Удалить строку")
mailingButton = KeyboardButton("Создать рассылку")
statsButton = KeyboardButton("Статистика")
admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_kb.add(seeAllButton)
admin_kb.add(addStrButton, removeSrtByIdButton)
admin_kb.add(mailingButton)
admin_kb.add(statsButton)