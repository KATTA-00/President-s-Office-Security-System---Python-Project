'''  President office '''
from VariablesAndOther.VARIABLES import *


###############################################################3333

class PresidentOffice:

    def __init__(self, lock, therm, panic, unlock):
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
        if self.LOCK.LOCK:
            if self.Flag:
                self.LOCKDOWN = True
                self.Flag = False
            self.LOCKLED.blink()
            self.LOCKBOTTON.updateState()
            if self.LOCKBOTTON.state == PRESS and not self.LOCKDOWN:
                self.Flag = True
                self.LOCKLED.onLed()
                self.LOCK.liftLock()
            print("LOCKED")
        elif self.LOCK.PASSED:
            print("PASSED")
            self.LOCKLED.blink(BLINK_3)
        elif self.LOCK.RESET:
            print("RESET")
            self.LOCKLED.blink(BLINK_1)
        elif self.LOCK.STARTED_CHANCE:
            print("ACTIVE")
            self.LOCKLED.offLed()
        else:
            print("DIACTIVE")
            self.LOCKLED.onLed()
        self.LOCK.Setup()

    def PanicLogic(self):
        self.PANIC.checkEmergency()
        if self.PANIC.EMERGENCY:
            self.LOCKDOWN = True

    def ThermistorLagic(self):
        self.THERM.checkTemperature()
        if self.THERM.GOODTEMP:
            self.THERMBUZZ.offBuzzer()
        else:
            self.THERMBUZZ.onBuzzer()

    def Lockdown(self):
        if self.LOCKDOWN:
            self.LOCKDOWN_LED.blink()
            self.UNLOCKDOWNBOTTON.updateState()
            if self.UNLOCKDOWNBOTTON.state == PRESS:
                self.PANIC.resetBotton()
                self.LOCKDOWN = False
                self.LOCKDOWN_LED.offLed()
