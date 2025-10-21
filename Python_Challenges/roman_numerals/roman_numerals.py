"""
Convert numbers to roman numerals.

Input number to create class instance
to_roman() method to return roman numeral
"""

class RomanNumeral:
    def __init__(self, number):
        self.number = str(number)

    ROMAN_NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def to_roman(self):
        roman_numeral = ''
        to_convert = self.number
        
        
        for key, value in self.__class__.ROMAN_NUMERALS.items():
            mutiplier, remainder = divmod(to_convert, value)
            if mutiplier > 0:
                roman_numeral += key * mutiplier
            to_convert = remainder

        return roman_numeral