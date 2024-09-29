import OPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
GPIO.setboard(4) # Orange Pi One
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

# read data using pin 7
instance = dht22.DHT22(pin=7)

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))

			print("Temperature: %-3.1f C" % result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)

		time.sleep(5)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()