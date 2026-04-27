import MOKO
import MCLK

png_file = MCLK.GetPngFile()
MOKO.Report("New_png_file", "set", "picture", png_file)
MOKO.Report("New_png_file", "save", "picture", "png")

MOKO.EndScript()