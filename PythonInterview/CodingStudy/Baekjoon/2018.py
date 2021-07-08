## https://www.acmicpc.net/problem/2018

num_list = [i for i in range(1,int(input())+1)]
#print(num_list[-1])
left = 0
right = 0
result = 0

while left <= right and right < num_list[-1]:
    sums = sum(num_list[left: right+1])
    #print(num_list[left:right+1], sums)
    if sums < num_list[-1] :
        right +=1

    elif sums > num_list[-1]:
        left += 1

    else:
        result += 1
        left += 1
        right = left


print(result)