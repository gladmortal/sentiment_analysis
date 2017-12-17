# Sentiment Analysis
# Data Created :16 July 2014
# Data Modified : 16 July 2014

import nltk
from nltk.corpus import stopwords
from nltk import tokenize
import nltk.data
import numpy
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk import NaiveBayesClassifier
import pickle



class training_data:
	def training_set(self):
		dictionary = []
		dictionary1 = []
		dictionary2 = []
		sentiment_index = []
		for line in open("train25000.tsv"):
			columns = line.split('\t')
			columns = [x.strip() for x in columns]
			final_data = columns[2] + ',' + columns[3]
			dictionary1.append(columns[2])
			dictionary2.append(columns[3])
			#print phrase
			#sentiment_index.append(columns[3])
		#dictionary = dict(zip(phrase, sentiment_index))
		#print phrase
		#sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		#dictionary = (', '.join('"' + item + '"' for item in dictionary))
		dictionary = zip(dictionary1, dictionary2)
		all_words = set(word.lower() for passage in dictionary for word in word_tokenize(passage[0]))
		all_words_refined = [ i for i in all_words if not i in stopwords.words('english')]
		#print token_sent_refined
		#print all_words
		all_words = all_words_refined
		#print all_words
		#print stopwords.words('english')

		t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in dictionary]
		#print t
		'''
		for x in dictionary:
			tokenize = word_tokenize(x[0])
			for word in all_words:
				if word in tokenize:
					d.update({word:x[1]})
		print d
		'''
		'''

		all_words = set(word.lower() for passage in dictionary for word in word_tokenize(passage[0]))
		#for key in dictionary:
		#	print key
		#	break
		print all_words
		#all_words = set(chain(*[word_tokenize(key[0].lower()) for key in dictionary.items()]))
		#print all_words
		training = [({i:(i in word_tokenize(sentence.lower())) for i in all_words},tag) for sentence, tag in dictionary]
		#training = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in dictionary]

		'''
		classifier = nltk.classify.NaiveBayesClassifier.train(t)
		classifier.show_most_informative_features()
		f = open('my_classifier.pickle', 'wb')
		pickle.dump(classifier, f, -1)
		f.close()
		test_sentence = "This is the best band I've ever heard!"
		test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
		return classifier.classify(test_sent_features)


'''
		#training_data = open("train.tsv", "w+")
		for line in open('train.tsv','r').readlines():
			#hello = {'main': 1}
			hello = {'jack': '4098', 'sape': '4139'}
			#sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
			#phrase_id,sentence_id, phrase, sentiment_index = line.strip().split('\t')
			#if phrase == 'Phrase':
			#	continue
			#for word in phrase.strip().split(' '):
			#fset = [(gender_features(n), g) for (n,g) in names]
			training_set = ([(phrase,sentiment_index,a,b) for phrase,sentiment_index,a,b in str(open('train.tsv','r').readlines()).split(' ')])
			#training_set = ([(phrase, sentiment_index) for phrase,sentiment_index in hello.items()])
			#training_set = [(phrase) sentiment_index]
			print training_set
			train = [(dict(a=1,b=1,c=1), 'y'),(dict(a=1,b=1,c=1), 'x'), (dict(a=1,b=1,c=0), 'y'), (dict(a=0,b=1,c=1), 'x'), (dict(a=0,b=1,c=1), 'y'), (dict(a=0,b=0,c=1), 'y'),(dict(a=0,b=1,c=0), 'x'), (dict(a=0,b=0,c=0), 'x'), (dict(a=0,b=1,c=1), 'y')]  
			print train
			classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
			break
			#return line
'''


f = training_data()
print f.training_set()




