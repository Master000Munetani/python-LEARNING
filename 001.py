from pickle import TRUE
from syslog import LOG_SYSLOG


print("hello world")
# 这个是单行注释(一般在#后空一格再写注释)
# 快捷键 Ctrl+/
'''
这是多行注释
'''

"""
这是另一种多行注释
"""
print("lysnb")  # 简单的注释内容（在代码后空两格写#）

# 注释不管写在哪里都不会执行
# 单行注释通常是对一行代码解释说明
# 多行注释一般是对多行、代码块注释


# 变量名 = 变量值

# 复合单词命名
my_name = "linyishan"  # 下划线
yourName = 2  # 第二个单词后开始首字母大写
HisName = 3  # 从第一个单词开始首字母大写

print("我叫",my_name)


# 检测数据类型--type(数据)

# int -- 整型
num1 = 1

# float -- 浮点型，就是小数
num2 = 1.1

# str -- 字符串类型，引号
a = "jk"

# bool -- 布尔型,T/F,用于判断
b = True

# list -- 列表
c = [10,20,30]

# tuple -- 元组
d = (10,20,40)

# set -- 集合
e = {10,20,30}

# dict -- 字典 -- 键值对
f = {"name":"tom","age":18}

#输出，判断数据类型
print(type(num1))
print(type(num2))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

"""
1.准备数据
2.格式化输出数据
"""

age = 19 
name1 = "lys"
weight = 68.5
stu_id = 1
stu_id1 = 1000

# 1.今年我x岁 -- %d 整数
print("今年我%d岁" % age)

# 2.我的名字是lys -- %s 字符串
print("我的名字是%s" % name1)

# 3.体重是68.5kg -- %f 小数/浮点型
print("体重是%fkg" % weight)
"""
默认保留6位小数
使用 %.nf -- 保留n位小数
"""
print("体重是%.2fkg" % weight)  # 保留2位小数

# 4。我的学号是001
print("我的学号是%d" % stu_id)  # 1
"""
%0nd -- 输出显示的是n位数，
不足则以0补全，超出则原样输出
"""
print("我的学号是%03d" % stu_id)  # 001
print("我的学号是%03d" % stu_id1)  # 超出，原样输出

# 5.我的名字是lys,今年19岁 -- 多个格式化输出
print("我的名字是%s,今年%d岁" %(name1,age))  # %(),内部以逗号隔开
print("我的名字是%s,明年%d岁" %(name1,age + 1))  # 可以对变量加减操作

# 6.我的名字是lys,今年19岁，体重68.5kg，学号是001
print("我的名字是%s,今年%d岁，体重%.2fkg，学号是%03d" %(name1,age,weight,stu_id))