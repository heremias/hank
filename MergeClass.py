z = [[1,2,3],[5,7,7],[9,10,13]]
x = [[1,2,3],[5,7,7],[9,10,13]]
y = [[1,1,3],[4,7,8],[9,11,13]]

point = [[x,y,z],[x,y,z],[x,y,z]]
present = point[0][0]
past = point[1][0]
future = point[2][0]
print(point)
print(present)
print(past)
print(future)

l1 = [[1,2,3],[5,7,8],[9,11,13]]
l2 = [[1,3],[6,7],[7,12],[15,18],[20,24]]
l3 = [[4,7,9],[22,45],[78]]
l4 = [[3,6,7,10],[12,12,12,13],[14,15,18,20]]
l5 = [[1,3,6,12,15],[18,20,24,34,65],[67,78,84,87,94]]
l6 = [[4],[7,9],[11,23,34],[35,36,45,47],[48,57,595,6,59],[50,660,60,7,80890,990],[12,3,465,4,3,53,6]]
l7 = [1,3,6,7,10,12,15,18,20,24,34,99,100,10000]
l8 = [8,57,595,6,59,50,660,60,7,80890,990,12,3,465,4,3,53,6]

done = False
matrix_count = False
nums = []
i = 0

n = 0
matrix = [l1, l2, l3, l4, l5, l6, l7]

#xval = [x for i in y]
#xindex = [y for i in x]
#print(xval)
#print(xindex)

def merge_left (matrix):
    global done
    matrix_count = True
    k1 = matrix[0]
    k2 = matrix[1]
    p1 = k1[0]
    p2 = k2[0]
    if len(k1) == 1 and p1 > p2:
        nums.append(p2)
        k2.remove(p2)
        pass
    elif len(k1) == 1 and p1 < p2:
        nums.append(p1)
        nums.extend(k2)
        k1.remove(p1)
        matrix.pop(0)
        matrix.pop(0)
        done = True
        matrix_count = False
        matrix.insert(0, nums)
        #return done
    elif len(k2) == 1 and p1 > p2:
        nums.append(p2)
        nums.extend(k1)
        k2.remove(p2)
        matrix.pop(0)
        matrix.pop(0)
        done = True
        matrix_count = False
        matrix.insert(0, nums)
        #return done
    elif len(k2) == 1 and p1 < p2:
        nums.append(p1)
        k1.remove(p1)
        pass
    elif p1 < p2:
        nums.append(p1)
        k1.remove(p1)
        pass
    elif p2 < p1:
        nums.append(p2)
        k2.remove(p2)
        pass
    elif p1 == p2:
        nums.append(p1)
        k1.remove(p1)
        k2.remove(p2)
        pass


print(len(matrix))
print(matrix)
print(done, matrix_count)

while done == False and matrix_count == False:
    merge_left(matrix)

print(len(matrix))
print(matrix)
print(done, matrix_count)