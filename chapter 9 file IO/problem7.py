with open("log.html") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is present. Line No. {lineno}")
        break
    lineno += 1


else:
    print(f"python is not present")