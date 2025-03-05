with open("chapter 9 file IO/this.txt","r") as f:
    content = f.read()

with open("this_copy.txt","w") as f:
    f.write(content)