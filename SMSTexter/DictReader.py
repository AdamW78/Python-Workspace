import csv


def read(filename):
    with open(filename, newline='\n') as csvfile:
        dict_reader = csv.reader(filename, delimiter=',')
        carrier_dictionary = dict()
        for row in dict_reader:
            if row == f"{filename}.csv":
                continue
            print()


read("carrierdict.csv")