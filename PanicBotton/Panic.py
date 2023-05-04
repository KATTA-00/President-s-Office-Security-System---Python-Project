### import modules ###
from VariablesAndOther.Bottons.Bottons import Botton
from VariablesAndOther.VARIABLES import *

#################################################################################
'''  Module for Panic Botton  '''


class PanicBotton:
    """     class that used fot Panic Botton
    Methods :
            checkEmergency()
            resetBotton()
    """

    def __init__(self, board, pin):
        """     initialize the Attributes   """
        self.board = board
        self.pin = pin
        self.botton = Botton(self.board, self.pin)
        self.resetBotton()

    def checkEmergency(self):
        """ Method for check botton is pressed  """
        self.botton.updateState()
        if not self.EMERGENCY:
            if self.botton.state == PRESS:
                self.EMERGENCY = True
            else:
                self.EMERGENCY = False

    def resetBotton(self):
        """ Method for reset the botton """
        self.EMERGENCY = False
##################################################################################
