#how to dedect spam comments
p1 = "make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
