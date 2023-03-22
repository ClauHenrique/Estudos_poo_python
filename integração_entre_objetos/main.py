from clock.CockDisplay import ClockDisplay
import time

# my_display = ClockDisplay()
my_display = ClockDisplay(9, 58, 40)

while True:
    time.sleep(1)
    my_display.timeTick()
    print(my_display.getTime())
