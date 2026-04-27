import MOKO
import MTLG

alpha = MOKO.Telegram("alpha", "get", "list", "string")
MOKO.Report("alpha", "set", "string", alpha)
MTLG.TelegramReport("alpha", "set", "string", alpha)

MOKO.EndScript("passed")