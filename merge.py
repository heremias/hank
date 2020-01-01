l1 = [1,2,3,5,7,8,9,11,13,19]
l2 = [1,3,6,7,7,12,15,18,20,24,34]
nums = []
done = False


def merge_left (l1, l2):
    global done
    p1 = l1[0]
    p2 = l2[0]
    if len(l1) == 1 and len(l2) == 1:
        pass
    elif len(l1) == 1 and p1 > p2:
        nums.append(p2)
        l2.remove(p2)
        pass
    elif len(l1) == 1 and p1 < p2:
        nums.append(p1)
        nums.extend(l2)
        l1.remove(p1)
        del l2[:]
        done = True
        return done
    elif len(l2) == 1 and p1 > p2:
        nums.append(p2)
        nums.extend(l1)
        l2.remove(p2)
        del l2[:]
        done = True
        return done
    elif len(l2) == 1 and p1 < p2:
        nums.append(p1)
        l1.remove(p1)
        pass
    elif p1 < p2:
        nums.append(p1)
        l1.remove(p1)
        pass
    elif p2 < p1:
        nums.append(p2)
        l2.remove(p2)
        pass
    elif p1 == p2:
        nums.append(p1)
        l1.remove(p1)
        l2.remove(p2)
        pass

while done == False :
    merge_left(l1,l2)
#    print(l1)
#    print(l2)
 
print(nums)
print(done)