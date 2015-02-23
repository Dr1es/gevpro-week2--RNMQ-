#!/usr/bin/env python

import sys
from flag_color import FlagColor

class Country(FlagColor):
    """Constructor"""
    def __init__(self):
        countries = self.getCountries()

    def getCountries(self):
        """Get data from a text file and print it like
            Hello from {data}"""
        with open("countries_list.txt", "r")as f:
            countries = [line.strip() for line in f]
        for word in countries:
            self.color_picker()
            print("Hello from {}".format(word))

def main():
    name = Country()

if __name__== "__main__":
    main()
