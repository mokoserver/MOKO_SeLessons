import MOKO

message = MOKO.Utility("ExUtility", "get", "text", "string")
MOKO.Report("Message", "set", "string", message)

MOKO.EndScript()