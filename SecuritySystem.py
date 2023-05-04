"""************************************************************
***************************************************************
        PRESIDENT'S OFFICE - Security System
***************************************************************
***************************************************************
    GROUP - 7.B
                By :
                    E/19/129
                    E/19/151
                    E/19/156
                    E/19/166
GP106 - COMPUTING / Faculty Of Engineering / University Of Peradeniya
***************************************************************
***************************************************************
***************************************************************
***************************************************************
"""

################ IMPORTING MODULES ##########################
try:
    import pyfirmata
    import numpy
except:
    import pip

    pip.main(['install', 'pyfirmata', 'numpy'])
from pyfirmata import Arduino, util
from time import sleep
from PresidentOffice.PresidentOffice import PresidentOffice
from Door.SecretKnock import DoorLock
from TemperatureSensor.Thermostor import Thermistor
from PanicBotton.Panic import PanicBotton
from VariablesAndOther.Leds.Leds import Led, LedRun
from VariablesAndOther.Buzzers.Buzzers import Buzzer
from VariablesAndOther.Bottons.Bottons import Botton
from VariablesAndOther.VARIABLES import *


############################################################


def main():
    """      Main Function       """

    ################### Creating a Board ######################
    BOARD = Arduino("COM3")
    it = util.Iterator(BOARD)
    it.start()

    ################### Creating Door Lock ########################
    LOCK = DoorLock(BOARD, DOORLOCK_PIN)
    ################## Creating Thermistor ######################
    THERM = Thermistor(BOARD, THERMISTOR_PIN)
    ################# Creating Panic Botton ####################
    PANIC = PanicBotton(BOARD, PANIC_PIN)

    ################# Initializing the LEDs #####################
    LED_KNOCK = Led(BOARD, LED_KNOCK_PIN)
    LED_LOCKDOWN = Led(BOARD, LED_LOCKDOWN_PIN)
    LEDs = [LED_KNOCK, LED_LOCKDOWN]
    ################# Initializing the Buzzer #####################
    BUZ_TEMP = Buzzer(BOARD, BUZ_TEMP_PIN)
    ################# Initializing the UNLOCK Bottons #####################
    UNLOCK_BOTTON = Botton(BOARD, UNLOCK_BOTTON_PIN)
    UNLOCKDOWN = Botton(BOARD, UNLOCKDOWN_PIN)

    ################### Creating President Office ###########################
    PRESIDENT = PresidentOffice((LOCK, LED_KNOCK, UNLOCK_BOTTON), (THERM, BUZ_TEMP), PANIC, (LED_LOCKDOWN, UNLOCKDOWN))

    '''     MAIN LOOP       '''
    while True:
        # Calling KnockLogic() Method of PRESIDENT Object
        Knock_msg = PRESIDENT.KnockLogic()
        # Calling ThermistorLogic() Method of PRESIDENT Object
        Thermistor_msg = PRESIDENT.ThermistorLogic()
        # Calling PanicLogic() Method of PRESIDENT Object
        Panic_msg = PRESIDENT.PanicLogic()
        # Calling Lockdown() Method of PRESIDENT Object
        Lockdown_msg = PRESIDENT.Lockdown()

        main_string_list = [Lockdown_msg, Panic_msg, Knock_msg, Thermistor_msg, str(THERM.TEMP)]
        main_string = ','.join(main_string_list)
        print(main_string)

        # RUN the Buzzer
        BUZ_TEMP.RUN()
        # RUN LEDs
        LedRun(LEDs)
        # SLEEP the MAIN LOOP
        sleep(SLEEP)


########################################################################################################################


"""#######################################################################
###########################  RUN the main function  #####################
##########################################################################"""
if __name__ == "__main__":
    # Calling the main() function
    main()
"""*************************************************************************"""
