#!/usr/bin/env python

import sys
import csv
import math

__author__ = "Yash Ketkar"
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Production"

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
        elif row[1] in hours_by_type:
            hours_by_type[row[1]]+=sum(int(i) for i in row[2:])
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
print "\nThe aircraft type with lowest cost per seat per km is:\n{0} with a cost per seat per km of: {1}.".format(lowest_cost_type, lowest_cost)

# Part B
# Populating the characteristics_by_type dictionary with values from city_pairs.csv
print "\nPart B"
city_pairs = None
with open('city_pairs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if city_pairs is None:
            city_pairs = {}
        else:
            city_pairs[row[0] + "," + row[1]]=[int(row[2]), int(row[3])]

fleet = []
for city_pair in city_pairs:
    # We need to get the aircrafts which have range higher than or equal to the distance between the city pair
    range_aircrafts = [aircraft_type for aircraft_type in characteristics_by_type if characteristics_by_type[aircraft_type][0] >= city_pairs[city_pair][1]]
    # Thus we have eliminated all aircrafts with a lower range
    lowest_cost_for_city_pair = sys.maxint
    lowest_cost_type_for_city_pair = None
    for aircraft_type in range_aircrafts:
        # Number of trips = Passenger Demand / Number of Seats
        number_of_trips = math.ceil(1.0*city_pairs[city_pair][0]/characteristics_by_type[aircraft_type][2])
        # To get cost per trip, we take the distance between the cities
        # and divide it by the average speed to get the time taken for the trip (in hours)
        # we then multiply it by cost per hour for the aircraft type,
        # This will give us the cost for the trip.
        # i.e. Cost = (Distance/Speed) x Cost per hour = (Time) x Cost per hour
        cost_for_trip = (1.0*city_pairs[city_pair][1]/characteristics_by_type[aircraft_type][1])*characteristics_by_type[aircraft_type][3]
        total_cost_incurred = number_of_trips*cost_for_trip
        if total_cost_incurred < lowest_cost_for_city_pair:
            lowest_cost_for_city_pair = total_cost_incurred
            lowest_cost_type_for_city_pair = aircraft_type
    if lowest_cost_type_for_city_pair not in fleet:
        fleet.append(lowest_cost_type_for_city_pair)
    print "\nFor the city pair: {0} the most suitable aircraft type is:\n{1} with a total cost incurred: {2}".format(city_pair, lowest_cost_type_for_city_pair, lowest_cost_for_city_pair)

print "\nThe final resultant fleet would consist of: " + ",".join(fleet)
