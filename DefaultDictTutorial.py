import collections

n,m=map(int,input().split())
a=collections.defaultdict(list)
b=[]
for i in range(n):
    a[input()].append(i+1)
for i in range(m):
    b.append(input())

for i in b:
    if a[i]==[]:
        print(-1)
    else:
        print(*a[i])

  """HERE GOES THE PROBLEM DESCRIPTION

SOON TO COME
