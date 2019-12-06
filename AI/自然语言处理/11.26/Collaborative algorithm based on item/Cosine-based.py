## ItemCF-余弦算法
import math
def ItemSimilarity_cos(train):
    C = dict() ##同时购买的次数
    N = dict() ##购买⽤户数
    for u, items in train.items():
        for i in items.keys():
            if i not in N.keys():

                N[i] = 0
            N[i] += items[i] * items[i]
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i] = dict()
                if j not in C[i].keys():
                    C[i][j] = 0
                ##当⽤户同时购买了i和j，则加评分乘积
                C[i][j] += items[i] * items[j]
    W = dict()  ##相似分数
    for i, related_items in C.items():
        if i not in W.keys():
            W[i] = dict()
        for j, cij in related_items.items():
            W[i][j] = cij / (math.sqrt(N[i])* math.sqrt(N[j]))
    return W

if __name__ == '__main__':
    Train_Data = {
        'A': {'苹果': 2, '⾹蕉': 2, '⻄⽠': 2},
        'B': {'苹果': 2, '⻄⽠': 2},
        'C': {'苹果': 2, '⾹蕉': 2, '菠萝': 2},
        'D': {'⾹蕉': 2, '葡萄': 2},
        'E': {'葡萄': 2, '菠萝': 2},
        'F': {'⾹蕉': 2, '⻄⽠': 2}
    }
    W = ItemSimilarity_cos(Train_Data)
    print(W)