import sys
import csv

# Part A
# Question 1
# Here we need to find: Total cost = Hours flown * Costs/hour

# Creating a dictionary to store "Characteristics" for each "Aircraft Type"
# Key: Aircraft Type
# Value: List of integers the form [Range (km), Average Speed (km/h), Number of Seats, Costs per flight hour]
characteristics_by_type = None

# Populating the characteristics_by_type dictionary with values from ac_characteristics.csv
with open('ac_characteristics.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if characteristics_by_type is None:
            characteristics_by_type = {}
        else:
            characteristics_by_type[row[0]]=[int(i) for i in row[1:]]

# Creating a dictionary to store total "Hours flown" for each "Aircraft Type"
# Key: Aircraft Type
# Value: Integer indicating Total (Sum) Hours Flown in 2014
hours_by_type = None

# Populating the hours_by_type dictionary with values from operations.csv
with open('operations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if hours_by_type is None:
            hours_by_type = {}
        else:
            hours_by_type[row[1]]=sum(int(i) for i in row[2:])

# Printing Total Cost for each Aircraft Type
# Also populating total_cost_by_type dictionary
print "Part A - Question 1\nThe Total Cost (Hours flown x Costs/hour) for each Aircraft Type are as follows:"
total_cost_by_type = {}
for aircraft_type in characteristics_by_type:
    # Total hours flown in 2014 from the dictionary which we populated
    hours_flown = hours_by_type[aircraft_type]
    # Cost per hour is the last element of the list in characteristics_by_type dictionary's value
    cost_per_hour = characteristics_by_type[aircraft_type][3]
    # Calculating total cost by type
    total_cost_by_type[aircraft_type] = hours_flown*cost_per_hour
    print "{0} : {1} x {2} = {3} ".format(aircraft_type, hours_flown, cost_per_hour, total_cost_by_type[aircraft_type])

# Part A
# Question 2
# Here we need to find: Total cost / (number of seats * number of km flown)
# We have already found total cost above
# Number of seats by type have already been given
# We now have to find number of km flown
# i.e. Avg Speed (km/h) x number of hours flown
print "\nPart A - Question 2"
lowest_cost = sys.maxint
lowest_cost_type = None
number_of_km_by_type = {}
for aircraft_type in characteristics_by_type:
    # number of km = avg speed (km/hr) x total number of hours
    number_of_km_by_type[aircraft_type] = characteristics_by_type[aircraft_type][1]*hours_by_type[aircraft_type]
    # cost per seat per km = cost x (1.0/number of seats) x (1.0/number of km)
    cost_per_seat_per_km = total_cost_by_type[aircraft_type]*(1.0/characteristics_by_type[aircraft_type][2])*(1.0/number_of_km_by_type[aircraft_type])
    if lowest_cost > cost_per_seat_per_km:
        lowest_cost = cost_per_seat_per_km
        lowest_cost_type = aircraft_type
print "The aircraft type with lowest cost per seat per km is: {0} with a cost per seat per km of: {1}.".format(lowest_cost_type, lowest_cost)
