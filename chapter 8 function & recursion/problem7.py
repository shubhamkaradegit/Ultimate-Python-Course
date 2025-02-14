# Write a function that takes a list and a word as arguments and returns a new list with the word removed from every item.

def strip(l,word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

def rem(l,word):
    for i in l:
        l.remove(word)
        return l

l = ["Harry","Rohan","Shubham","an"]


print(rem(l,"an"))
print(strip(l,"an"))
