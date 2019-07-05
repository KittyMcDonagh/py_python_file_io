f = open("chal2_mcdonagh.txt","r+")
f.write("Gone")

f.seek(0, 2)
f.write("Last line")
f.seek(0)
lines = f.read()
print(lines)

f.close()



