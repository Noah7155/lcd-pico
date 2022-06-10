import lcd
from utime import sleep

while True:
    lcd.clear()
    lcd.write('Lcd-pico demo!')
    sleep(2)
    lcd.clear()
    lcd.write('Made by Dragonflame7155')
    sleep(2)
    lcd.clear()
    lcd.write('Here are some of the avaliable characters')
    sleep(2)
    lcd.clear()
    lcd.write("az AZ 09 = . ? ([{}])")
    sleep(2)
    lcd.clear()
    lcd.write("These are symbols that can be used with dispchar()")
    sleep(2)
    lcd.clear()
    lcd.dispchar(htg)
    lcd.dispchar(dlr)
    lcd.dispchar(prc)
    lcd.dispchar(aps)
    lcd.dispchar(fsh)
    lcd.dispchar(bsh)
    sleep(2)
