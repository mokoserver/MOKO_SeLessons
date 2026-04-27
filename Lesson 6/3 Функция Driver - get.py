import MOKO

value = MOKO.Driver("ExDriver", "get", "Value", "string")
MOKO.Report("UserValue", "set", "string", value)

MOKO.Report("Random_values", "info", "table", "№#50;Случайное число#110")
for i in range(10):
    random_value = MOKO.Driver("ExDriver", "get", "Random", "string")
    MOKO.Report("Random_values", "set", "table", f"{i+1};{random_value}")

MOKO.EndScript()