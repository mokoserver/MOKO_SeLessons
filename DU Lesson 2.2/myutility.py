import MOKO

MOKO.Utility("MyUtility", "set", "info")

surname = MOKO.Utility("MyUtility", "get", "surname", "string")
MOKO.Report("user_surname", "set", "string", surname)

name = MOKO.Utility("MyUtility", "get", "name", "string")
MOKO.Report("user_name", "set", "string", name)

patronymic = MOKO.Utility("MyUtility", "get", "patronymic", "string")
MOKO.Report("user_patronymic", "set", "string", patronymic)

MOKO.EndScript()