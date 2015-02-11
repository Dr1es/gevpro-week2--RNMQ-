#!/usr/bin/env python

import sys

class Country():
    def __init__(self,name):
        self.name = name
        countries = self.getCountries()

    def __str__(self):
        return ("Hello from {}".format(countries))

    def getCountries(self):
        countryList = []
        infile = open("countries_list.txt","r")
        for line in infile:
            country = line.split()
            countryList.append(country)
        return countryList


def main():
    name = Country()


if __name__== "__main__":
    main()
