def rev_str(string):
    length=len(string)
    for i in range(length-1,-1,-1):
        return string[i]
for char in rev_str("hello"):
    print char,
