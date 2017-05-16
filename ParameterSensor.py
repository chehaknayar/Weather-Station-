import json
import Adafruit_CharLCD as LCD
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
import time

lcd_rs=25,  lcd_en=24, lcd_d4=23, lcd_d5=17, lcd_d6=18, lcd_d7=22, lcd_backlight=4, lcd_columns=16 , lcd_rows=2

lcd=LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)

sensor = BMP085.BMP085()

now = datetime.now()
day=now.strftime("%A")
month=now.strftime('%B')
temp=float(sensor.read_temperature())
pressure=float(sensor.read_pressure())
alt=float(sensor.read_altitude())
slp=float(sensor.read_sealevel_pressure())

sensorr = {}      
sensorr['today'] = {}
sensorr['today']['date']=[]

sensorr['today']['date'].append({ 'day': day, 'month': now.month, 'monthname': month, 'pressure': pressure, 'temperature': temp, 'altitude':alt, 'sealevelpressure':slp})
with open('data.txt', 'w') as outfile:
	json.dump(sensorr, outfile)
with open('data.txt') as json_file:
	data = json.load(json_file) for p in data['today']['date']:
		lcd.message(str(datetime.now()))        	lcd.message(str('\nTemp = {0:0.2f} *C'.format(p['temperature'])))
    time.sleep(5)       	lcd.message(str('\n'))        	lcd.message(str(datetime.now()))
    lcd.message(str('\nPress={0:0.2f}Pa'.format(p['pressure'])))
    time.sleep(5)
    lcd.message(str('\n'))
    lcd.message(str(datetime.now()))
    lcd.message(str('\nAltitude={0:0.2f}m'.format(p['altitude'])))
    time.sleep(5)
    lcd.message(str('\n'))
    lcd.message(str(datetime.now()))
    lcd.message(str('\nSLP.={0:0.2f} Pa'.format(p['sealevelpressure'])))
    

