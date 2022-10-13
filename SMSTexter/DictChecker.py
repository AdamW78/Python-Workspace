from os import listdir
from os.path import isfile
from csv import reader

csv_dict_filename = ""
def is_csv_dict(filename) -> bool:
    """
    Checks whether a given file is a cell carrier dictionary

    :param filename: file to check
    :return: boolean for whether file is a csv dictionary
    """
    if filename.endswith("csv"):
        with open(filename, newline='\n') as csvfile:

            csv_reader = reader(csvfile)
            csv_file_list = list(csv_reader)
            headers = csv_file_list[0]
            if 'Cell Carrier' in headers:
                return True
            else:
                return False


def has_csv_dict() -> bool:
    """
    Checks whether user has already written a CSV file from cell carrier dictionary

    :return: Boolean value for whether user has cell carrier dictionary stored locally
    """
    files = [f for f in listdir('.') if isfile(f)]
    for file in files:
        if is_csv_dict(file):
            csv_dict_filename = file
            return True
    return False


def get_csv_dict() -> str:
    if not csv_dict_filename == "":
        raise Exception("Error: Tried to fetch .csv dict file but none was found")
    return csv_dict_filename
