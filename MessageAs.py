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



MSG = f"""ЖИДКОСТИ 👇🏻 

➖ {"<b>"}Hotspot Fuel (30ml SALT 50mg)➖
Цена: 350р{"</b>"}

Вкусы:
🥝🍈 Киви Помело
🍏 🍐Яблоко Груша
🥚🍋 Личи Лайм
🍍🫐 Ананас Ежевика
🍍 🥥Ананас Кокос
🫐🍈 Дыня Черника 
🥭🍈 Манго Грейпфрут
☘️🫐 Смородина Мята
🍑🍈 Персик Маракуя

➖ {"<b>"}HotSpot Don't Chew It (30ml SALT 50mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🥭 Жвачка Маракуя

➖{"<b>"} SMPL (30ml SALT 50mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🥭Yellow - холодный манго с бананом
🫐Violet - Ледяная черника с клубникой
🥚Pink - ледяная малина с личи
🍓Red - Спелая малина с клубникой 
🍒Plum - Ледяная вишня с черникой
🍏Ruby - Ледяное яблоко с вишней и клубникой 
🍇Indigo - Спелый виноград и лайм
🥝Green - Киви с лаймом
🍌Coral - Сладкий банан со льдом 

➖ {"<b>"}Мишка (30ml SALT 50mg)➖
Цена: 350р{"</b>"}

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

 ➖ {"<b>"}Husky Premium (30ml SALT 45mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🍈YELLOW KING - со вкусом медовой дыни, вьетнамской дыни, алоэ и льда 
🥭BLOOD BOY - со вкусом австралийского, двойного и сладкого манго

➖ {"<b>"}Husky Double Ice (30ml SALT 45mg) ➖
Цена: 330р{"</b>"}

Вкусы:
🧊🥭Artic strike
🧊🍈North sweet 

 ➖ {"<b>"}Husky Mint Series (30ml SALT 45mg) ➖
Цена: 330р{"</b>"}

Вкусы:
🌱🍋Citrus days 
🌱🍇Juice grapes 
🌱🫐Berry Hunter

 ➖ {"<b>"}Gang (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🫐 🍓 Черника Малина
🧊 🍉 Ледяной Арбуз
🫐 🧊 Смородина Ежевика
🫐 🍓 Ягодный Микс
🍓 🥤 Клубника Ванильная кола

 ➖ {"<b>"}NEW Gang Ice (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🧊 🍇 Виноградный Бабл Гам
🧊 🫐 Черничный Бабл Гам
🧊 🍊 Апельсиновый Бабл Гам
🧊 🍓 Земляничный Бабл Гам

➖ {"<b>"}MAD SALT (30ml SALT 60mg) ➖
Цена: 350р{"</b>"}

Вкусы:
🧊 🥚 Холодный Личи
🥝 🍍 Киви Ананас
🌵 🔥 Кактус Лайм
🥤 🍒 Dr.pepper - вишневый лимонад
🫒 🍇 Виноград Лайм
🥤 ☀️ Клюквенный Морс
🍓 🍭 Клубника Гуава
🍌 🧊 Тропический Микс
🥭 🧊 Холодное Манго
🫒💖 Лайм Бабл-гам
🍊🧡 Апельсиновая газировка
🍈 🥝 Киви Дыня
🍏 🍈 Яблоко Маракуя
🥤 🍑 Летний лимонад

➖ {"<b>"}Beast (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
💙Blue

➖ {"<b>"}Toxic Salt (30ml SALT 50mg) ➖
Цена: 300р{"</b>"}

Вкусы:
🍓 Strawberry 
🫐 Forest Berries

{"<b>"}💨 ПОД-СИСТЕМЫ

Aegis Hero Красно-Белые (LE) - 2650р
Aegis Hero - 2400р
Aegis Boost Le - 2400р
Aegis Boost 2 (B60) - 2800р
Aegis Nano - 2000р
Aegis One - 1700р
Manto Aio - 2300р
Charon baby - 1350р
Charon baby plus - 1800р
Charon baby Mystery box - 1350р
Santi - 1900р
Vaporesso osmall 2 - 950р

⚙️ Испарители/Картриджи

Испаритель Charon Baby (0.6ОМ) - 200р
Испаритель Charon baby plus (0.4ОМ) - 210р
Испаритель Aegis Hero/Boost (0.4ОМ) - 250р{"</b>"}"""


# Haski = Liquid("Haski", "Дыня/Банан", "Hz", 5, 450, 1)
# print(Haski.get_info())
