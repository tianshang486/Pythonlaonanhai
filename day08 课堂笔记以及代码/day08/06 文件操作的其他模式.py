# 读并追加  # 顺序不能错误。
# f = open('文件的读写', encoding='utf-8', mode='r+')
# content = f.read()
# print(content)
# f.write('人的一切痛苦，本质都是对自己无能的愤怒。')
# f.close()

# 错误示例：
# f = open('文件的读写', encoding='utf-8', mode='r+')
# f.write('人的一切痛苦,,,本质都是对自己无能的愤怒,,,')
# content = f.read()
# print(content)
# f.close()