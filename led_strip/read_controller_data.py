from time import sleep

from myfirmata import get_the_board, setup_board, setup_pin
from pyfirmata import Arduino, INPUT, OUTPUT, Board


class LED:
    def __init__(self, board: Board, pin_number: int, flip_delay: float = 0.05):
        self.pin = setup_pin(board.digital[pin_number], OUTPUT)
        self.flip_delay = flip_delay

    def turn_on(self) -> bool:
        return self.turn(1)

    def turn_off(self) -> bool:
        return self.turn(0)

    def turn(self, value: bool | int) -> bool:
        value = bool(value)
        if value == self.pin.value:
            return False
        self.pin.write(value)
        sleep(self.flip_delay)
        return True

    def flip(self) -> None:
        self.pin.write(not self.pin.value)
        sleep(self.flip_delay)


board = setup_board(get_the_board(Arduino))

print("Connected")

# inputs = [setup_pin(board.analog[i], INPUT) for i in range(6)]
# inputs += [setup_pin(board.digital[i], INPUT) for i in range(2, 14)]
# inputs = [board.get_pin(["a", i, "i"]) for i in range(6)]
# inputs += [board.get_pin(["d", i, "i"]) for i in range(2, 14)]
# leds = [LED(board, i) for i in range(2, 14)]

led = LED(board, 13, 0)

print("Running")

while True:
    led.turn(1)
    sleep(0.5)
    led.turn(0)
    sleep(0.5)
