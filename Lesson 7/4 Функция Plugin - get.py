import MOKO

sum = MOKO.Plugin("ExPlugin", "get", "Sum", "string")
MOKO.Report("ExPlugin_sum", "set", "string", sum)

string = MOKO.Plugin("ExPlugin", "get", "string", "string")
MOKO.Report("ExPlugin_string", "set", "string", string)

screen = MOKO.Plugin("ExPlugin", "get", "InstantScreenshot", "string")
MOKO.Report("ExPlugin_screen", "set", "picture", screen)

MOKO.EndScript()