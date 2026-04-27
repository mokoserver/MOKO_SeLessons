import MOKO
import MOSC

UN = 'CSMinfo'  # Utility Name

#Region Этапы регистрации:
#hash Заполнение формы

def get_info(reports):
    string = ''
    reports_names = ''
    for report in reports:
        reports_names = reports_names + report + ";"
        string = string + MOKO.Utility(UN, "get", report, "string") + ';'

    MOKO.Report(reports_names, "set", "strings", string)

reports = ['RegistrationID',  # Регистрационный номер заказа
           'cipher',  # Идентификация (шифр) образца
           'IMEI',  # IMEI образца
           'the_start_date_of_the_test',  # Дата начала испытаний
           'date_of_completion_of_the_test',  # Дата завершения испытаний
           'T_nom',  # Температура окружающего воздуха
           'fi_nom',  # Относительная влажность воздуха
           'P_nom',  # Атмосферное давление
]

MOKO.Program("tree", "set", "select = Заполнение формы")
MOKO.Stage("Регистрация")
MOKO.Utility(UN, "set", "info")

MOSC.Utility_to_Report(reports, UN, "strings")
MOKO.Program("tree", "set", "chosen = passed")

#EndRegion Этапы регистрации:

MOKO.EndScript()