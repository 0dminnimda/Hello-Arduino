from pyfirmata import Arduino, util
from itertools import cycle
from time import sleep


class LED:
    def __init__(self, board, pin_number,
                 change_wait=0.05):
        self._pin = board.get_pin(f"d:{pin_number}:o")
        self._lighted = False
        self.change_wait = change_wait

    def get_lighted(self):
        return self._lighted

    lighted = property(get_lighted)

    def turn_on(self):
        if not self.lighted:
            self._lighted = True
            self._pin.write(1)
            sleep(self.change_wait)
            return True
        return False

    def turn_off(self):
        if self.lighted:
            self._lighted = False
            self._pin.write(0)
            sleep(self.change_wait)
            return True
        return False

    def switch_state(self):
        self._lighted = not self._lighted
        self._pin.write(self._lighted)
        sleep(self.change_wait)


board = Arduino('COM3')

print("Connected")

util.Iterator(board).start()

inp_pin = 2
out_pin = 7

digital_input = board.get_pin(f"d:{inp_pin}:i")
led = LED(board, out_pin, 0)


print("Running")

lighted = False

i = 0

while True:
    sw = digital_input.read()
    if sw is True:
        if led.turn_on():
            print("turned on", i)
    else:
        if led.turn_off():
            print("turned off", i)
            i += 1
