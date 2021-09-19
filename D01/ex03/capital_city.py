def capital_city(argv):
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
    if len(argv) > 1:
        exit(1);

    state = argv[1]
	reponse = capital_cities[states[state]] if state in states else "Unknow state"
	print(reponse)
    
if __name__ == '__main__':
    import sys
    capital_city(sys.argv)
