'''
a = "a very long string with emails"

emails = []
3 seconds
'''
'''

f = open("file.txt")
data = f.read()
print(data)
f.close()

st = "Hey shubham you are amazing"

w = open("myfile.txt","w")
w.write(st)
w.close()

'''

f = open("file.txt")

# lines = f.readlines()
# print(lines , type(lines))

# line1 = f.readline()
# print(line1 , type(line1))

# line2 = f.readline()
# print(line2 , type(line2))

# line3 = f.readline()
# print(line3 , type(line3))

# line4 = f.readline()
# print(line4 == "")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
    
f.close()