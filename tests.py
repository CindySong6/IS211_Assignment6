import unittest
import conversions
import conversions_refactored


c_to_f_to_k_examples =  ((0, 32, 273.15),
                    (-273.15, -459.67, 0),
                    (100, 212, 373.15),
                    (-50.93, -59.67, 222.22),
                    (72.34, 162.21, 345.49))

class ConversionTest(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        '''Check if convertCelsiusToKelvin converts the correct temperature from Celsius to Kelvin'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(result, k)

    def test_convert_celsius_to_fahrenheit(self):
        '''Check if convertCelsiusToFahrenheit converts the correct temperature from Celsius to Fahrenheit'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(result, f)        

    def test_convert_fahrenheit_to_celsius(self):
        '''Check if convertFahrenheitToCelsius converts the correct temperature from Fahrenheit to Celsius'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertFahrenheitToCelsius(f)
            self.assertEqual(result, c)  

    def test_convert_fahrenheit_to_kelvin(self):
        '''Check if convertFahrenheitToKelvin converts the correct temperature from Fahrenheit to Kelvin'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(result, k)  

    def test_convert_kelvin_to_celsius(self):
        '''Check if convertKelvinToCelsius converts the correct temperature from Kelvin to Celsius'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertKelvinToCelsius(k)
            self.assertEqual(result, c)

    def test_convert_kelvin_to_fahrenheit(self):
        '''Check if convertKelvinToFahrenheit converts the correct temperature from Kelvin to Fahrenheit'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions.convertKelvinToFahrenheit(k)
            self.assertEqual(result, f)  


# Using convert() function from conversions_refactored to convert units
class RefactoredConversionTest(unittest.TestCase):

    # checking all temperature conversions using convert() function
    def test_convert_celsius_to_kelvin(self):
        '''Check if convert() function converts the correct temperature from Celsius to Kelvin'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('Celsius', 'Kelvin', c)
            self.assertEqual(result, k)

    def test_convert_celsius_to_fahrenheit(self):
        '''Check if convert() function converts the correct temperature from Celsius to Fahrenheit'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('celsius', 'fahrenheit', c)
            self.assertEqual(result, f)        

    def test_convert_fahrenheit_to_celsius(self):
        '''Check if convert() function converts the correct temperature from Fahrenheit to Celsius'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('fahrenheit', 'celsius', f)
            self.assertEqual(result, c)  

    def test_convert_fahrenheit_to_kelvin(self):
        '''Check if convert() function converts the correct temperature from Fahrenheit to Kelvin'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('fahrenheit', 'kelvin', f)
            self.assertEqual(result, k)  

    def test_convert_kelvin_to_celsius(self):
        '''Check if convert() function converts the correct temperature from Kelvin to Celsius'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('kelvin', 'celsius', k)
            self.assertEqual(result, c)

    def test_convert_kelvin_to_fahrenheit(self):
        '''Check if convert() function converts the correct temperature from Kelvin to Fahrenheit'''
        for c, f, k in c_to_f_to_k_examples:
            result = conversions_refactored.convert('kelvin', 'fahrenheit', k)
            self.assertEqual(result, f)  


    # checking all distance conversion using convert()
    def test_convert_mile_to_yard(self):
        '''Check if convert() function converts the correct distance from Mile to Yard'''
        result1 = conversions_refactored.convert('mile', 'yard', 1)
        self.assertEqual(result1, 1760)
        result2 = conversions_refactored.convert('MILE', 'YARD', 3.52)
        self.assertEqual(result2, 6195.2)

    def test_convert_mile_to_meter(self):
        '''Check if convert() function converts the correct distance from Mile to Meter'''
        result1 = conversions_refactored.convert('mile', 'Meter', 1)
        self.assertEqual(result1, 1609.34)
        result2 = conversions_refactored.convert('MILE', 'meter', 3.52)
        self.assertEqual(result2, 5664.89)

    def test_convert_meter_to_yard(self):
        '''Check if convert() function converts the correct distance from Meter to Yard'''
        result1 = conversions_refactored.convert('meter', 'yard', 1000)
        self.assertEqual(result1, 1093.61)
        result2 = conversions_refactored.convert('METER', 'Yard', 123.45)
        self.assertEqual(result2, 135.01)

    def test_convert_meter_to_mile(self):
        '''Check if convert() function converts the correct distance from Meter to Mile'''
        result1 = conversions_refactored.convert('meter', 'mile', 1000)
        self.assertEqual(result1, 0.62)
        result2 = conversions_refactored.convert('METER', 'MILE', 234834)
        self.assertEqual(result2, 145.92)

    def test_convert_yard_to_mile(self):
        '''Check if convert() function converts the correct distance from Yard to Mile'''
        result1 = conversions_refactored.convert('yard', 'mile', 12345)
        self.assertEqual(result1, 7.01)
        result2 = conversions_refactored.convert('Yard', 'MILE', 100000.57)
        self.assertEqual(result2, 56.82)

    def test_convert_yard_to_meter(self):
        '''Check if convert() function converts the correct distance from Yard to Meter'''
        result1 = conversions_refactored.convert('yard', 'Meter', 1234)
        self.assertEqual(result1, 1128.37)
        result2 = conversions_refactored.convert('Yard', 'Meter', 10.5)
        self.assertEqual(result2, 9.60)

    # checking if converting to the same unit will work
    def test_convert_same_unit(self):
        '''Check if convert() function converts the correct output for the same unit'''
        result1 = conversions_refactored.convert('Mile', 'Mile', 1000)
        self.assertEqual(result1, 1000)
        result2 = conversions_refactored.convert('Celsius', 'celsius', -120.15)
        self.assertEqual(result2, -120.15)

    # checking invalid or incompatible inputs, expect to raise exception
    def test_fail_convert_incompatible_units(self):
        '''Check if convert() function raises ConversionNotPossible Error for incompatible unit conversion'''
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, 'meter', 'celsius', 10)

    def test_fail_convert_invalid_input(self):
        '''Check if convert() function raises ConversionNotPossible Error for bad input type'''
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, 0, 4, 'number')
        self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, 'mile', 'meter', '4.1')

if __name__ == '__main__':
    unittest.main()