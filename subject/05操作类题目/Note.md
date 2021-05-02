# x="abc",y="def",z=["d","e","f"]，分别求出 x.join(y) 和 x.join(z) 返回的结果
```python
#join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
x="abc"
y="def"
z=["d","e","f"]
a=x.join(y)
b=x.join(z)
c = a.join("9527")
d = b.join({"test1":1,"k8s":a})
print(a) # dabceabcf
print(b) # dabceabcf
print(c) # 9dabceabcf5dabceabcf2dabceabcf7
print(d) # test1dabceabcfk8s
```


    
