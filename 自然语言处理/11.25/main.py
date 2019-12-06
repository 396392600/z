import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

#导入movie review数据
if __name__ == '__main__':
    positive_fileids = movie_reviews.fileids('pos')
    negative_fileids = movie_reviews.fileids('neg')

#定义一个函数，用来提取特征数据
def extract_features(word_list):
    return dict([(word,True) for word in word_list])

#将语料库中的数据通过刚才定义的函数提取出来
features_positive =[(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in positive_fileids]
features_negative =[(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in negative_fileids]

#将数据分成训练数据和测试数据
threshold_factor = 0.8
threshold_positive =int(threshold_factor*len(features_positive))
threshold_negative =int(threshold_factor*len(features_negative))
features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] +features_negative[threshold_negative:]

#使用朴素贝叶斯分类器训练
classifier = NaiveBayesClassifier.train(features_train)
print ("\nAccuracy of the classifier:",
nltk.classify.util.accuracy(classifier, features_test))

#分类器对象中存有从训练数据中获取的对语义最有影响的单词，将其输出
print ("\nTop 10 most informative words:")
for item in classifier.most_informative_features()[:10]:
    print (item[0])

#输入文本
input_reviews = ["It is an amazing movie",
                 "This is a dull movie. I would never recommend it to anyone.",
                 "A complete and utter destruction of one of the most iconic superheroes. "
                 "0.1 effort and thought put into the storyline. "
                 "A coming of age awkward teenage movie with a'spiderman' stamp put on it. "
                 "Bad jokes aimed at teenagers (abest). "
                 "A complete caricature of a villain,a complete caricature of a Spiderman. "
                 "Just please stop making this garbage Put some god damn effort! "
                 "A total waste of time",
                 "Just staving off some negative reviews. "
                 "Fits well into the Marvel movies to date and is an excellent follow up to Avengers: Endgame."]

#用前面训练出的分类器预测文本的分类
print ("\nPredictions:")
for review in input_reviews:
    print ("\nReview:", review)
    probdist =classifier.prob_classify(extract_features(review.split()))
    pred_sentiment = probdist.max()
    print ("Predicted sentiment:", pred_sentiment )
    print ("Probability:",
round(probdist.prob(pred_sentiment), 2))