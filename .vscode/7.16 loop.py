# for 循环
# for i in range(1,10):
#     print(i)

dict_1={'name':'张三','age':18,'sex':'男'}
list_keys=dict_1.keys()
list_variables=dict_1.values()
list_tuple=dict_1.items()
# print(list_tuple) # list_tuple([('name', '张三'), ('age', 18), ('sex', '男')])列表的每个元素是一个tuple
# for k, v in list_tuple:
#     print(f'{k}: {v}') # k,v是元组解胞
# dict_items([('name', '张三'), ('age', 18), ('sex', '男')])
# print(list_keys) #dict_1.keys()返回字典的所有键
# print(list_variables) #dict_1.values()返回字典的所有值
# for k in dict_1: #默认遍历键
#     print(dict_1[k]) 

# dict_1.keys是视图，不支持索引
# 区别于range惰性序列，支持索引，两者均记录规则，不占用大量内存

