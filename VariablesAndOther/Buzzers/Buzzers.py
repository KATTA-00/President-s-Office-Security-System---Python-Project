### import modules ###
from pyfirmata import OUTPUT, Arduino, util
from time import sleep, time
from VariablesAndOther.VARIABLES import *

###############################################################
'''  Module for Buzzer  '''


class Buzzer:
    """     class for Buzzer
    Methods :
            onBuzzer()
            offBuzzer()
            RUN()
    """

    def __init__(self, board, pin):
        """     initialize the Attributes   """
        self.board = board
        self.pin = pin
        self.ON, self.OFF = False, False
        self.board.digital[self.pin].mode = OUTPUT

    def onBuzzer(self):
        """ Method to on the buzzer """
        self.ON = True
        self.OFF = False

    def offBuzzer(self):
        """ Method to off the buzzer """
        self.OFF = True
        self.ON = False

    def RUN(self):
        """ Method for run the buzzer """
        if self.ON:
            self.board.digital[self.pin].write(1)
        else:
            self.board.digital[self.pin].write(0)


##########################################################################

##########################################################################
''' For Testing '''
if __name__ == "__main__":
    board = Arduino("COM3")
    digital_pin = 6
    it = util.Iterator(board)
    it.start()
    Buz = Buzzer(board, digital_pin)
    Buz.onBuzzer()
    while True:
        Buz.RUN()
        sleep(SLEEP)
##########################################################################
