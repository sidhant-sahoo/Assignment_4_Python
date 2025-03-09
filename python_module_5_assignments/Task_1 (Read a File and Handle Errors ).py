# Task 1: Read a File and Handle Errors

try:
    with open('sample.txt','r') as file:
        reading = file.readlines()
        for index, reading in enumerate(reading, start = 1):
            print('Line',index,':',reading)
except FileNotFoundError:
    print("Error: the file 'sample.txt' was not found.")