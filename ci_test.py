with open('myfile.txt','r+') as f:
    f.write('Line 0')
    current_position = f.tell()
    f.seek(current_position + 8)
    f.write('Line 6')
    f.seek(0, 2)
    f.write('\nLine 5')