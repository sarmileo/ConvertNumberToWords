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
    url = f'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={number}&letter_case=lowercase&action=solve'
elif option == "2":
    url = f'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={number}&format=currency&letter_case=lowercase&action=solve'
elif option == "3":
    url = f'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={number}&format=check&letter_case=lowercase&action=solve'
resp = req.get(url)

pattern = "<div id=\"answer\" class=\"still\"><br>([a-z\s\-\.]+)<\/div>"
patternCheckWriting = "<div id=\"answer\" class=\"still\"><br>([a-z\s\-]+)<br><strong>or<\/strong><br> ([a-z\s\-\/\d]+)<\/div>"
#print(resp.text) # Printing response

if option == "1" or option == "2":
    numberInWords = re.search(pattern, resp.text)
    print()
    print(numberInWords[1])
if option == "3":
    numberInWords = re.search(patternCheckWriting, resp.text)
    print()
    print(numberInWords[1] + "\n or \n" + numberInWords[2])



