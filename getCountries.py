def getCountries():
    countryList = []
    infile = open("countries_list.txt","r")
    for line in infile:
        country = line.split()
        countryList.append(country)
    return countryList


def main():
    do = getCountries()
    print(do)


main()
