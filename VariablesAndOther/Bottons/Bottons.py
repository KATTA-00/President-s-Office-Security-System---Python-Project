###  import modules ###
from pyfirmata import INPUT, Arduino, util
from VariablesAndOther.VARIABLES import *
from time import sleep

############################################################################
'''  Module about Botton  '''


class Botton:
    """ class for Botton
    Methods :
            updateVAL()
            updateState()
            readStates()
    if botton is pressed >>>> state = PRESS
                 unpressed >>>> state = UNPRESS
    """

    def __init__(self, board, pin):
        """     initialize the Attributes   """
        self.board = board
        self.pin = pin
        self.state = UNPRESS
        self.VAL = False
        self.board.digital[self.pin].mode = INPUT
        self.updateVAL()

    def updateVAL(self):
        """ Method for read the input   """
        self.VAL = self.board.digital[self.pin].read()

    def updateState(self):
        """A method read the input and change the State"""
        self.updateVAL()
        if self.VAL == None:
            self.state = UNPRESS
        elif self.VAL:
            self.state = PRESS
        else:
            self.state = UNPRESS

    def readStates(self):
        """ Method for return the state of the botton"""
        return self.state


#####################################################################################

#####################################################################################
''' For Testing '''
if __name__ == "__main__":
    board = Arduino("COM3")
    digital_pin = 11
    it = util.Iterator(board)
    it.start()
    BOTTON = Botton(board, digital_pin)
    while True:
        BOTTON.updateState()
        print(BOTTON.state)
        sleep(SLEEP)
#####################################################################################
