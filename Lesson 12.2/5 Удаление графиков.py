import MOKO
import MGPH
import time

MGPH.DeleteLine([0,1,2])
time.sleep(4)
MGPH.DeleteLine(["Plot 1", "Plot 2"])
time.sleep(4)
MGPH.DeleteLine(["Plot 3"])

MOKO.EndScript()