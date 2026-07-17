# 1.函数
# 函数可以吞吐不定个数的参数
def menu(*arg):
    "'菜单'"
    return arg
ex_arg=menu('a',1)
# print(ex_arg)

# 吞吐普通参数+仅一个任意数量的参数
def menu_1(a,b,*arg):
    "'菜单_1'"
    return a,b,arg
ex_arg_1=menu_1('a',1,2,3,4)
# print(ex_arg_1)

# 吞吐普通参数+仅一个任意数量的键值对参数
def trans(a,b,**arg):
    "'键值对参数函数'"
    arg['in_1']=a
    arg['in_2']=b
    return arg
ex_trans=trans(1,2,c=3,d=4,e=5)
# print(ex_trans)

# *和**解包/打包(示例)
# # 1. 定义处：收
# def order(main, *extras, **info):
#     print(main, extras, info)
# # 2. 调用处：发
# foods = ['煎蛋', '火腿']
# beizhu = {'辣度': '微辣'}
# order('牛肉面', *foods, **beizhu)
# # 牛肉面 ('煎蛋', '火腿') {'辣度': '微辣'}
# # 3. 转发：收完再发（装饰器的核心套路）
# def log(*args, **kwargs):
#     print('--- 收到订单 ---')
#     order(*args, **kwargs)
# log('牛肉面', *foods, **beizhu)
# # 4. 函数外：拆包与合并
# first, *rest = foods          # first='煎蛋', rest=['火腿']
# combo = [*foods, '可乐']       # ['煎蛋', '火腿', '可乐']
# menu = {**{'a': 1}, **beizhu} # {'a': 1, '辣度': '微辣'}
# print(*foods)                 # 煎蛋

# 2.类