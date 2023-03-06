# lists of conversion functions
def convertToSelf(value):
  return value

def convertCelsiusToKelvin(celsius):
  return celsius + 273.15, 2

def convertCelsiusToFahrenheit(celsius):
  return celsius * 9 / 5 + 32

def convertFahrenheitToCelsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

def convertFahrenheitToKelvin(fahrenheit):
  return (fahrenheit + 459.67) * 5 / 9

def convertKelvinToCelsius(kelvin):
  return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
  return kelvin * 9 / 5 - 459.67

def convertMileToMeter(mile):
  return mile * 1609.344

def convertMileToYard(mile):
  return mile * 1760

def convertMeterToMile(meter):
  return meter / 1609.344

def convertMeterToYard(meter):
  return meter * 1.09361


def convertYardToMeter(yard):
  return yard / 1.09361


def convertYardToMile(yard):
  return yard / 1760

# Error class
class ConversionNotPossible(ValueError):
    pass

# A dictionary to store the corresponding conversion
conversion = {
  'celsius': {
    'celsius': convertToSelf,
    'kelvin': convertCelsiusToKelvin,
    'fahrenheit': convertCelsiusToFahrenheit
  },
  'kelvin': {
    'kelvin': convertToSelf,
    'celsius': convertKelvinToCelsius,
    'fahrenheit': convertKelvinToFahrenheit
  },
  'fahrenheit': {
    'fahrenheit': convertToSelf,
    'celsius': convertFahrenheitToCelsius,
    'kelvin': convertFahrenheitToKelvin
  },
  'mile': {
    'mile': convertToSelf,
    'meter': convertMileToMeter,
    'yard': convertMileToYard
  },
  'meter': {
    'meter': convertToSelf,
    'mile': convertMeterToMile,
    'yard': convertMeterToYard
  },
  'yard': {
    'yard': convertToSelf,
    'mile': convertYardToMile,
    'meter': convertYardToMeter
  }
}

# convert any unit to another unit
def convert(fromUnit, toUnit, value):
  """
    fromUnit - the unit we are converting from, as a string
    toUnit - the unit we are converting to, as a string
    value - the value of fromUnit we are converting from
  """
  if not (type(fromUnit) == str and type(toUnit) == str and (type(value) == int or type(value) ==float)): 
    raise ConversionNotPossible('Invalid input. fromUnit and toUnit should be strings, value should be number')
  if not ((fromUnit in conversion) and (toUnit in conversion[fromUnit])):
    raise ConversionNotPossible('Invalid units. Please input the following units: celsius, fahrenheit, kelvin only for Temperature conversion. Mile, meter, yard only for Distance conversion.')
  else:
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    result = round(conversion[fromUnit][toUnit](value), 2)
    print(result)
