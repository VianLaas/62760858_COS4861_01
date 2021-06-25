from Q3_1_a import NGram

# This class adds a feature to NGram from Q3_1_a
# that will print the most common N-Grams in the corpus
class NGramStatistics(NGram):
	# Once our constructor has been called, we
	# now have access to the _ngrams dictionary
	# which contains a count of all the N-Grams
	def __init__(self, n, corpus):
		super(NGramStatistics, self).__init__(n, corpus)

	def PrintTop50NGrams(self):
		# Remove all tuples in _ngrams of length
		# less than self._n
		tempDict = dict()
		for ngram in self._ngrams:
			if len(ngram) == self._n:
				tempDict[ngram] = self._ngrams[ngram]

		self._ngrams = tempDict
		
		# Now print the table
		print("{: <40}| {: <5}".format("N-GRAM", "COUNT"))
		print("-" * 47)
		for ngram in sorted(self._ngrams, key = self._ngrams.get, reverse = True)[:51]:
			print("{: <40}| {: <5}".format(ngram[0] + ("" if len(ngram) == 1 else " " + ngram[1]), str(self._ngrams[ngram])))

def main():
	print("-------------------------------------------------------------")
	print("This program compares N-Gram statistics for two small corpora")
	print("-------------------------------------------------------------\n")
	
	# We'll use the text files from Additional Resources
	# on myUnisa as our corpora 
	# (both have been truncated to exactly 1000 words)
	with open('.\\test1000.txt') as f:
		corpus1 = f.read()
	with open('.\\training1000.txt') as f:
		corpus2 = f.read()

	# Let's start with Unigrams first
	print("================== UNIGRAMS ==================")
	print()

	# Create our unigram objects
	ngram1 = NGramStatistics(1, corpus1)
	ngram2 = NGramStatistics(1, corpus2)

	# Print the output
	print("Corpus: test1000.txt")
	ngram1.PrintTop50NGrams()
	print()
	print("Corpus: training1000.txt")
	ngram2.PrintTop50NGrams()

	# Next, we handle Bigrams
	print()
	print("================== BIGRAMS ==================")
	print()

	# Reassign our bigram objects using polymorphism
	ngram1 = NGramStatistics(2, corpus1)
	ngram2 = NGramStatistics(2, corpus2)

	# Print the output
	print("Corpus: test1000.txt")
	ngram1.PrintTop50NGrams()
	print()
	print("Corpus: training1000.txt")
	ngram2.PrintTop50NGrams()

if __name__ == "__main__":
	main()