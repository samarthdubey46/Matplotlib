import csv
import random
import time
x_value = 0
total_1 = 1000
total_2 = 1000
fieldnames = ["x_value", "total_1", "total_2"]
with open("test1.csv",'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
while True:
    with open("test1.csv",'a') as cs:
        writer = csv.DictWriter(cs,fieldnames=fieldnames)
        info = {
            "x_value" : x_value,
            "total_1" : total_1,
            "total_2" : total_2
        }
        writer.writerow(info)
        x_value += 2
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
        time.sleep(2)