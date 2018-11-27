import board
import busio
from adafruit_ht16k33 import matrix
import bitmapfont
import time

i2c = busio.I2C(board.SCL, board.SDA)
mx = matrix.Matrix8x8(i2c, auto_write=False)
bf = bitmapfont.BitmapFont(8, 8, mx.pixel)

mx.fill(0)
mx.show()
bf.init()

while True:
    for i in range(15, -30, -1):
        mx.fill(0)
        bf.text('IKEA', i, 0, 100)
        mx.show()
        time.sleep(0.025)