# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

num_list = input().split()
target = int(input())

if str(target) not in num_list:
    print('X')

else:
    n = user_input // 2
    while True:
        if int(num_list[n]) > target:
            n = n - 1
        elif int(num_list[n]) < target:
            n = n + 1
        else:
            print(n + 1)

            break




