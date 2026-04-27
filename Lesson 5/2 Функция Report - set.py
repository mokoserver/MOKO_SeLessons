import MOKO

MOKO.Report("String", "set", "string", "string")

MOKO.Report("Table", "info", "table", "№#50;Случайное число#110")
MOKO.Report("Table", "set", "table", "1;3\\r2;4")

screen = MOKO.Program("control", "get", "screenshot", "string")
MOKO.Report("Picture", "set", "picture", screen)

MOKO.EndScript()