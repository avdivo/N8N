import re


def escape_md(text: str) -> str:
    # ] ставим сразу после открывающей скобки — так он не закрывает класс
    return re.sub(r"([][*()~`>#+\-=|{}.!_])", r"\\\1", text)


# Проверка
test = "_test_ и _ещё_ один _"
result = escape_md(test)
print(result)
