import MOKO

MOKO.Driver("MyDriver", "Check", "")
MOKO.Driver("MyDriver", "init", "")
MOKO.Driver("MyDriver", "set", "range = 2,24 5,49")
result = MOKO.Driver("MyDriver", "get", "inrange = 5", "string")
MOKO.Report("check_1", "set", "string", result)
result = MOKO.Driver("MyDriver", "get", "inrange = 6", "string")
MOKO.Report("check_2", "set", "string", result)

MOKO.Driver("MyDriver", "set", "range = 6,78 1,24")
result = MOKO.Driver("MyDriver", "get", "inrange = 5", "string")
MOKO.Report("check_3", "set", "string", result)
result = MOKO.Driver("MyDriver", "get", "inrange = 7", "string")
MOKO.Report("check_4", "set", "string", result)

MOKO.EndScript()