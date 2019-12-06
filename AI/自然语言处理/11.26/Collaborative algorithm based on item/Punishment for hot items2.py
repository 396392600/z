import math
def ItemSimilarity_alpha(train,alpha=0.3):
    C = dict() ##被购买的次数
    N = dict() ##被购买⽤户数
    for u,items in train.items():
        for i in items.keys():
            if i not in N.keys():
                N[i]=0
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i]=dict()
                if j not in C[i].keys():
                    C[i][j]=0
                ##当⽤户同时购买了i和j，则加1
                C[i][j] += 1
    W = dict() ##相似分数
    for i,related_items in C.items():
        if i not in W.keys():
            W[i]=dict()
        for j,cij in related_items.items():
            W[i][j] = cij / (math.pow(N[i],alpha)*math.pow(N[j],1-alpha) )
    return W

def Recommend(train,user_id,W,K):
    rank = dict()
    ru = train[user_id]
    for i,pi in ru.items():
        tmp=W[i]
        for j, wj in sorted(tmp.items(), key=lambda d: d[1], reverse=True)[0:K]:
            if j not in rank.keys():
                rank[j] = 0
            ##r如果⽤户已经购买过，则不再推荐
            if j in ru:
                continue
            ##待推荐的物品j与⽤户已购买的物品i相似，则累加上相似分数
            rank[j] += pi * wj
    return rank


if __name__ == '__main__':
    Train_Data = {
        'A': {
            '苹果': 1, '⾹蕉': 1, '⻄⽠': 1
        },
        'B': {'苹果': 1, '⻄⽠': 1},
        'C': {'苹果': 1, '⾹蕉': 1, '菠萝': 1},
        'D': {'⾹蕉': 1, '葡萄': 1},
        'E': {'葡萄': 1, '菠萝': 1},
        'F': {'⾹蕉': 1, '⻄⽠': 1}
    }
    W = ItemSimilarity_alpha(Train_Data)
    print(Recommend(Train_Data, 'C', W, 3))