from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit
from easyIO import *
import imu


# Startuję M5Stack core2 
imu0 = imu.IMU()

# Startuję ekran
screen = M5Screen()
# Czyszczę ekran
screen.clean_screen()
# Ustawiam kolor ekranu
screen.set_screen_bg_color(0xccFFFF)
# Ustawiam podświetlenie ekranu na 40%
screen.set_screen_brightness(40)
# Podłączam się do czujnika Temperatury/Wilgotności/Ciśnienia
env3_0 = unit.get(unit.ENV3, unit.PORTC)
# Podłączam czujnik odległości
sonic_io_0 = unit.get(unit.SONIC_IO, unit.PORTB)
# Projektuję wyglad ekranu
# mnoznik dla temperatury = 6
# temperatura Etykiety
temp = M5Label('temp', x=8, y=21, color=0xff0000, font=FONT_MONT_14, parent=None)
temp0c = M5Label('0', x=0, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp5c = M5Label('5', x=31, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp10c = M5Label('10', x=61, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp15c = M5Label('15', x=91, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp20c = M5Label('20', x=121, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp25c = M5Label('25', x=151, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp30c = M5Label('30', x=181, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp35c = M5Label('35', x=211, y=0, color=0x000, font=FONT_MONT_10, parent=None)
temp40c = M5Label('40C', x=241, y=0, color=0x000, font=FONT_MONT_10, parent=None)
# Temperatura linie
templine = M5Line(x1=10, y1=20, x2=100, y2=20, color=0x000, width=1, parent=None)
# templine = M5Bar(x=10, y=20, w=240, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0xff0000, parent=None)
templine.set_color(0xff0000)
templine.set_line_width(2)
# Temperatyra linie 0-40C
templine0 = M5Line(x1=0, y1=0, x2=0, y2=20, color=0x000, width=1, parent=None)
templine5 = M5Line(x1=30, y1=0, x2=30, y2=10, color=0x000, width=1, parent=None)
templine10 = M5Line(x1=60, y1=0, x2=60, y2=20, color=0x000, width=1, parent=None)
templine15 = M5Line(x1=90, y1=0, x2=90, y2=10, color=0x000, width=1, parent=None)
templine20 = M5Line(x1=120, y1=0, x2=120, y2=20, color=0x000, width=1, parent=None)
templine25 = M5Line(x1=150, y1=0, x2=150, y2=10, color=0x000, width=1, parent=None)
templine30 = M5Line(x1=180, y1=0, x2=180, y2=20, color=0x000, width=1, parent=None)
templine35 = M5Line(x1=210, y1=0, x2=210, y2=10, color=0x000, width=1, parent=None)
templine40 = M5Line(x1=240, y1=0, x2=240, y2=20, color=0x000, width=1, parent=None)

# xxxx = M5Line(x1=2, y1=120, x2=72, y2=120, color=0x000, width=1, parent=None)


# ćisnienie
pres = M5Label('pres', x=8, y=105, color=0x000, font=FONT_MONT_14, parent=None)
pres0 = M5Label('940hPa', x=2, y=80, color=0x000, font=FONT_MONT_10, parent=None)
pres50 = M5Label('1000hPa', x=122, y=80, color=0x000, font=FONT_MONT_10, parent=None)
pres100 = M5Label('1060hPa', x=242, y=80, color=0x000, font=FONT_MONT_10, parent=None)

#linie ciśnienia
presline = M5Line(x1=20, y1=60, x2=200, y2=60, color=0x000, width=1, parent=None)
presline.set_color(0x0B8924)
presline.set_line_width(2)
presline0 = M5Line(x1=0, y1=40, x2=0, y2=100, color=0x000, width=1, parent=None)
presline50 = M5Line(x1=120, y1=80, x2=120, y2=100, color=0x000, width=1, parent=None)
presline100 = M5Line(x1=240, y1=100, x2=240, y2=100, color=0x000, width=1, parent=None)

# wilgotnosc
humi = M5Label('humi', x=8, y=63, color=0x8097F5, font=FONT_MONT_14, parent=None)
humi0 = M5Label('0%', x=2, y=40, color=0x000, font=FONT_MONT_10, parent=None)
humi25 = M5Label('25%', x=62, y=40, color=0x000, font=FONT_MONT_10, parent=None)
humi50 = M5Label('50%', x=122, y=40, color=0x000, font=FONT_MONT_10, parent=None)
humi25 = M5Label('75%', x=182, y=40, color=0x000, font=FONT_MONT_10, parent=None)

humi100 = M5Label('100%', x=242, y=40, color=0x000, font=FONT_MONT_10, parent=None)



# linie wilgotności
humiline = M5Line(x1=20, y1=60, x2=200, y2=60, color=0x000, width=1, parent=None)
humiline.set_color(0x8097F5)
humiline.set_line_width(2)
humiline0 = M5Line(x1=0, y1=40, x2=0, y2=60, color=0x000, width=1, parent=None)
humiline25 = M5Line(x1=60, y1=40, x2=60, y2=50, color=0x000, width=1, parent=None)
humiline50 = M5Line(x1=120, y1=40, x2=120, y2=60, color=0x000, width=1, parent=None)
humiline75 = M5Line(x1=180, y1=40, x2=180, y2=50, color=0x000, width=1, parent=None)
humiline100 = M5Line(x1=240, y1=40, x2=240, y2=60, color=0x000, width=1, parent=None)

# bateria
# bateria = M5Bar(x=40, y=11, w=240, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0xff0000, parent=None)
bateria = M5Label('bateria', x=68, y=193, color=0x000, font=FONT_MONT_14, parent=None)


# Ramka
ramkadol = M5Line(x1=0, y1=120, x2=240, y2=120, color=0x7BF4C8, width=1, parent=None)
ramkaprawa = M5Line(x1=240, y1=0, x2=240, y2=120, color=0x7BF4C8, width=1, parent=None)
ramkaod1 = M5Line(x1=0, y1=40, x2=240, y2=40, color=0x7BF4C8, width=1, parent=None)
ramkaod2 = M5Line(x1=0, y1=80, x2=240, y2=80, color=0x7BF4C8, width=1, parent=None)


# polozenie
label0 = M5Label('label0', x=133, y=199, color=0x000, font=FONT_MONT_14, parent=None)


# Odlegosc

label1 = M5Label('label0', x=233, y=199, color=0x000, font=FONT_MONT_14, parent=None)


# label1.set_text(str(sonic_io_0.get_distance(1)))


# Funkcja podswietlenie ekranu 100% na 60 sekund
def buttonA_wasPressed():
  # global params
  screen.set_screen_brightness(100)
  wait(60)
  screen.set_screen_brightness(10)
  pass
btnA.wasPressed(buttonA_wasPressed)


# Pętla - odświezam co 1 sek
while True:
  # Temperatura 
  temp.set_text(str(round(env3_0.temperature,1)))
  # Wilgotność
  humi.set_text(str(round(env3_0.humidity,1)))
  # Ciśnienie
  pres.set_text(str(round(env3_0.pressure/100,1)))

  # Linia temperatury
  templine.set_points(0, 20, int((6 * (env3_0.temperature))), 20)
  # Linia wilgotności
  humiline.set_points(0, 60, int((2.4 * (env3_0.humidity))), 60)
  # Linia ciśnienia
  presline.set_points(0, 100, int((((env3_0.pressure/100)*100)/1060)), 100)
#   bateria.set_size((map_value((power.getBatVoltage()), 3.7, 4.1, 0, 100)), 12)
  label0.set_text(str(imu0.ypr[1]))
  bateria.set_text(str(map_value((power.getBatVoltage()), 3.7, 4.1, 0, 100)))
 
  wait(1)
  