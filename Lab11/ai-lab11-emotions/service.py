import random
from math import sqrt, floor

from sklearn import neural_network
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

import pandas as pd

def euclidian_distance(a, b):
    return sqrt(sum([(a[i] - b[i]) ** 2 for i in range(len(a))]))


class Service:
    def __init__(self, train_inputs, train_output, test_inputs, test_output):
        self.train_inputs = train_inputs
        self.train_outputs = train_output
        self.test_inputs = test_inputs
        self.test_outputs = test_output

    def run(self):
        # extract features from words
        # v1: bag of words
        # train = self.bag_of_words(self.train_inputs)
        # test = self.bag_of_words(self.test_inputs)

        # v2: bag of words n-gram
        # train = self.bag_of_words_n_gram(self.train_inputs)
        # test = self.bag_of_words_n_gram(self.test_inputs)

        # v3: Tf-Idf
        train = self.tf_idf(self.train_inputs)
        test = self.tf_idf(self.test_inputs)

        self.supervised(train, test)
        self.unsupervised(train, test)
        self.hybrid(train, test)

    def bag_of_words(self, data_input):
        # transform input data in features
        vectorizer = CountVectorizer(max_features=150)
        vectorizer.fit_transform(self.train_inputs)
        # print('\nBag of Words:\n\t', vectorizer.get_feature_names_out())
        bag = []
        for sentence in data_input:
            feature = vectorizer.transform([sentence]).toarray()
            bag.append(feature.tolist()[0])
        return bag

    def bag_of_words_n_gram(self, data_input):
        # transform input data in features
        vectorizer = CountVectorizer(ngram_range = (2, 2))
        vectorizer.fit_transform(self.train_inputs)
        # print('\nBag of Words n-gram:\n\t', vectorizer.get_feature_names_out())

        bag = []
        for sentence in data_input:
            feature = vectorizer.transform([sentence]).toarray()
            bag.append(feature.tolist()[0])
        return bag

    # Term Frequency-Inverse Document Frequency
    def tf_idf(self, data_input):
        tf_idf_vectorizer = TfidfVectorizer(min_df=0., max_df=1., use_idf=True)
        tf_idf_matrix = tf_idf_vectorizer.fit_transform(self.train_inputs)
        tf_idf = []
        for sentence in data_input:
            feature = tf_idf_vectorizer.transform([sentence]).toarray()
            tf_idf.append(feature.tolist()[0])
        return tf_idf


    def glove(self, data_input):
        # nltk.download('stopwords')
        # nltk.download('punkt')
        # nltk.download('wordnet')
        # nltk.download('omw-1.4')

        #step 3
        word_tokens = []
        i = 0
        for line in data_input:
            words = word_tokenize(line)
            word_tokens.insert(i, words)
            i = i + 1

        #step 4
        stop_words = stopwords.words('english')
        lines_without_stopwords = []
        for line in data_input:
            stop_removed = []
        for line in word_tokens:
            for word in line:
                if word not in stop_words:
                    stop_removed.append(word)
        #print(stop_removed)

        #step 5
        wordnet_lemmatizer = WordNetLemmatizer()
        lines_with_lemmas = []  # stop words contain the set of stop words
        for line in self.train_inputs:
            lem_line = []
        for word in stop_removed:
            lem_line.append(wordnet_lemmatizer.lemmatize(word))
        string = ''
        new_lines = ','.join([str(i) for i in lem_line])

        vec = CountVectorizer(binary=False)  # we cound ignore binary=False argument since it is default
        vec.fit(lem_line)

        #pd.DataFrame(vec.transform(lem_line).toarray(), columns=sorted(vec.vocabulary_.keys()))

        bag = []
        for sentence in data_input:
            feature = vec.transform(lem_line).toarray()
            #feature = vectorizer.transform([sentence]).toarray()
            bag.append(feature.tolist()[0])
        return bag

        print(lem_line)
        return lem_line

    def supervised(self, train, test):
        # neural network prediction
        print('\n\n1.Supervised clustering using ANN')
        classifier = neural_network.MLPClassifier(hidden_layer_sizes=(2,), activation='relu', max_iter=100,
                                                  solver='sgd', verbose=10, random_state=1, learning_rate_init=.01)
        classifier.fit(train, self.train_outputs)
        computed = classifier.predict(test)

        print("\nComputed                Real")
        print("----------------------------------")
        for i in range(len(self.test_inputs)):
            print(computed[i], '            ', self.test_outputs[i])

        print("\nAccuracy:", accuracy_score(self.test_outputs, computed))

    def unsupervised(self, train, test):
        # kmeans prediction
        print('\n\n2. Unsupervised clustering')
        unsupervisedClassifier = KMeans(n_clusters=2)
        unsupervisedClassifier.fit(train)
        computed = unsupervisedClassifier.predict(test)
        real = [1 if self.test_outputs[i] == 'negative' else 0 for i in range(len(self.test_outputs))]
        computed_labels = ['negative' if computed[i] == 1 else 'positive' for i in range(len(computed))]

        print("Computed                Real")
        print("----------------------------------")
        for i in range(len(self.test_inputs)):
            print(computed_labels[i], '            ', self.test_outputs[i])

        print("\nAccuracy:", accuracy_score(real, computed))


    def hybrid(self, train, test):
        print('\n\n3. Hybrid clustering')

        positive = []
        negative = []
        for i in range(len(self.train_inputs)):
            if self.train_outputs[i] == 'positive':
                positive.append(self.train_inputs[i])
            else:
                negative.append(self.train_inputs[i])

        vectorizer_positive = CountVectorizer()
        vectorizer_positive.fit_transform(positive)
        positive_bag = vectorizer_positive.get_feature_names_out()
        #print('Positive bag of words:\n', vectorizer_positive.get_feature_names_out())

        vectorizer_negative = CountVectorizer()
        vectorizer_negative.fit_transform(negative)
        negative_bag = vectorizer_negative.get_feature_names_out()
        #print('Negative bag of words:\n', vectorizer_negative.get_feature_names_out())

        # extract neutral words
        neutral_bag = []
        for word in positive_bag:
            if word in negative_bag:
                neutral_bag.append(word)

        # # transform input data based on specific positive/negative features
        k = 2
        for i in range(len(self.train_inputs)):
            count_pos, count_neg, count_neutral = 0, 0, 0
            words = self.train_inputs[i].split(' ')
            for word in words:
                if word in neutral_bag:
                    count_neutral += k
                elif word in positive_bag:
                    count_pos += k
                elif word in negative_bag:
                    count_neg += k
            train[i].append(count_pos)
            train[i].append(count_neg)
            train[i].append(count_neutral)

        for i in range(len(self.test_inputs)):
            count_pos, count_neg, count_neutral = 0, 0, 0
            words = self.test_inputs[i].split(' ')
            for word in words:
                if word in neutral_bag:
                    count_neutral += k
                elif word in positive_bag:
                    count_pos += k
                elif word in negative_bag:
                    count_neg += k
            test[i].append(count_pos)
            test[i].append(count_neg)
            test[i].append(count_neutral)

        # # kmeans prediction
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(train)
        computed = kmeans.predict(train)
        real = [0 if self.train_outputs[i] == 'negative' else 1 for i in range(len(self.train_outputs))]
        computed_labels = ['negative' if computed[i] == 0 else 'positive' for i in range(len(computed))]

        print("Computed                Real")
        print("----------------------------------")
        for i in range(len(self.train_inputs)):
            print(computed_labels[i], '            ', self.train_outputs[i])

        print("\nAccuracy:", accuracy_score(real, computed))

