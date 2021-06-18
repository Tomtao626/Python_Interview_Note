# dp
# dp
# 背包问题
# everyone weight
w = [0,1,4,3,1]
# everyone value
p = [0,1500,3000,2000,2000]
# calcute the nums
n = len(w)-1
# the bag weight
m = 4

# in bag nums
x = []
v = 0
# optp[i][j]表示在前i个的物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m+1)] for raw in range(n+1)]

def knapsack_dynamic(w,p,n,m,x):
    # 获取optp[i][j]
    # 物品一件件来
    for i in range(1, n+1):
        # j为子背包的载重量，寻找能够承载物品的子背包
        for j in range(1, m+1):
            # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
            if j>=w[i]:
                # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
                optp[i][j] = max(optp[i-1][j], optp[i-1][j-w[i]]+p[i])
            else:
                optp[i][j] = optp[i-1][j]


    # 递推装入背包的物体，寻找跳变的地方，从最后结果开始地推
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i-1][j]:
            x.append(i)
            j = j-w[i]


    # 返回最大价值，即表格中最后一行最后一列的值
    v = optp[n][m]
    return v

print(f"最大值为:{str(knapsack_dynamic(w,p,n,m,x))}")
print(f"最大索引为:{x}")

