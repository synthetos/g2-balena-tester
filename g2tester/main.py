#from pygame import *
from utils import *
from time import sleep
import board
import neopixel

def setup_leds():
    # Create the class object
    pixels = neopixel.NeoPixel(board.D12, 6, auto_write=False)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    DARK_VIOLET = (153,0, 230)
    YELLOW = (255,255,25)
    WHITE = (255, 255, 255 )

    # Set Pixel Configuration
    pixels[0] = RED
    pixels[1] = GREEN
    pixels[2] = BLUE
    pixels[3] = DARK_VIOLET
    pixels[4] = YELLOW
    pixels[5] = WHITE
    

    # Display Configuration
    pixels.show()


if __name__ == "__main__":

    setup_leds()
    print_c("[#]Starting G2 Tester Script")
    count = 0
    while(1):
        sleep(1)
        print_c(f"-- Simulating Working... #[{count}]")
        count = count + 1
    print_r('\tExiting...')

