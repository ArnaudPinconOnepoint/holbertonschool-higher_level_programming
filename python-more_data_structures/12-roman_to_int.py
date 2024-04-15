#!/usr/bin/python3
def roman_to_int(roman_string):
    # Dictionary of Roman Numerals
    dict={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    # Result to return
    res = 0
    # Last number saved
    last_rom_val = None
    # Check if roman_string is a string or not None
    if (roman_string is None or not isinstance(roman_string, str)):
        return res
    # Loop to check each roman numeral
    for i in roman_string:
        rom_val = dict.get(i)
        # Check if the current char is not a roman numeral
        if rom_val is None:
            return 0
        if last_rom_val == None or rom_val <= last_rom_val:
            res = res + rom_val
            last_rom_val = rom_val
        # If the rom_val is greater than last_rom_val, we need to cancel the previous sum
        # then add to the final result the subtraction of rom_val with last_rom_val.
        elif rom_val > last_rom_val:
            res = res - 2*last_rom_val + rom_val
            last_rom_val = rom_val
    return res
