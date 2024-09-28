

def romanToInterger(roman: str) -> int:
    roman_to_interger = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ans = 0

    # for i, roman_number in enumerate(roman):
    #     roman_value = roman_to_interger[roman_number]
    #     if roman_number == "V" and roman[i-1] == "I":
    #         roman_value = roman_to_interger["V"]-roman_to_interger["I"]
    #     elif roman_number == "X" and roman[i-1] == "I":
    #         roman_value = roman_to_interger["X"]-roman_to_interger["I"]
    #     elif roman_number == "L" and roman[i-1] == "X":
    #         roman_value = roman_to_interger["L"]-roman_to_interger["X"]
    #     elif roman_number == "C" and roman[i-1] == "X":
    #         roman_value = roman_to_interger["C"]-roman_to_interger["X"]
    #     elif roman_number == "M" and roman[i-1] == "C":
    #         roman_value = roman_to_interger["M"]-roman_to_interger["C"]
    #     elif roman_number == "D" and roman[i-1] == "C":
    #         roman_value = roman_to_interger["D"]-roman_to_interger["C"]
    #     ans += roman_value

    for i in range(len(roman)):
        current_value = roman_to_interger[roman[i]]
        if i < (len(roman)-1) and current_value < roman_to_interger[roman[i+1]]:
            ans -= current_value
        else:
            ans += current_value

    return ans


print(romanToInterger("LVIII"))


# The key intuition lies in the fact that in Roman numerals, when a smaller value appears
# before a larger value, it represents subtraction, while when a smaller value appears after
# or equal to a larger value, it represents addition.

# Example Walkthrough:

# For the input "MCMXCIV":

#     Start with "M" = 1000 → ans = 1000
#     "C" < "M" → Subtract "C" = 100 → ans = 900
#     "M" = 1000 → Add "M" → ans = 1900
#     "X" < "C" → Subtract "X" = 10 → ans = 1890
#     "C" = 100 → Add "C" → ans = 1990
#     "I" < "V" → Subtract "I" = 1 → ans = 1989
#     "V" = 5 → Add "V" → ans = 1994
