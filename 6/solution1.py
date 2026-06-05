list1 = [1, 2, 4]
list2 = [1, 3, 4]

#list1 = [5, 10, 15]
#list2 = [1, 2, 3]

#list1 = []
#list2 = [0]
ans = []

i = 0
j = 0
while i < len(list1) and j < len(list2):
    a = list1[i]
    b = list2[j]
    if a < b:
        ans.append(a)
        i = i + 1
    else:
        ans.append(b)
        j = j + 1

while i < len(list1):
    ans.append(list1[i])
    i = i + 1

while j < len(list2):
    ans.append(list2[j])
    j = j + 1

print("the answer is: " + str(ans))