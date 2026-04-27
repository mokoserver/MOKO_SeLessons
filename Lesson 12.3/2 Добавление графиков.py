import MOKO
import time
import numpy as np
import MGPH

MOKO.Report('Graph', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2):
    i = 0
    number = 0
    sin_with_diff_phase = ''
    while i <= len(ArrOx):
        if i % 50 == 0 and i > 0:
            MOKO.Report(f'Graph_{number}', 'set', 'table', sin_with_diff_phase)
            sin_with_diff_phase = ''
            number = number + 1

        if i < len(ArrOx):
            sin_with_diff_phase = sin_with_diff_phase + f'{i+1};{round(ArrOx[i],2)};{round(ArrOy[i],2)};'\
                                                      + f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};'\
                                                      + f'{i+1};{round(ArrOx2[i],2)};{round(ArrOy2[i],2)};' \
                                                      + '\\r'
        i = i + 1

MGPH.GraphInit()
MGPH.ClearGraph()

#Graph Settings
Value_OyOx = [-400,400,0,0.04]
Name_Oy = "Амплитуда"
Name_Ox = "Время"
Autoscale = "No"
MGPH.AddGraphSett(Value_OyOx, Name_Oy, Name_Ox, Autoscale)

#High Mask
name = "High Mask"
ArrOy = [300,300]
ArrOx = [0,0.05]
LineWidth = "3"
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#Low Mask
name = "Low Mask"
ArrOy = [-300,-300]
ArrOx = [0,0.05]
LineWidth = "3"
Color = "FFFF00" #Yellow
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#Average Mask
name = "Average Mask"
ArrOy = [0,0]
ArrOx = [0,0.05]
LineWidth = "3"
Color = "0" #Black
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx,LineWidth,Color,Visible)

#Region Status (статус)
#description: Frequency;(частота);Phase (фаза);Width (толщина);Color (цвет);Visible;(видимость)

#First Plot
MOKO.Program('tree', 'set', 'select = ' + 'Sinus with phase 90')

name = "Plot 1"  #hash Sinus with phase 90: 40;(40);90;3;Lime (лаймовый);Yes;(да)
MOKO.Report('Name1;Name4;Name7;Name10', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy = SinusGenerator(x,Ampl,freq,90)
ArrOx = list(x)
LineWidth = "3"
Color = "00FF00" #Lime
Visible = "Yes"
MGPH.AddLine(name, ArrOy, ArrOx,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

# Region Status (статус)

#Second Plot
MOKO.Program('tree', 'set', 'select = ' + 'Sinus with phase 0')

name = "Plot 2" #hash Sinus with phase 0: 40;(40);0;3;Aqua (аква);Yes;(да)
MOKO.Report('Name2;Name5;Name8;Name11', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy1 = SinusGenerator(x,Ampl,freq,0)
ArrOx1 = list(x)
LineWidth = "3"
Color = "00FFFF" #Aqua
Visible = "Yes"
MGPH.AddLine(name, ArrOy1, ArrOx1,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

# Region Status (статус)

#Third Plot
MOKO.Program('tree', 'set', 'select = ' + 'Sinus with phase -90')

name = "Plot 3"  #hash Sinus with phase -90: 40;(40);-90;3;Red (красный);Yes;(да)
MOKO.Report('Name3;Name6;Name9;Name12', 'set', 'strings', f'{name};{name};{name};{name}')
sampling_freq = 100
start = 0
stop = 0.05
x = np.arange(start,stop,stop/sampling_freq)
freq = 40
Ampl = 300
ArrOy2 = SinusGenerator(x,Ampl,freq,-90)
ArrOx2 = list(x)
LineWidth = "3"
Color = "FF0000" #Red
Visible = "Yes"
MGPH.AddLine(name, ArrOy2, ArrOx2,LineWidth,Color,Visible)

MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2)

MOKO.EndScript()