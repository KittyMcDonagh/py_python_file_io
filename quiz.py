# Open file, for read only
# Define a variable, 'f', that opens the file

# Open file with relative path
# f = open('files/relative_data.txt', 'r')

f = open('/home/ubuntu/environment/files/relative_data.txt', 'r')

# Call the readlines() and assign it to variable 'lines'
# lines = f.readlines()
lines = f.read()

# Close the file handle
f.close()

# Print the results to screen
print(lines)