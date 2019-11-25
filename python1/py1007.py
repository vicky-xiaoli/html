
# 有这样一个list["a","b","c",1,2,3]，生成一个字典，将字符作为字典的key，数字作为字典的value。结果{'a': 1, 'b': 2, 'c': 3}。

# li = ["a","b","c",1,2,3]
# di = {}
# for i in range(int(len(li)//2)):  #确定循环次数
#     di[li[i]] = li[len(li)//2 + i ]  #根据索引位置的元素确定字典的键和值
# print(di)