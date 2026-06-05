s = "()[]{}"
#s = "(]"
#s = "([)]"
#s = "{[]}"
#s = "]"
ans = True

def validateOpenClose(c):
    if c in "([{":
        return True
    return False

d = {"(" : ")",
     "[" : "]",
     "{" : "}"}

collection = []

for c in s:
    if validateOpenClose(c):
        collection.append(c)
    else:
        if len(collection) == 0:
            ans = False
            break
        temp = collection.pop()
        #print(d[temp])
        if d[temp] != c:
            ans = False
            break

if len(collection) > 0:
    ans = False

#print(collection)

print("answer is: " + str(ans))