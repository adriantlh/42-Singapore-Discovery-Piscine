#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))

ans = first_number * second_number
state = ""

if ans > 0:
    state = "positive"
if ans < 0: 
    state = "negative"
if ans == 0:
    state = "positive and negative"

print (f'{first_number} x {second_number} = {ans}')
print (f'The result is {state}')

