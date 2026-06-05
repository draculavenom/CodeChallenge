disks = 3#input("give me the number of disks")
origin = 1#input("give me the tower where the disk are, it should be represented by a number from 1 to 3")
destination = 3#input("give me the tower where the disk will be, it should be represented by a number from 1 to 3")

print("number of disk is " + str(disks) + ", origin is tower " + str(origin) + " and I want to move them to tower " + str(destination))

def solution(di, o, de):
    #print("di: " + str(di) + "; o: " + str(o) + "; de: " + str(de))
    if di == 1:
        print("move from " + str(o) + " to " + str(de))
        return 
    solution(di - 1, o, getAuxiliar(o, de))
    print("move from " + str(o) + " to " + str(de))
    solution(di - 1, getAuxiliar(o, de), de)
        

def getAuxiliar(o, de):
    if o == 1:
        if de == 3:
            return 2
        else:
            return 3
    elif o == 2:
        if de == 3:
            return 1
        else:
            return 3
    if de == 1:
        return 2
    return 1

solution(disks, origin, destination)