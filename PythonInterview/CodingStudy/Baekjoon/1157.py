## https://www.acmicpc.net/problem/1157


import collections
s1 = input()
s1 = s1.upper()

s_li = []
for i in s1:
    s_li.append(i)

s = collections.Counter(s_li).most_common()

mi = []
mx = 0
for k, n in s:
    if n >= mx:
        mx = n
        mi.append(k)

if len(mi) != 1:
    print('?')
else:
    print(mi[0])

