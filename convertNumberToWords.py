#!/usr/bin/env python3

import requests as req
import re

number = float(input("Enter number: "))

url = f'https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={number}&letter_case=lowercase&action=solve'
resp = req.get(url)

pattern = "<div id=\"answer\" class=\"still\"><br>([a-z\s\-\.]+)<\/div>"

#print(resp.text) # Printing response
numberInWords = re.search(pattern, resp.text)
print(numberInWords[1])


