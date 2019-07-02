# When you open a file, the variable you use (f) stores an object called a 
# file handle. It allows us to manipulate our files.
# There are various methods attached to the file handle which allow us to
# manipulate our file. If you type 'f.' a list of  the methods will show:
# read(), readlines(), close(), etc.

# When you open a file you're reading / writing at a certain position in that
# file.

f = open('data.txt', 'r')

# When you read a line from the file, the file position is advanced whatever
# number of lines are in that line. The next time you read a line the data will
# be read from that new position. When python sees a '\n' it interprets it as
# as a break between lines. Files use a cursor to track where they are.

line = f.readline()
