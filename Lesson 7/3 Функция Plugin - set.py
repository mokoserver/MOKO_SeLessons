import MOKO
from time import sleep

MOKO.Plugin("ExPlugin", "set", "ChangeLedLoop")
sleep(2)

MOKO.Plugin("ExPlugin", "set", "Number1 = 10")
MOKO.Plugin("ExPlugin", "set", "Number2 = 6")

MOKO.Plugin("ExPlugin", "set", "string = Hello, World!")

MOKO.Plugin("ExPlugin", "set", "ShowTab = Info")
sleep(1)
MOKO.Plugin("ExPlugin", "set", "ShowTab = Main")
sleep(1)
MOKO.Plugin("ExPlugin", "set", "ShowTab = Graph")

MOKO.Plugin("ExPlugin", "set", "Graph = start")
sleep(3)
MOKO.Plugin("ExPlugin", "set", "Graph = stop")

MOKO.Plugin("ExPlugin", "set", "Screenshot")

MOKO.EndScript()