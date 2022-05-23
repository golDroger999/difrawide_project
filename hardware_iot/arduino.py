import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyACM0')


start=0
end=0

trigpin = board.get_pin('d:7:o')
echopin= board.get_pin('d:8:i')

trigpin.write(0)
time.sleep(5)

while True:
    trigpin.write(1)
    time.sleep(3)
    trigpin.write(0)

    while echopin.write(0):
        pass
        start = time.time()
    while echopin.write(1):
        pass
        end = time.time()

    print((end - start)/58.0*1000000)
    time.sleep(1)