
"""
def getMSG() -> str:
    global mess_file
    message = mess_file.read()
    if message != "":
        return message
    else:
        return MSG1
"""

"""
def setMSG(message: str) -> None:
    if message == "" or message == None:
        return
    mess_file.write(message)
"""

def getMSG() -> str:
    global MSG1
    if MSG1 is not None:
        return MSG1
    return ""


def setMSG(message: str) -> None:
    global MSG1
    if message is not None:
        MSG1 = message


MSG2 = ""


MSG1 = f"""
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

