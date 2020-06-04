# msg = '''------------ info of 太白金星  -----------
# Name  : 太白金星
# Age   : 18
# job   : Teacher
# Hobbie: girl
# ------------- end -----------------'''

# msg1 = '''------------ info of 德刚  -----------
# Name  : 德刚
# Age   : 73
# job   : Teacher
# Hobbie: boy
# ------------- end -----------------'''

# 制作一个公共的模板
# 让一个字符串的某些位置变成动态可传入的。
# 格式化输出
# name = input('请输入你的姓名：')
# age = input('请输入你的年龄：')
# job = input('请输入你的工作：')
# hobby = input('请输入你的爱好：')
# # % 占位符  s --> str  d  i  r
# msg = '''------------ info of %s  -----------
# Name  : %s
# Age   : %d
# job   : %s
# Hobbie: %s
# ------------- end -----------------''' % (name, name, int(age), job, hobby)
# print(msg)


# 坑：在格式化输出中，% 只想表示一个百分号，而不是作为占位符使用
msg = '我叫%s,今年%s,学习进度1%%' % ('太白金星', 18)
print(msg)