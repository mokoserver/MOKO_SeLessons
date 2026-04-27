import MOKO
import MGPH
import time

MGPH.ShowLine([0,1])
MGPH.ShowLine(["Plot 2", "Plot 3"])

MGPH.ShowLineOnly([0,1,2])
time.sleep(2)
MGPH.ShowLineOnly(["Plot 1", "Plot 2", "Plot 3"])

MOKO.EndScript()