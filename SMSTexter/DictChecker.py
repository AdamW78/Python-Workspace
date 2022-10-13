from os import listdir
from os.path import isfile
from csv import reader


def is_csv_dict(filename) -> bool:
    """
    Checks whether a given file is a cell carrier dictionary

    :param filename: file to check
    :return: boolean for whether file is a csv dictionary
    """
    if filename.endswith("csv"):
        csv_reader = reader(filename)
        headers = list()
        for row in csv_reader:
            list.append(row)
            break
        print(headers[0])



def has_csv_dict() -> bool:
    """
    Checks whether user has already written a CSV file from cell carrier dictionary

    :return: Boolean value for whether user has cell carrier dictionary stored locally
    """
    files = [f for f in listdir('.') if isfile(f)]
    for file in files:
        if is_csv_dict(file):
            return True
