from pyfirmata import Arduino, util
from time import sleep


board = Arduino('COM5')

print("Connected")

util.Iterator(board).start()

r = board.get_pin("d:11:p")
g = board.get_pin("d:10:p")
b = board.get_pin("d:9:p")

r.write(0)
g.write(0)
b.write(0)


def torange(stop):
    if stop > 0:
        for i in range(0, stop + 1):
            yield i / stop
    elif stop < 0:
        for i in range(stop, 1):
            yield i / stop


total = 2000


while True:
    for i in torange(total):
        r.write(i)
    for i in torange(total):
        g.write(i)
    for i in torange(total):
        b.write(i)

    for i in torange(-total):
        r.write(i)
    for i in torange(-total):
        g.write(i)
    for i in torange(-total):
        b.write(i)


r.write(0)
g.write(0)
b.write(0)
breakpoint()
