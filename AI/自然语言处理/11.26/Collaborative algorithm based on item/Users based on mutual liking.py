##ItemCF算法
import math
def ItemSimilarity(train):
    C = dict() ##同时被购买的次数
    N = dict() ##购买⽤户数
    for u,items in train.items():
        for i in items.keys():
            if i not in N.keys():
                N[i] = 0
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i] = dict()
                if j not in C[i].keys():
                    C[i][j] = 0
                ##当⽤户同时购买了i和j，则加1
                C[i][j] += 1
    W = dict() ##相似分数
    for i, related_items in C.items():
        if i not in W.keys():
            W[i] = dict()
        for j,cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i]*N[j])
    return W

if __name__ == '__main__':
    Train_Data = {
        'A':{'苹果':1,'⾹蕉':1,'⻄⽠':1},
        'B':{'苹果':1,'⻄⽠':1},
        'C':{'苹果':1,'⾹蕉':1,'菠萝':1},
        'D':{'⾹蕉':1,'葡萄':1},
        'E':{'葡萄':1,'菠萝':1},
        'F':{'⾹蕉':1,'⻄⽠':1}
    }
    W = ItemSimilarity(Train_Data)
    print(W)
