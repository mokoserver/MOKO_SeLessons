import MOKO
import MGPH
from time import sleep

MGPH.ScreenshotGraph()
sleep(2)
MGPH.ScreenshotWindow()

screen = MGPH.GetScreenshotGraph()
MOKO.Report("Screenshot_graph", "set", "picture", screen)
screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_window", "set", "picture", screen)

MOKO.EndScript()