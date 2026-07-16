# 1.for 循环
# for i in range(1,10):
#    print(i)
value=[i**3 for i in list(range(1,10)) if i<6]
# print(value)

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

# 2.while循环
i=0
while i<10:
    i+=1
    if i==2:
        continue
    if i==7:
        break
    # print(i)

# 3.变量的转换
# print(set(dict_1.items()))
# dict要搭配zip函数

# 4.zip 函数
dict_2=dict(zip(list(dict_1.values()),list(dict_1.keys())))
# print(dict_2.keys())

# 5.函数的定义(function.__doc__返回函数的说明文档)
# def 函数名（输入参数）:# 同一个函数的输入参数可以是各个类型的变量
#     ‘“函数的说明文档‘“
#     函数体
#     return 返回值
def add(a,b):
    '"两变量相加"'
    c=a+b
    return(c)
# print(add([1],[2]))
# print(add.__doc__)