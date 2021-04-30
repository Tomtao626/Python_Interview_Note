四种Python 列表反转显示方法
第一种，使用reversed 函数，reversed返回的结果是一个反转的迭代器，我们需要对其进行 list 转换

listNode = [1,2,3,4,5]
newList = list(reversed(listNode))
print(newList)


#结果
[5,4,3,2,1]
第二种，使用sorted函数，sorted是排序函数，它是对一个列表进行排序后生成一个新的list列表，而sort则是在原来的列表上直接进行排序。

listNode = [1,2,3,4,5]
newList = sorted(listNode,reverse = True)
print(newList)


#结果
[5,4,3,2,1]
其中，reverse是排序规则，True表示按降序排列，False表示按升序进行排序，False是默认值。

第三种，使用切片技术

listNode = [1,2,3,4,5]
li = listNode[::-1]
print(li)


#结果
[5,4,3,2,1]
切片的格式 [0:3:1]，其中下标0 指的是序列的第一个元素(左边界)，下标3可以指是切片的数量(右边界)，参数1表示切片的步长为1，如果是-1则表示从右边开始进行切片且步长为1。切片不包括右边界下标。

[ : ]表示获取序列所有的元素，省略步长则会默认步长为1。　　

第四种，使用循环，递归

listNode = [1,2,3,4,5]
new=[]
head=listNode  
while head!=None:  
    new.append(head.val)  
    head=head.next  
new.reverse()  
print(new)
def getLists(self,listNode):

    if listNode is None:
        return []
    l = self.getLists(listNode.next)
　　 return l + [listNode.val] 
lists = [1,2,3,4,5] 
getLists(lists)
其中，+ 连接多个小的列表，最后组成一个全新的大列表，相当于使用多个值或列表新建一个列表，比如存在列表 l = [1,2]，我们运行 l = l + [3] 时l结果就是 [1,2,3]。

另外append也是将某值添加到列表中，但append相当于修改列表，比如我们执行 l.append([3]) 时，列表的结果就会是 [1,2,[3]]。