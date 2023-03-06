import unittest
import conversions

c_to_k_examples =  ((0, 273.15),
                    (-273.15, 0),
                    (100, 373.15),
                    (-50.93, 222.22),
                    (72.34, 345.49))

c_to_f_examples = ((0, 32.00),
                           (-17.78, 0),
                           (100, 212),
                           (-88.31, -126.96),
                           (-273.15, -459.67))

f_to_k_examples = ((32, 273.15),
                   (-459.67, 0),
                   (0, 255.37),
                   (100.08, 310.97),
                   (-50.32,227.42))

class CelsiusToKelvin(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        '''Check if convertCelsiusToKelvin converts the correct temperature from Celsius to Kelvin'''

        for c, k in c_to_k_examples:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(result, k)

class CelsiusToFahrenheit(unittest.TestCase):
    def test_convertCelsiusToFahrenheit(self):
        '''Check if convertCelsiusToFahrenheit converts the correct temperature from Celsius to Fahrenheit'''
        
        for c, f in c_to_f_examples:
            result = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(result, f)        

class FahrenheitToCelsius(unittest.TestCase):
    def test_convertFahrenheitToCelsius(self):
        '''Check if convertFahrenheitToCelsius converts the correct temperature from Fahrenheit to Celsius'''

        for c, f in c_to_f_examples:
            result = conversions.convertFahrenheitToCelsius(f)
            self.assertEqual(result, c)  

class FahrenheitToKelvin(unittest.TestCase):
    def test_convertFahrenheitToKelvin(self):
        '''Check if convertFahrenheitToKelvin converts the correct temperature from Fahrenheit to Kelvin'''

        for f, k in f_to_k_examples:
            result = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(result, k)  

class KelvinToCelsius(unittest.TestCase):
    def test_convertKelvinToCelsius(self):
        '''Check if convertKelvinToCelsius converts the correct temperature from Kelvin to Celsius'''

        for c, k in c_to_k_examples:
            result = conversions.convertKelvinToCelsius(k)
            self.assertEqual(result, c)

class KelvinToFahrenheit(unittest.TestCase):
    def test_convertKelvinToFahrenheit(self):
        '''Check if convertKelvinToFahrenheit converts the correct temperature from Kelvin to Fahrenheit'''

        for f, k in f_to_k_examples:
            result = conversions.convertKelvinToFahrenheit(k)
            self.assertEqual(result, f)  

