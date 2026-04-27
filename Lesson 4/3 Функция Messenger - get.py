import MOKO

string = MOKO.Messenger("get", "Messenger - get.png", "Пожалуйста, введите что-нибудь", "string")
MOKO.Messenger("set", "head", string)

bool = MOKO.Messenger("get", "Messenger - get.png", "Пожалуйста, нажмите на любую кнопку.", "boolean")
if bool:
    MOKO.Messenger("set", "Тип boolean", "Вы нажали кнопку 'Yes'")
else:
    MOKO.Messenger("set", "Тип boolean", "Вы нажали кнопку 'No'")

choice = MOKO.Messenger("get", "Language. Язык.jpg", "Пожалуйста, выберите язык.", "choice=English;Русский")
MOKO.Messenger("set", "Language. Язык.jpg", f"Вы выбрали {choice}")

path = MOKO.Messenger("get", "Выбор директории", "Пожалуйста, укажите путь.", "path")
MOKO.Messenger("set", "Выбор директории", path)

MOKO.EndScript()