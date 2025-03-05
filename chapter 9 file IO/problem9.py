with open("chapter 9 file IO/this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("both content are same")
else:
    print("both content are not same")