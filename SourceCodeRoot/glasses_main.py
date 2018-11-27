import board
import neopixel
px = neopixel.NeoPixel(board.SCL, 32, brightness  =0.2, auto_write = True)
pix_on = (100, 100, 100)
pix_off = (0, 0, 0)
while True:
    px[0]=pix_on
    for i in range(15):
        px[i] = pix_off
        px[i+1] = pix_on
    px[15]=pix_off
    px[23]=pix_on
    for i in range(7):
        px[23-i] = pix_off
        px[22-i] = pix_on
    px[16]=pix_off
    px[31]=pix_on
    for i in range(7):
        px[31-i] = pix_off
        px[30-i] = pix_on
    px[24]=pix_off