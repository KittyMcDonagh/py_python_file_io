f = open("kitty.txt","w+")
f.write("Line 1\nLine 2\nLine 3\n")

f.seek(0)

lines = f.read()

f.close()

print(lines)



