import gpiod, serial_asyncio
import time

class Gpio():
    def __init__(self):

        self.chip=gpiod.Chip('gpiochip0')
        self.line = gpiod.find_line("PA17")
        self.lines = self.chip.get_lines([self.line.offset()])
        self.lines.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

    def start_trasmission(self):
        while True:
            self.lines.set_values([1])
            time.sleep(1)
            self.lines.set_values([0])
            time.sleep(1)

if __name__=="__main__":
    gpioObject=Gpio()
    gpioObject.start_trasmission()