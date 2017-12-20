from collections import defaultdict
dic = defaultdict(list)

dic[1].extend([2])
dic[1].extend([4])
dic[2].extend([7])

print(dic)
new = {k: sum(v)/len(v) for k, v in dic.items() if len(v) > 0}
print(new)
new.pop(2)
print(new)
new[1] = [7]
print(new)

lists = [1,2,3,4,5,6,7]

lists.append(3)
print(lists)

dic = {
        1 : [1,2,3,4],
        2 : [5,6,7],
        3 : [10,11,12],
        4 : [8]
}

for k in dic.iterkeys():
    print(k)

x = [k for k, v in dic.iteritems() if 6 in v]

min_value = min(dic.values())
min_list = [key for key, value in dic.items() if value == min_value]

min = 300
for keys in dic:
    x = len(dic[keys])
    if x < min:
        min = x
        list = dic[keys]
        key = keys  

print('list: ', list)
print('key: ', key)
print('min: ', min)

for i in range(len(lists) - 1):
    if 3 == lists[i]:
        del lists[i]

print(lists)


