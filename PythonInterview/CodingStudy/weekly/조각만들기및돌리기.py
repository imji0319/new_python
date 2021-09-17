import numpy as np
def sol(shapes):
    list = []
    answer = -1
    sha = np.array(shapes)
    x = max(sha[:, 0]) - min(sha[:, 0]) + 1
    y = max(sha[:, 1]) - min(sha[:, 1]) + 1
    ze = np.zeros((x, y))

    if min(sha[:,0]) > 0 :
        sha[:,0] = sha[:,0]-min(sha[:,0])

    if min(sha[:,1]) > 0:
        sha[:,1] = sha[:,1]-min(sha[:,1])

    for j in sha:
        r, c = j
        # print(r,c)
        ze[r, c] = 1

    list.append(ze)
    #print('rotate 패턴')
    list.append(np.rot90(ze))
    list.append(np.rot90(ze,2))
    list.append(np.rot90(ze,3))






    return list



ts1 = [[0, 0], [1, 0], [0, 1], [0, 2]]
ts2 = [[0, 3], [0, 4], [1, 4], [2, 4], [2, 5]]
ts3 = [[4, 0], [4, 1], [5, 1]]



ts22 = sol(ts2)

for i in ts22:
    print(i)