from collections import defaultdict
import math
def defItemIndex(DictUser):
    DictItem = defaultdict(defaultdict)
    ##遍历每个⽤户
    for key in DictUser:
        ##遍历⽤户k的购买记录
        for i in DictUser[key]:
            DictItem[i][key] = [key, DictUser[key][i]]
    return DictItem


def defUserSimilarity(DictItem):
    N = dict()  # ⽤户购买的数量
    C = defaultdict(defaultdict)
    W = defaultdict(defaultdict)
    ##遍历每个物品
    for key in DictItem:
        ##遍历⽤户k购买过的物品
        # print(key,":")
        for x in DictItem[key]:
            i = DictItem[key][x]
            # i[0]表示⽤户的id ，如果未计算过，则初始化为0
            if i[0] not in N.keys():
                N[i[0]] = 0
            N[i[0]] += 1
            ## (i,j)是物品k同时被购买的⽤户两两匹配对
            for j in DictItem[key]:
                if i[0] == j[0]:
                    continue
                if j[0] not in C[i[0]].keys():
                    C[i[0]][j[0]] = 0
                # C[i[0]][j[0]]表示⽤户i和j购买同样物品的数量
                C[i[0]][j[0]] += 1
    for i, related_user in C.items():
        for j, cij in related_user.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W


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
    W = defItemIndex(Train_Data)
    print(defUserSimilarity(W))