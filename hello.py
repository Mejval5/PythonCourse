#!/usr/bin/python3
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

name = sys.argv[1] if len(sys.argv) > 1 else 'Human'

import greeting

print(__name__)
print("Hello script")
greeting.greeting(name)