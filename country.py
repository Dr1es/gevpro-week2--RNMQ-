#!/usr/bin/env python

import sys
from flag_color import FlagColor

class Country():
    def __init__(self):
        countries = self.getCountries()
        print((r,g,b))

    def getCountries(self):
        with open("countries_list.txt", "r")as f:
            countries = [line.strip() for line in f]
        for word in countries:
            print("Hello from {}".format(word))

def main():
    name = Country()

if __name__== "__main__":
    main()
