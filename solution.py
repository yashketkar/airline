import csv

# Part A
# Question 1

# Creating a dictionary to store "Cost per flight hour" for each "Aircraft Type"
# Key: Aircraft Type
# Value: Cost per flight hour
cost_by_type = None

# Creating a dictionary to store "Number of Seats" for each "Aircraft Type"
# Key: Aircraft Type
# Value: Number of Seats
seats_by_type = None

# Populating the cost_by_type and seats_by_type dictionaries with values from ac_characteristics.csv
with open('ac_characteristics.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if cost_by_type is None:
            cost_by_type = {}
            seats_by_type = {}
        else:
            cost_by_type[row[0]]=row[-1]
            seats_by_type[row[0]]=row[-2]

# Creating a dictionary to store "Hours flown" for each "Aircraft Type"
# Key: Aircraft Type
# Value: Hours Flown
hours_by_type = None

# Populating the hours_by_type dictionary with values from operations.csv
with open('operations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if hours_by_type is None:
            hours_by_type = {}
        else:
            hours_flown = sum(int(i) for i in row[2:])
            hours_by_type[row[1]]=hours_flown

# Printing Total Cost for each Aircraft Type
print "Part A - Question 1\nThe Total Cost (Hours flown x Costs/hour) for each Aircraft Type are as follows:"
for aircraft_type in cost_by_type:
    hours_flown = int(hours_by_type[aircraft_type])
    cost_per_hour = int(cost_by_type[aircraft_type])
    print "{0} : {1} x {2} = {3} ".format(aircraft_type, hours_flown, cost_per_hour, hours_flown*cost_per_hour)

# Part A
# Question 2
