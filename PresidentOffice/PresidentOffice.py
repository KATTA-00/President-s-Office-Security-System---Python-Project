'''#######################################################################
##################  President office    ##################################
##########################################################################
 '''

### import modules ###
from VariablesAndOther.VARIABLES import *


###############################################################3333

class PresidentOffice:
    """ The class of President office - Containing LOCK, PANIC BOTTON and THERMISTOR
    Methods :
        KnockLogic()
        PanicLogic()
        ThermistorLogic()
        Lockdown()
    """

    def __init__(self, lock, therm, panic, unlock):
        """ Initialize the instancese"""
        self.LOCK = lock[0]
        self.LOCKLED = lock[1]
        self.LOCKBOTTON = lock[2]
        self.THERM = therm[0]
        self.THERMBUZZ = therm[1]
        self.PANIC = panic
        self.LOCKDOWN_LED = unlock[0]
        self.UNLOCKDOWNBOTTON = unlock[1]
        self.LOCKDOWN = False
        self.Flag = True

    def KnockLogic(self):
        """Logic for the DOOR LOCK"""
        if self.LOCK.LOCK:  # if LOCK is LOCKED
            if self.Flag:
                self.LOCKDOWN = True
                self.Flag = False
            self.LOCKLED.blink()
            self.LOCKBOTTON.updateState()
            string = "DOOR LOCKED"
            if self.LOCKBOTTON.state == PRESS and not self.LOCKDOWN:  # if LOCK is UNLOCKED
                self.Flag = True
                self.LOCKLED.onLed()
                self.LOCK.liftLock()
        elif self.LOCK.PASSED:  # if LOCK is PASSED
            self.LOCKLED.blink(BLINK_3)
            string = "DOOR PASSED"
        elif self.LOCK.RESET:  # if LOCK is RESET
            self.LOCKLED.blink(BLINK_1)
            string = "DOOR RESET"
        elif self.LOCK.STARTED_CHANCE:  # if a chance started
            self.LOCKLED.offLed()
            string = "Started a Chance"
        else:  # if not started a chance
            self.LOCKLED.onLed()
            string = "Knock is Active"

        self.LOCK.Setup()  # Run the Setup() method of LOCK

        return string

    def PanicLogic(self):
        """Logic for Panic Botton"""
        self.PANIC.checkEmergency()  # check Panic Botton
        if self.PANIC.EMERGENCY and not self.LOCKDOWN:
            self.LOCKDOWN = True  # if the Botton pressed
            self.LOCK.lockDoor()    # if the botton pressed lock the door
            return "Panic Botton is pressed"
        elif self.LOCKDOWN:
            return "LOCKDOWN"
        else:
            return "Panic Botton is not pressed"

    def ThermistorLogic(self):
        """Logic for Thermistor Sensor"""
        self.THERM.checkTemperature()  # check Temperature Sensor
        if self.THERM.RIGTH_TEMP:
            self.THERMBUZZ.offBuzzer()  # if the temperature is in range
            return "Good Temperature"
        else:
            self.THERMBUZZ.onBuzzer()  # else on the buzzer
            return "Bad Temperature"

    def Lockdown(self):
        """Method to handle the LOCKDOWN """
        if self.LOCKDOWN:
            self.LOCKDOWN_LED.blink()
            self.UNLOCKDOWNBOTTON.updateState()
            string = "LOCKDOWN"
            if self.UNLOCKDOWNBOTTON.state == PRESS:
                self.PANIC.resetBotton()
                self.LOCKDOWN = False
                self.LOCKDOWN_LED.offLed()
        else:
            string = "System Safe"
        return string
#########################################################################################
