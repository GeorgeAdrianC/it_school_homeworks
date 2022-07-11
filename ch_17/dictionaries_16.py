import copy


a =[[1,2], [3,4]]
b = copy.deepcopy(a)

for i in range(len(a)):
    if isinstance(a[i], list):
        for j in range(len(a[i])):
            print(a[i][j] == b [i][j])
