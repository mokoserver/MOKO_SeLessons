import MOKO
import MGPH
from time import sleep

MGPH.Autoscale("OnlyOx")
sleep(4)
MGPH.Autoscale("OnlyOy")

MOKO.EndScript()