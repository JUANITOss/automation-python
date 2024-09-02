# Step 1: Create and write to a file
fileWrite = open('example.txt', 'w') 
fileWrite.write('Hello, this is a simple text file created and read by Python!')

fileWrite.close()

# Step 2: Read content in file and save it to content var
fileRead = open('example.txt', 'r')
content = fileRead.read()

fileRead.close()

# Output the content to the console
print(content + '\n\n')

# Step 3: Append to file

fileAppend = open('example.txt', 'a')
fileAppend.write('\nNow we have 2 lines of text!')

fileAppend.close()

# Step 4: Read updated content in file and save it to content var
fileRead = open('example.txt', 'r')
content = fileRead.read()

fileRead.close()

# Output the content to the console
print(content)