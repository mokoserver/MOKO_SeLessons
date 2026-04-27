import MOKO
from MOSC import *
import random


def measurement_6_6_3(band, command, hash_name, report_name, type, code_scheme, limits):
    if status_tree(hash_name):
        global index
        MOKO.Stage(f"CMW500 -> command -> {command}", "driver")
        data = str(round(random.random() * 10,2))
        if not limits[0] < float(data.replace(",", ".")) < limits[1]:
            MOKO.Report("sig_6_6_3_status", "set", "string", "Не выполняется")
        MOKO.Report(report_name, "set", "table", data)
        MOKO.Program("tree", "set", "chosen = passed")


MOKO.Report("sig_6_6_3_status", "set", "string", "Выполняется")

def table_report(report_name):
    table_data = MOKO.Report(report_name, "get", "table", 'table', "arraystring")
    MOKO.Report(report_name, "clear", "table", "string")
    MOKO.Report(report_name, "info", "table", 'Проверяемый параметр#250;GMSK#50;EGPRS#50;GPRS#50;HSCSD#50;')
    params = ["Ошибка по частоте, несущей", "Среднеквадратическая ошибка по фазе", "Пиковая ошибка по фазе", "Максимальная выходная мощность"]

    for j in range(len(params)):
        string = params[j] + ";"
        for i in range(int(len(table_data) / 4)):
            value = table_data[4 * i + j]
            string = string + value + ";"
        MOKO.Report(report_name, "set", "table", string)


#########################################################################################################################

    ###########      #############           ####         ####            #############    #############    #############
    ##               ##                     ##  ##       ##  ##           ##         ##    ##         ##    ##         ##
    ##               ##                    ##    ##     ##    ##          ##         ##    ##         ##    ##         ##
    ##               ##                   ##      ##   ##      ##         ##         ##    ##         ##    ##         ##
    ##               #############       ##        #####        ##        #############    ##         ##    ##         ##
    ##    #######               ##      ##                       ##                  ##    ##         ##    ##         ##
    ##    ##   ##               ##     ##                         ##                 ##    ##         ##    ##         ##
    ##         ##               ##    ##                           ##                ##    ##         ##    ##         ##
    #############    #############   ##                             ##    #############    #############    #############

#########################################################################################################################

#Region 6.6.3 GSM 900
#description: Диапазон частот;Частотный канал;Мощность;Измерение

MOKO.Stage("CMW500 -> init", "driver")
MOKO.Stage("CMW500 -> reset", "driver")

MOKO.Stage("CMW500 -> settings", "driver")

# виды измерений
measur900 = [['MevModCurr FrequencyError', 'g09_ch62_value1', [-90, 90]], #hash g09_ch62_value1: GSM 900;62;5;PERR RMS
             ['MevModCurr PhaseErrorRMS', 'g09_ch62_value2', [-5, 5]], #hash g09_ch62_value2: GSM 900;62;5;PERR Peak
             ['MevModCurr PhaseErrorPeak', 'g09_ch62_value3', [-20, 20]], #hash g09_ch62_value3: GSM 900;62;5;FERR
             ['MevModCurr BurstPower', 'g09_ch62_value4', [23,25]]] #hash g09_ch62_value4: GSM 900;62;5;Max output power

types = ["GMSK", "EGPRS", "GPRS", "HSCSD"]
code_schemes = ["MC1", "MC5", "C1", "C1"]
prefix900 = "sig_6_6_3_GSM900"

for j in range(len(types)):
    for i in measur900:
        measurement_6_6_3("GSM900", i[0], i[1], prefix900, type, code_schemes[j], i[2])

table_report(prefix900)


#EndRegion 6.6.3 GSM 900

MOKO.EndScript()


