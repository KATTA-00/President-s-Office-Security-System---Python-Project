### import modules ###
from pyfirmata import OUTPUT, Arduino, util
from time import sleep, time
from VariablesAndOther.VARIABLES import *

###############################################################
'''  Mudule about LED  '''


# Function for RUN the LEDs
def LedRun(arr):
    for i in arr:
        i.RUN()


###################################################################
class Led:
    """     class for LED
    Methods :
            onLed()
            offLed()
            blink()
            RUN()
    """

    def __init__(self, board, pin):
        """     initialize the Attributes   """
        self.board = board
        self.pin = pin
        self.ON, self.OFF, self.BLINK, self.Flag = False, False, False, False
        self.TIME, self.blinkCount, self.COUNT, self.BLINKING = 0, 0, 0, 0
        self.board.digital[self.pin].mode = OUTPUT

    def onLed(self):
        """ Method to on the led """
        if self.COUNT == -1:
            self.ON = True
            self.OFF = False
            self.BLINK = False
            self.BLINKING = 0
            self.blinkCount = 0
        elif time() - self.BLINKING > 2 * DELAY_BLINK * self.COUNT:
            self.ON = True
            self.OFF = False
            self.BLINK = False
            self.BLINKING = 0

    def offLed(self):
        """ Method to off the led """
        if self.COUNT == -1:
            self.ON = False
            self.OFF = True
            self.BLINK = False
            self.BLINKING = 0
            self.blinkCount = 0
        elif time() - self.BLINKING > 2 * DELAY_BLINK * self.COUNT:
            self.OFF = True
            self.ON = False
            self.BLINK = False
            self.BLINKING = 0

    def blink(self, count=-1):
        """ Method to blink the led """
        self.COUNT = count
        self.BLINK = True
        self.ON = False
        self.OFF = False

    def RUN(self):
        """ Method to run the led """
        if self.ON:
            self.board.digital[self.pin].write(1)
        elif self.BLINK:
            if self.blinkCount == 0:
                self.BLINKING = time()
                self.TIME = time()
                self.blinkCount += 1
            if time() - self.TIME <= DELAY_BLINK:
                self.board.digital[self.pin].write(1)
                if not self.Flag:
                    self.blinkCount += 1
                    self.Flag = True
            elif time() - self.TIME <= 2 * DELAY_BLINK:
                self.board.digital[self.pin].write(0)
            else:
                self.TIME = time()
                self.Flag = False
                if self.blinkCount >= self.COUNT - 1:
                    self.blinkCount = 0
                    if self.COUNT != -1:
                        self.offLed()
                        self.BLINK = False
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
    LED1 = Led(board, digital_pin)
    LED1.onLed()
    while True:
        LED1.RUN()
        sleep(SLEEP)
##########################################################################
