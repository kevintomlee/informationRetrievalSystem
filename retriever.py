from collections import defaultdict
import math
from operator import itemgetter

class Retriever:
	"""
	The Retriever
	"""
	queryVector = dict()
	scores = dict()
	totalNoDoc = 0

	dictionary = defaultdict()
	def __init__(self, path, N):
		self.totalNoDoc = N

	def processQuery(self, query):
		for term in query.split():
			if term in self.dictionary:
				if term in self.queryVector:
					self.queryVector[term] += 1.0
				else:
					self.queryVector[term] = 1.0
		qlength = 0.0
		for term in self.queryVector:
			qlength += self.queryVector[term]
		for term in self.queryVector:
			self.queryVector[term] /= qlength


	def retriveTopNDocs(self, n):
		None

	## Read the index file into memory
	def readIndexFile(self, filename):
		indexFile = open(filename, 'r')
		s = indexFile.read()
		self.dictionary = eval(s)
		indexFile.close()

	def calculateCosineSimilarity(self):
		length = dict()
		## normailize length for each document
		## result is square root of the sum of each tf's square
		for term in self.dictionary:
			posting = self.dictionary[term]
			for pair in posting:
				tf = float(pair[0])
				if pair[1] in length:
					length[pair[1]] += tf * tf
				else:
					length[pair[1]] = tf * tf
		for term in length:
			length[term] = math.sqrt(length[term])
		#print(length)
		## cosine similarity
		for term in self.queryVector:
			if term in self.dictionary:
				posting = self.dictionary[term]
				df = len(posting)
				idf = math.log(float(self.totalNoDoc)/(float(df) - 1))
				for pair in posting:
					wfd = float(pair[0])/length[pair[1]]
					wfq = self.queryVector[term]
					if pair[1] in self.scores:
						self.scores[pair[1]] += wfd * idf * wfq
					else:
						self.scores[pair[1]] = wfd * idf * wfq
		for doc in self.scores:
			self.scores[doc] /= length[doc]
		return self.scores

	def topNdoc(self, n):
		toplist = []
		sortedlist = sorted(self.scores.items(), key=itemgetter(1), reverse=True)
		#print(sortedlist)
		if n > len(sortedlist):
			n = len(sortedlist)
		for i in range(n):
			toplist.append(sortedlist[i])
		return toplist