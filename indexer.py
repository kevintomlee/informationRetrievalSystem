import os
from os import listdir
from os.path import isfile, join

from collections import defaultdict

from document import *
from postings import Posting

class Indexer:
	"""
	@Author: Xiang
	1: Constrcut a term dictionary
	2: Building postings lists for each term in the dictionary
	3: For each term in each document, build document vector(calculate term frequency of each term)
	"""

	vocabulary = set()
	"""
	Dictionary format:
	a dictionary of lists
	term -> list
	each list should be total documents number long(the list is a list of lists)
	list format : [[tf, docid], [tf, docid], ...]
	"""
	dictionary = defaultdict()
	numberOfDoc = 0
	#dictionary['one'] = [1,2,3,4]
	filePath = ""

	"to be added"
	puctuations = (',', '!')

	def __init__(self, path):
		"""
		Constructor:
		Building the index adn store the information in a file
		"""
		filePath = path
		self.indexing(filePath)


	def read_file(self, filename):
		"""
		Read one file and return the content as a list of lines
		"""
		lines = []
		f = open(filename, 'r')
		for line in f:
			lines.append(line)
		f.close()
		return lines

	def get_files(self, path):
		"""
		Get all file name in the specifed directory
		"""
		files = []
		for name in os.listdir(path):
			if os.path.isfile(os.path.join(path, name)):
				files.append(os.path.join(path, name))
		self.numberOfDoc = len(files)
		return files

	def tokenization(self, line):
		"""
		Rules: 
		1: 
		2: Remove .
		3: To lower case
		4: Remove spaces and newlines, convert to term
		"""
		line = line.replace(r'.', ' ')
		line = line.lower()
		tokens = line.split()
		return tokens

	def normalization(self, word):
		"Rules: "
		return word

	def get_stop_words(self, filename):
		"""
		The file should contain one word per line,
		remove words from the list that appear in the dictionary
		"""
		return read_file(filename)

	def stemming(self):
		None

	def indexing(self, path):
		#build vocabulary
		files = self.get_files(path)
		docid = 0
		for docfile in files:
			Document(docfile, docid, docfile)
			## term frequency
			tf = dict()
			for line in self.read_file(docfile):
				for token in self.tokenization(line):
					if token not in tf:
						tf.setdefault(token, 1)
					else:
						tf[token] += 1
					self.vocabulary.add(self.normalization(token))
					if token not in self.dictionary:
						# parse document to term-docName pair
						self.dictionary.setdefault(token, []).append([1, docfile])
					else:
						posting = self.dictionary[token]
						added = False
						for pair in posting:
							if pair[1] == docfile:
								pair[0] += 1
								added = True
								break
						if not added:
							posting.append([1, docfile])
							#else:
							#	posting.append([1, docfile])
								
			#Document("", docid, docfile, doclength)
			#for term in iter(tf):
			#	for docPairs in self.dictionary[term]:
					#print(postings[term])
			#		if [1, docfile] in docPairs:
			#			docPairs = tf[term]
					

				

			#print(tf)

	def writeToFile(self, filename):
		#write dictionary to a text file with name filename
		file = open(filename, 'w')
		file.write(str(self.dictionary))
		file.close()


		

