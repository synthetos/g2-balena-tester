
# Example 1
#

from __future__ import print_function
import top_phat_button
import time
import sys

myButtons = top_phat_button.ToppHATButton()

def runExample():

    print("\nSparkFun Top pHAT Button  Example 1\n")

    if myButtons.is_connected() == False:
        print("The Top pHAT Button device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    myButtons.pressed_interrupt_enable = False
    myButtons.clicked_interrupt_enable = False

    while True:
        myButtons.button_pressed #These functions must be called to update button variables to their latest setting
        myButtons.button_clicked #These functions must be called to update button variables to their latest setting  
        if myButtons.a_pressed == True:
            print("A Pressed")
        if myButtons.a_clicked == True:
            print("A Released")
        if myButtons.b_pressed == True:
            print("B Pressed")
        if myButtons.b_clicked == True:
            print("B Released")
        if myButtons.up_pressed == True:
            print("Up Pressed")
        if myButtons.up_clicked == True:
            print("Up Released")
        if myButtons.down_pressed == True:
            print("Down Pressed")
        if myButtons.down_clicked == True:
            print("Down Released")
        if myButtons.left_pressed == True:
            print("Left Pressed")
        if myButtons.left_clicked == True:
            print("Left Released")
        if myButtons.right_pressed == True:
            print("Right Pressed")
        if myButtons.right_clicked == True:
            print("Right Released")
        if myButtons.center_pressed == True:
            print("Center Pressed")
        if myButtons.center_clicked == True:
            print("Center Released")

        time.sleep(.1)


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)

