import os
from openpyxl import workbook, load_workbook


class Liquid():
    name = ''
    taste = ''
    prod = ''
    strenght = 0
    price = 0
    availability = False

    def __init__(self, _name, _taste, _prod, _strenght, _price, _availability):
        self.name = _name
        self.taste = _taste
        self.prod = _prod
        self.strenght = _strenght
        self.price = _price
        if _availability == 1:
            self.availability = True
        else:
            self.availability = False

    def get_info(self):
        print_str = "Жидкость: " + self.name + " " + self.taste + " Крепкость - " + str(
            self.strenght) + " Цена: " + str(self.price) + " Наличие" + str(self.availability)
        return print_str


def get_names():
    wb = load_workbook(filename="./sources/product.xlsx")
    wb.active = 0
    prod_sheet = wb.active
    names = set()
    i = 2
    while prod_sheet['A' + str(i)].value is not None:
        names.add(prod_sheet['A' + str(i)].value)
        i += 1
    return list(names)



MSG = f"""
    ЖИДКОСТИ 👇🏻 

➖ {"<b>"}Hotspot Fuel (30ml SALT 50mg){"</b>"}➖
{"<b>"}Цена: 350р{"</b>"}

Вкусы:
🥝🍈 Киви Помело
🥝🍌 Киви Банан
🍏 🍐Яблоко Груша
🥚🍋 Личи Лайм
🍍🫐 Ананас Ежевика
☘️ 🍓Кислые лесные ягоды
🍍 🥥Ананас Кокос
🍋 🍒Брусника Лимон 
🌲🥑 Хвоя Грейпфрут 
🫐🍈 Дыня Черника 
🥭🍑 Манго Персик
🥭🍈 Манго Грейпфрут
☘️🫐 Смородина Мята
🍑🍈 Персик Маракуя

➖ {"<b>"}HotSpot Don't Chew It (30ml SALT 50mg){"</b>"} ➖
{"<b>"}Цена: 350р{"</b>"}

Вкусы:
🍑 Жвачка Сочный Персик
🍉 Жвачка Арбуз
🍇 Жвачка Ледяной Виноград
🍒 Жвачка Ледяная Вишня
🍏 Жвачка Спелое зеленое яблоко
🥭 Жвачка Маракуя

➖ {"<b>"}SMPL (30ml SALT 50mg){"</b>"} ➖
{"<b>"}Цена: 350р{"</b>"}
Вкусы:
🥭Yellow 
🍓Purple 
🫐Violet 
🥚Pink 
🍒Plum 
🍏Ruby

➖ {"<b>"}Мишка (30ml SALT 50mg){"</b>"}➖
{"<b>"}Цена: 350р{"</b>"}

Вкусы:
🍩 Булочка с корицей
🚬 Кремовый табак

➖ {"<b>"}Морс Микс (30ml SALT 50mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🌲 Алтайский 
🍇 Карельский 
🏡 Садовый 
🌳 Лесной 
🥝 Фьюжн 
🍓 Южный

➖ {"<b>"}Mad (30ml SALT 60mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🌵 Кактус-Лайм
🥤 Морс с клюквой

 ➖ {"<b>"}Husky Premium (30ml SALT 45mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🍓YOGI DOGGY - смесь йогурта, персика, клубники и льда
🧊 ANIMAL JAM - со вкусом лесных ягод, малинового джема и льда
🍈YELLOW KING - со вкусом медовой дыни, вьетнамской дыни, алоэ и льда 
🍍MIAMI SNOW - со вкусом ананаса, личи, банана и льда
🫐DARK FLESH - смесь черники, гуавы и льда
🥝GREEN LAND - со вкусом киви, лимона, кранберри и льда
🥭BLOOD BOY - со вкусом австралийского, двойного и сладкого манго

➖ {"<b>"}Husky Double Ice (30ml SALT 45mg) ➖
Цена: 330р{"</b>"}

Вкусы:
🧊🥤Winter river 
🧊🥭Artic strike
🧊🍈North sweet 
🧊 🥝Chilly Kiwi
🧊 🍌Frosty palm
🧊 🍓Siberian black

 ➖ {"<b>"}Husky Mint Series (30ml SALT 45mg) ➖
Цена: 330р{"</b>"}

Вкусы:
🌱🍉Water Place
🌱🍋Citrus days 
🌱🍇Juice grapes 
🌱🫐Berry Hunter
🌱🍓Red Garden
🌱🫐Blue up

 ➖ {"<b>"}Gang (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🫐 🥤 Фанта с Голубикой
🍏 🫐 Яблоко Черника
🫐 🍓 Черника Малина
🍧 🍓 Малиновое Мороженое
🍇 🍉 Фруктовый Мармелад
🧊 🍉 Ледяной Арбуз
🍓 🧊 Ягодный Пломбир
🫐 🧊 Смородина Ежевика
🫐 🍓 Ягодный Микс
🍓 🥤 Клубника Ванильная кола

 ➖ {"<b>"}NEW Gang Ice (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🧊 🍇 Виноградный Бабл Гам
🧊 🫐 Черничный Бабл Гам
🧊 🥝 Фруктовый Бабл Гам
🧊 🍊 Апельсиновый Бабл Гам
🧊 🍓 Клубничный Бабл Гам

➖ {"<b>"}Beast (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
💙Blue
💖Pink 
💜Purple 
💛Yellow

➖ {"<b>"}Toxic Salt (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🍓 Strawberry 
🫐 Forest Berries

💨 {"<b>"}ПОД-СИСТЕМЫ

Aegis Hero(LE) Красно-Белые - 2650р
Aegis Hero - 2400р
Pasito 2 - 2400р
Manto Aio - 2300р
Charon baby - 1350р
Charon baby plus - 1800р
Santi - 1900р{"</b>"}

⚙️{"<b>"} Испарители/Картриджи{"</b>"}

Испаритель Charon Baby (0.6ОМ) - 200р
Испаритель Charon baby plus (0.4ОМ) - 210р
Испаритель Aegis Hero/Boost (0.4ОМ) - 250р
"""


# Haski = Liquid("Haski", "Дыня/Банан", "Hz", 5, 450, 1)
# print(Haski.get_info())
