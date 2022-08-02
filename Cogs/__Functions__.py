import time
import os
import csv

def check_for_file(file_name:str):
    for file in os.listdir():
        if file == file_name:
           return True
        else:
            False

def create_file(file_name:str, inside_text:str):
    with open(file_name, "w") as wf:
        wf.write(inside_text)

def append_file(file_name:str, inside_text:str, write_file_if_not_found:bool=False):
    if check_for_file(file_name):
        with open(file_name, "a") as af:
            if inside_text == "":
                pass
            else:
                af.write(f"{inside_text}\n")
    elif check_for_file(file_name) != True and write_file_if_not_found:
        create_file(file_name, inside_text)

def give_file_line(file_name:str, file_line_number:int):
    if check_for_file(file_name):
        with open(file_name, "r") as rf:
            file_line = rf.readlines()
            return file_line[file_line_number - 1]
    else:
        print(f"The file {file_name} could not be found.\nThe file could be in a another directory that this program does not have the permission to enter.")
        exit(-1)

def give_file_lines(file_name:str):
    if check_for_file(file_name):
        with open(file_name, "r") as rf:
            file_lines = rf.readlines()
            return file_lines
    else:
        print(f"The file {file_name} could not be found.\nThe file could be in a another directory that this program does not have the permission to enter.")
        exit(-1)

def get_time():
    timeVar = time.strftime("%Y:%m:%d:%I:%M:%S %p")
    return timeVar
