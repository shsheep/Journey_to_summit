def rotate(li):
    height, width = len(li), len(li[0])
    ret = [[0] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            ret[x][y] = li[height-1-y][x]
    return ret

def rotate_zero_space(li):
    height = len(li)
    for i in range(height):
        for j in range(1, height):
            li
    
    
    

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for t in a:
    print(t)
ret = rotate(a)
print()
for t in ret:
    print(t)
rotate_zero_space()
a = [[1,2,3],[4,5,6],[7,8,9]]
for t in a:
    print(t)
