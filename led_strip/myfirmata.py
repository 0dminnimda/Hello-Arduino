import inspect
from typing import Any, Callable, Type, TypeAlias

import pyfirmata as pfm
import serial
from serial.tools.list_ports import comports as list_comports


# DIGITAL = "d"
# ANALOG = "a"

# INPUT = "i"
# OUTPUT = "o"
# PWM = "p"
# SERVO = "s"


if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec  # type: ignore[attr-defined]


PinValueType: TypeAlias = bool | int | float


# _old_Pin_write = pfm.Pin.write


# def _Pin_write(self: pfm.Pin, value: PinValueType) -> None:
#     if self.value != value:
#         _old_Pin_write(self, value)


# pfm.Pin.write = _Pin_write


class AttrPin:
    def __init__(self, pin: pfm.Pin) -> None:
        self.pin = pin

    def __get__(self, obj: Any, tp: Any = None) -> PinValueType:
        return self.pin.read()  # type: ignore

    def __set__(self, obj: Any, value: PinValueType) -> None:
        self.pin.write(value)


def setup_board(board: pfm.Board) -> pfm.Board:
    pfm.util.Iterator(board).start()
    return board


def setup_pin(pin: pfm.Pin, mode: int = pfm.ANALOG) -> pfm.Pin:
    if getattr(pin, "mode", None) == pfm.UNAVAILABLE:
        raise pfm.InvalidPinDefError(f"Invalid pin definition: {pin} is UNAVAILABLE")

    if pin.type is pfm.DIGITAL:
        if mode == pfm.PWM:
            pin.mode = pfm.PWM
        elif mode == pfm.SERVO:
            pin.mode = pfm.SERVO
        elif mode == pfm.OUTPUT:
            pin.mode = pfm.OUTPUT
        else:
            pin.mode = pfm.INPUT
    elif pin.type is pfm.ANALOG:
        pin.enable_reporting()

    return pin


def get_the_board(board_factory: Callable[[str], pfm.Board] = pfm.Arduino) -> pfm.Board:
    hit = False
    board = None

    for port in list_comports():
        try:
            board = board_factory(port[0])
        except serial.SerialException:
            continue

        if hit:
            raise IOError("More than one board found!")
        hit = True

    if board is None:
        raise IOError("No boards found")
    return board
