def str_insert(id: int, val: str, st: str) -> str:
    return st[:id] + val + st[id:]


def ref_str(string_: str) -> str:
    is_open_tag = True
    i = 0
    while i < len(string_):
        if string_[i] == "➖":
            if is_open_tag:
                string_ = str_insert(i + 1, f'{"<b>"}', string_)
                is_open_tag = False
            else:
                string_ = str_insert(i + 1, f'{"</b>"}', string_)
                is_open_tag = True
        i += 1
    return string_

# --------------------------------------------------------------------------

def setMSG(_type: str, message: str) -> None:
    file = ""
    if _type == "L":
        file = open("LiqMess.txt", 'w', encoding="utf-8")
    elif _type == "V":
        file = open("VapeMess.txt", 'w', encoding="utf-8")
    elif _type == "C":
        file = open("ConsMess.txt", 'w', encoding="utf-8")
    elif _type == "O":
        file = open("OneVapeMess.txt", 'w', encoding="utf-8")
    else:
        return 1
    file.write(ref_str(message))
    file.close()


def getMSG(_type: str) -> str:
    file = None
    if _type == "L":
        file = open("LiqMess.txt", 'r', encoding="utf-8")
    elif _type == "V":
        file = open("VapeMess.txt", 'r', encoding="utf-8")
    elif _type == "C":
        file = open("ConsMess.txt", 'r', encoding="utf-8")
    elif _type == "O":
        file = open("OneVapeMess.txt", 'r', encoding="utf-8")
    else:
        return ""
    mess = file.read()
    if mess != "":
        file.close()
        return mess
    else:
        file.close()
        return "Технический сбой!"

#--------------------------------------------------------------------
