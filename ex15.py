from sys import argv #import method of sys-library

script, filename = argv #get argumens values

txt = open(filename) #open file

print(f"Here's your file {filename}") #print filename
print(txt.read()) #print file's content

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
