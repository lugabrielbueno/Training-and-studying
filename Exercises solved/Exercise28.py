#Tax Calculator - Asks the user to enter a cost and either a country or state sale tax. It then returns the tax plus the total cost with tax.

# List with all states and sale taxes
all_states = [(	'Alaska', 0),
	('Alabama',4),
	('Arkansas',6.5),
	('Arizona',5.6),
	('California',7.5),
	('Colorado',2.9),
	('Connecticut',6.35),
	('Delaware',0),
	('Florida',6),
	('Georgia',4),
	('Hawaii',4),
	('Iowa',6),
	('Idaho',6.5),
	('Illinois',6.25),
	('Indiana',7),
	('Kansas',6.5),
	('Kentucky',6),
	('Louisiana',4.45),
	('Massachusetts',6.25),
	('Maryland',6),
	('Maine',5.5),
	('Michigan',6),
	('Minnesota',6.875),
	('Missouri',4.225),
	('Mississippi',7),
	('Montana',0),
	('North Carolina',4.75),
	('North Dakota',5),
	('Nebraska',5.5),
	('New Hampshire',0),
	('New Jersey',6.625),
	('New Mexico',5.125),
	('Nevada',6.85),
	('New York',4),
	('Ohio',5.75),
	('Oklahoma',4.5),
	('Oregon',0),
	('Pennsylvania',6),
	('Rhode Island',7),
	('South Carolina',6),
	('South Dakota',4.75),
	('Tennessee',7),
	('Texas',6.25),
	('Utah',6.1),
	('Virginia',5.3),
	('Vermont',6),
	('Washington',6.5),
	('Wisconsin',5),
	('West Virginia',6),
	('Wyoming',4)]

def tax_by_state():

    #Receiving the inputs
    while True:
        state = input('State : ').title()
        cost = float(input('Your price : '))

        #Looking for the state
        for stat in all_states:
                if stat[0] == state.title():
                    #Founded, now calculating the tax
                    tax = cost*(stat[1]/100)
                    #Condition to no taxes
                    if tax == 0:
                        print("There's no taxes for sale in {}".format(stat[0].title()))
                        return round(cost,2)
                        #if have taxes...
                    else:
                        print("That's your price with taxes")
                        return round(cost + cost*(stat[1]/100),2)
print(tax_by_state())