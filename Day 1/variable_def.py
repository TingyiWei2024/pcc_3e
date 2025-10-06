print("Hello Python world!")

# 变量与赋值

glass = 'water'
print(glass)

glass = input("请输入你想喝的饮料：")
print(glass)

# 变量命名规则

# 变量名只能包含字母、数字和下划线。
# 变量名只能以字母或下划线开头。
# 变量名不能包含空格。
# 变量名不能与Python的关键字相同。


glass1 = input("请输入你想喝的饮料1:")
glass2 = input("请输入你想喝的饮料2:")
print(glass1)
print(glass2)

temp = glass1
glass1 = glass2
glass2 = temp
print(glass1)
print(glass2)

name = input("请输入你的名字:")
passwoed = input("请输入你的密码:")
gender = input("请输入你的性别:")
age = input("请输入你的年龄:")
print(name, passwoed, gender, age)