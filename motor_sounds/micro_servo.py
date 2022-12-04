from pyfirmata import Arduino, util

board = Arduino('COM5')

print("Connected")

util.Iterator(board).start()

servo = board.get_pin('d:9:s')

servo.write(0)
