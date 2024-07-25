numeral_input = input("Input Roman Numberals to be converted: ")

def roman_numeral_to_int(numeral):
    converted_int = 0

    if "CM" in numeral:
        converted_int += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        converted_int += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        converted_int += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        converted_int += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        converted_int += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        converted_int += 4
        numeral = numeral.replace("IV", "")

    for i in numeral:
        if i == "M":
            converted_int += 1000
        elif i == "D":
            converted_int += 500
        elif i == "C":
            converted_int += 100
        elif i == "L":
            converted_int += 50
        elif i == "X":
            converted_int += 10
        elif i == "V":
            converted_int += 5
        elif i == "I":
            converted_int += 1

    print("The roman numerals you entered translates to: " + str(converted_int) + "!")

roman_numeral_to_int(numeral_input)
