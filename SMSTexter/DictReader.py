import csv


def read(filename) -> dict:
    with open(filename, newline='\n') as csvfile:
        carrier_dict_reader = csv.reader(csvfile, delimiter=',')
        carrier_dict_list = list(carrier_dict_reader)
        carrier_dictionary = dict()
        for carrier_dict_entry_line in carrier_dict_list:
            # Skip first two lines of file
            if carrier_dict_entry_line[0] == 'Cell Carrier' or carrier_dict_entry_line[0] == '':
                continue
            email_list = list(carrier_dict_entry_line)
            # Remove Cell Carrier from list and store
            carrier = email_list.pop(0)
            # Remove blank entries
            formatted_email_list = [email for email in email_list if email != '']
            carrier_dictionary[carrier] = formatted_email_list
        return carrier_dictionary

