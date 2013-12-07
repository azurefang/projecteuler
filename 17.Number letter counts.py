#!/usr/bin/env python
# -*- coding: utf-8 -*-

units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
moreThanTen = ['ten', 'eleven', 'twelve', 'thirteen', 'foueteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

number = []
for i in range(1, 1000):
    num = str(i)
    length = len(num)
    if  length == 1:
        number.append(len(units[i-1]))
    elif length == 2:
        if num[0] == '1':
            number.append(len(moreThanTen[i-10]))
        else:
            if num[1] != '0':
                number.append(len(tens[i//10-2]) + number[i%10-1])
            else:
                number.append(len(tens[i//10-2]))
    else:
        if num[1:] != '00':
            number.append(number[i//100-1] + len('hundred') + len('and') + number[i%100-1])
        else:
            number.append(number[i//100-1] + len('hundred'))

number.append(number[0] + len('thousand'))

print sum(number)
