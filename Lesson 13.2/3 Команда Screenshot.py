import MOKO
import MCLK

MCLK.Screenshot()

screenshot = MCLK.GetScreenshot()
MOKO.Report("image_screenshot", "set", "picture", screenshot)
MOKO.Report("image_screenshot", "save", "picture", "png")

MOKO.EndScript()