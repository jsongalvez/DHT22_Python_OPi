# DHT22 Python library

This simple class can be used for reading temperature and humidity values from DHT22 sensor on Raspberry Pi.

Original Source Code: https://github.com/szazo/DHT11_Python
DHT22 Source Code: https://github.com/MineAP/DHT22_Python

# Usage

1. Instantiate the `DHT22` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT22Result` object with actual values and error code.

For example:

```python
import OPi.GPIO as GPIO
import dht22

# initialize GPIO
GPIO.setboard(4) # Orange Pi One
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

# read data using pin 7
instance = dht22.DHT22(pin=7)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `dht22_example.py` (you probably need to adjust pin for your configuration)


# License

This project is licensed under the terms of the MIT license.
