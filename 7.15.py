# 高级变量类型
# 1.集合(无序不重复)
set_1={1,2,3,4,5,1,1,1} #大括号创建
set_2=set([1,3,5,7]) #用列表创建
set_j=set_1 & set_2 #集合的交 &
set_b=set_1 | set_2 #集合的并 |
set_c=set_1 - set_2 #集合的差 -
set_d=set_1 ^ set_2 #集合的对称差 ^(只在一个集合中出现的元素)
# print(set_1)
# print(set_2)
# print(set_j)
# print(set_b)
# print(set_c)
# print(set_d)

# 2.printf的使用
a=1+1
# print(f'元组的长度为：{a}')

# 3.元组（有序不可变）
tuple_1=(1,2,3,4,5,1,1,1) #小括号创建
tuple_2=1,2,3,4,5,1,1,1 #不使用小括号创建
# print(tuple_1)
a,b,*c= tuple_1
# print(f'a={a}')
# print(f'b={b}')
# print(f'c={c}')
b,a=a,b
# print(f'a={a}')
# print(f'b={b}')

# 4.列表（有序可变）
list_1=[1,2,3,4,5,1,1,1] #中括号创建
list_2=list((1,3,5,7)) #用元组创建
list_1.append(6) #列表末尾添加元素
list_1.insert(0,'A') #列表指定位置添加元素
cut=list_1[1:-1:1]
print(list_1)
print(list_1[1])
print(cut)
