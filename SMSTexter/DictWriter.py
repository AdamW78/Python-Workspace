import csv


class DictWriter:

    def __init__(self, dictionary, filename):
        """
        Writes passed in cell carrier dictionary to csv file to cache locally

        :param dictionary: dictionary object containing cell carrier keys as strings and lists of text-to-email addresses as strings
        :param filename: string name of csv file to write
        :raises IOError: If writing to the CSV file fails, raise an IOError
        """
        csv_columns = ["Cell Carrier", "Email 1", "Email 2", "Email 3", "Email 4", "Email 5"]
        csv_file = filename+".csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for key in dictionary:
                    write_list = [key]
                    for email in dictionary[key]:
                        write_list.append()
                    writer.writerow(write_list)
        except IOError:
            raise IOError(f"Error: Failed to write cell carrier dictionary to {filename}.csv")




