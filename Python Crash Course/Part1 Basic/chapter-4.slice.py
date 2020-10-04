myList = range(1000)

print(min(myList))
print(max(myList))

'''
# python列表的切片，格式如：
# list[start_index:end_index:step]，其中：
# start_index含，
# end_index不含
# step只能是非0整数，如果为正则正向取值，为负则反向取值
# 测试下来可知
如果start_index的实际位置比end_index前，则step必须为正数，否则结果为空
反之，则step必须为负数，否则结果为空.
'''
#如期望输出
print(list(myList[-1:10:-2]))
#无法输出
print(list(myList[-1:10:2]))

#如期望输出
print(list(myList[10:-1:2]))