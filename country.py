#!/usr/bin/env python

import sys

class Country():
    def __init__(self):
        countries = self.getCountries()

    def __str__(self):  
        return("Hello from {}".format(self.getCountries))

    def getCountries(self):
        with open("countries_list.txt", "r")as f:
            countries = [line.strip() for line in f]
        return countries


def main():
    name = Country()
    print(name)

if __name__== "__main__":
    main()
