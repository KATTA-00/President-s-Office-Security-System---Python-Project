### import Moduels ###
from pyfirmata import Arduino, INPUT, util
from numpy import log
from VariablesAndOther.VARIABLES import *
from time import sleep

########################################################################
'''  Module about the Temperature sensor  '''


class Thermistor:
    """     class that used for Temperature sensor
    Methods :
            getVAL()
            getTemperature()
            checkTemperature()
    """

    def __init__(self, board, pin):
        """     initialize the Attributes   """
        self.board = board
        self.pin = pin
        self.TEMP = 0
        self.RIGTH_TEMP = True
        self.board.analog[self.pin].mode = INPUT
        self.board.analog[self.pin].enable_reporting()

        self.getVAL()
        self.getTemperature()

    def getVAL(self):
        """ Method for read the sensor value"""
        self.VAL = self.board.analog[self.pin].read()
        if self.VAL == None or self.VAL == 0:
            self.VAL = 0.0001
        elif self.VAL == 1:
            self.VAL = 0.9999

    def getTemperature(self):
        """ Method for calculate temperature value"""
        self.getVAL()
        VRT = 5.0 * self.VAL
        VR = VCC - VRT
        RT = VRT / (VR / R)
        ln = log(RT / RT0)
        TX = (1 / ((ln / B) + (1 / T0)))
        self.TEMP = round(TX - 273.15, 3)
        return self.TEMP  # return the temperature value

    def checkTemperature(self):
        """ Method for check the temperature value in the range """
        self.getTemperature()
        if TEMP_LIMITS[0] <= round(self.TEMP, 1) < TEMP_LIMITS[1]:
            self.RIGTH_TEMP = True
        else:
            self.RIGTH_TEMP = False


###########################################################################


##########################################################################
''' For Testing '''
if __name__ == "__main__":
    board = Arduino("COM3")
    pin = 0
    it = util.Iterator(board)
    it.start()
    Term = Thermistor(board, pin)
    while True:
        print(Term.getTemperature())
        sleep(SLEEP)
##########################################################################
