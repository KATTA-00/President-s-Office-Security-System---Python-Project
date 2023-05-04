### IMPORTING MODULES ###
from pyfirmata import Arduino, util
from time import sleep
from PresidentOffice import PresidentOffice
from Door.SecretKnock import DoorLock
from TemperatureSensor.Thermostor import Thermistor
from PanicBotton.Panic import PanicBotton
from VariablesAndOther.Leds.Leds import Led,LedRun
from VariablesAndOther.Buzzers.Buzzers import Buzzer
from VariablesAndOther.Bottons.Bottons import Botton
from VariablesAndOther.VARIABLES import *


################### Creating a Board ######################
BOARD = Arduino("COM3")
it = util.Iterator(BOARD)
it.start()

################### Creating Door Lock ########################
LOCK = DoorLock(BOARD, DOORLOCK_PIN)
################## Creating Thermistor ######################
THERM = Thermistor(BOARD, THERMISTOR_PIN)
################# Creating Panic Botton ####################
PANIC = PanicBotton(BOARD,PANIC_PIN)

################# Initializing the LEDs #####################
LED_KNOCK = Led(BOARD, LED_KNOCK_PIN)
LED_LOCKDOWN = Led(BOARD, LED_PANIC_PIN)
LEDs = [LED_KNOCK, LED_LOCKDOWN]
################# Initializing the Buzzer #####################
BUZ_TEMP = Buzzer(BOARD, BUZ_TEMP_PIN)
################# Initializing the UNLOCK Bottons #####################
UNLOCK_BOTTON = Botton(BOARD,UNLOCK_BOTTON_PIN)
UNLOCKDOWN = Botton(BOARD, UNLOCKDOWN_PIN)



PRESIDENT = PresidentOffice((LOCK,LED_KNOCK,UNLOCK_BOTTON), (THERM,BUZ_TEMP), PANIC, (LED_LOCKDOWN,UNLOCKDOWN))

''' MAIN LOOP '''
while True:
    PRESIDENT.KnockLogic()
    PRESIDENT.ThermistorLagic()
    PRESIDENT.PanicLogic()
    PRESIDENT.Lockdown()


    BUZ_TEMP.RUN()
    LedRun(LEDs)
    sleep(SLEEP)
