import itertools

a=list(input().split())
a[0]=sorted([*a[0]])
b=list(itertools.permutations(a[0],int(a[1])))

for c in b:
    temp=''
    for d in c:
        temp+=d
    print(temp)

"""PROBLEM DESCRIPTION TO BE ADD"""
