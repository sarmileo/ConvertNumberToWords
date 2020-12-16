#!/usr/bin/env python3

import requests as req
import re

number = float(input("Enter number: "))

print("""
Options
1- Word Representation
2- Currency
3- Check Writing""")
option = input("Select: ")

url = ""
if option == "1":
    format = ""
elif option == "2":
    format = "&format=currency"
elif option == "3":
    format = "&format=check"
    
url = f'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={number}{format}&letter_case=lowercase&action=solve'

resp = req.get(url)

# pattern for option 1 and 2, for option 3 with float values
pattern1 = "<div id=\"answer\" class=\"still\"><br>([\w\s\/\-]*)<\/div>"
#pattern for option 3 with integer values
pattern2 = "<div id=\"answer\" class=\"still\"><br>([\w\s\-]*)<br><strong>or<\/strong><br> ([\w\s\-\/]*)<\/div>"

pattern = ""
result = ""
numberInWords = ""

#check for option 1 or 2
if option == "1" or option == "2":
    pattern = pattern1
    numberInWords = re.search(pattern1, resp.text)
#check for option 3 and if the number is not integer
elif option == "3" and number != int(number):
    pattern = pattern1
    numberInWords = re.search(pattern, resp.text)
#check for option 3 if the number is integer
elif option == "3":
    pattern = pattern2
    numberInWords = re.search(pattern, resp.text)

#result for pattern1 has group 1
#result for pattern2 has group 1 and 2
if pattern == pattern1:
    result = numberInWords[1]
if pattern == pattern2:
    result = f"{numberInWords[1]}\n or\n{numberInWords[2]}"

print()
print(result)

filename = "numberToWords.txt"
with open(filename, "w") as file:
    file.write(result)



