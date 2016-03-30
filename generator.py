# Python 3
import random
from statistics import median
import json
import csv

def random_data(n, minimum, maximum):
    i = 1
    with open("output.csv", "a") as csv_file:
        w = csv.writer(csv_file)
        while i <= n:
            w.writerow([i,int(random.uniform(minimum, maximum)),'PayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayload'])
            i += 1
    return


def normal_data(n, mu, sigma):
    i = 1
    with open("output.csv", "a") as csv_file:
        w = csv.writer(csv_file)
        while i <= n:
            w.writerow([i,int(random.normalvariate(mu, sigma)),'PayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayloadPayload'])
            i += 1
    return


n = int(input ("Number of samples (n) = "))


data_type = input ("Choose data type: (R)andom, (N)ormal: ")

if data_type == "R" or data_type == "r":
    minimum = float(input("Choose minimum data value: "))
    maximum = float(input("Choose maximum data value: "))
    random_data(n, minimum, maximum)
elif data_type == "N" or data_type == "n":
    mu = float(input("Choose mean: "))
    sigma = float(input("Choose std dev: "))
    normal_data(n, mu, sigma)
else:
    print ("Sorry, selection unknown.")





print ("Data has been exported to output.csv")
