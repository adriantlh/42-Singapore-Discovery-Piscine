#!/usr/bin/env python3

def greetings(x=None):
    if isinstance(x, int):
        print('Error, It was not a name.')
    elif x is None:
        print('Hello, noble stranger.')
    else:
        print(f'Hello, {x}.')


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
