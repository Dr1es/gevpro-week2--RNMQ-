def getCountries():
    countryList = []
    infile = open("countries_list.txt","r")
    for line in infile:
        country = line.split()
        countryList.append(Country(country))
        return countryList
