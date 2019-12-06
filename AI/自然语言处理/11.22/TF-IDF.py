import pkuseg
import numpy as np
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
seg = pkuseg.pkuseg()

filenames = ["a.txt","b.txt","c.txt"]

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str=content_str+i
    return content_str
if __name__ == "__main__":

    corpus = []
    for name in filenames:

        with open(name,'r',encoding='utf-8') as f:
            str = f.read()
            str = format_str(str)
            str = seg.cut(str)
            corpus.append(" ".join(str))
    vectorizer=CountVectorizer()
#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i 类文本下的词频    
    transformer=TfidfTransformer()
#该类会统计每个词语的tfidf权值    
    tfidf=transformer.fit_transform(vectorizer.fit_transform( corpus))
#第一个fit_transform是计算tf-idf，第二个fit_transform是将 文本转为词频矩阵  
    word=vectorizer.get_feature_names()
     #获取词袋模型中的所有词语  
    weight=tfidf.toarray()
#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf 权重
    for (name, w) in zip(filenames, weight):
        print(name, ": ")
        loc = np.argsort(-w)
        for i in range(5):
            print(i + 1, word[loc[i]], w[loc[i]])

