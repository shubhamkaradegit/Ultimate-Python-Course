with open("log.html") as f:
    content = f.read()

if("python" in content):
    print("python is present in content")
else:
    print("python is not present in content")