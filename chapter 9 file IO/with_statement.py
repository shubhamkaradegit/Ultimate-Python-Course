f = open("file.txt")
print(f.read())
f.close()

# the same can be written using with statatment

with open("file.text") as f:
    print(f.read())

# you don't have to explicitely close the file

