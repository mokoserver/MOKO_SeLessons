import MOKO
import MGPH
from time import sleep

MOKO.Plugin("Graph", "init", "")
sleep(4)
MGPH.ClearGraph()

name = "First graph"
ArrOy = [0,1,2,3,4,5]
ArrOx = [0,1,2,3,4,5]
LineWidth = "5"
Color = "00FF00"
Visible = "False"
MGPH.AddLine(name, ArrOy, ArrOx, LineWidth, Color, Visible)

MOKO.EndScript()