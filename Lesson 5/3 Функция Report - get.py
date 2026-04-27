import MOKO

string = MOKO.Report("String", "get", "string", "", "string")
print(string)

table = MOKO.Report("Table", "get", "table", "", "arraystring")
print(table)

screen = MOKO.Report("Picture", "get", "picture", "", "string")

MOKO.EndScript()