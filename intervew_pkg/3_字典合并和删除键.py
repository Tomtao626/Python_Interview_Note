# 字典如何删除键和合并两个字典

# del和update方法

dic = {"name": "jack", "age":18}
del dic["name"]  # 删除键
print(dic)

dic2 = {"name": "tom"}
dic.update(dic2)  # update合并
print(dic)