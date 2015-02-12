def getCountries():
    with open("countries_list.txt", "r")as f:
        countries = [line.strip() for line in f]
    return countries

def main():
    do = getCountries()
    print(do)

main()
