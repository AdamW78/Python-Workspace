from time import sleep
import imessage
from os import listdir
from os import getcwd


def input_validation_selection(input_string, txt_files_list):
    if input_string.isdigit():
        if int(input_string) > len(txt_files_list):
            print(f"Error: Input \"{input_string}\" is not an option!")
            return False
        return True
    else:
        print(f"Error: Input \"{input_string}\" is not a valid number choice!")
        return False


def ask_for_input(txt_files_list):
    if len(txt_files_list) >= 1:
        if len(txt_files_list) > 1:
            print("Select the text file in which phone numbers are listed")
            print("Options:")
            counter = 1
            for txt_file in txt_files_list:
                print(f"{counter}. {txt_file}")
                counter += 1
            print()
            file_choice = input("Enter the number of your choice: ")
            if input_validation_selection(file_choice, txt_files_list):
                correct_file = txt_files_list[int(file_choice) - 1]
            else:
                print("Exiting program - please run the program with valid input values")
                exit(0)
            return correct_file
        else:
            print(f"Only detected one text file with name \"{txt_files_list[0]}\".")
            yes_no = input("Is this the correct file? Enter \"y\" or \"n\": ").casefold()
            if yes_no == "y" or yes_no == "n":
                if yes_no == "n":
                    print("Move your file to the same folder as this script and run the program again.")
                    exit(0)
            else:
                print(f"Error: Input \"{yes_no}\" is invalid, using \"{txt_files_list[0]}\" as phone number list.")
            return txt_files_list[0]


local_files = listdir(getcwd())
txt_files = []
for file in local_files:
    if file.endswith(".txt"):
        txt_files.append(file)
print(len(txt_files))
filename = ask_for_input(txt_files)
phone_number_list = open(filename, "r")
phone_numbers = phone_number_list.readlines()
text_message = phone_numbers[-1]
i = 0
texts = []
failed_sends = []
while i < len(phone_numbers) - 1:
    cur_line = phone_numbers[i]
    i += 1
    line = cur_line.split()
    phone_number = line.pop()
    name = line.pop()
    print(phone_number)
    # has_imessage = imessage.check_compatibility(phone_number)
    # if has_imessage:
    imessage.send("+1 571-262-9202", text_message)
    # else:
    # failed_sends.append(phone_number)
#sleep(5)
#for text in texts:
    #print(imessage.status(text))
