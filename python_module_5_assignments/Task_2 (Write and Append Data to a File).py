# Task 2: Write and Append Data to a File

with open('output.txt','w') as file:
    write = file.write(input('Enter text to write to the file: '))
    print('Data successfully written to output.txt.')
with open('output.txt','a') as file:
    append = file.write('\n'+ input('Enter additional text to append: '))
    print('Data successfully append.')
with open('output.txt','r') as file:
    read = file.readlines()
    print('Final content of the output.txt:')
    for i in read:
        print(i)