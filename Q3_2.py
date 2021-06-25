from Q3_1_a import NGram

# This class augments the NGram class in
# Q3_1_a to perform Laplace Smoothing
class LaplaceNGram(NGram):
	# Override the constructor to initalize V to 0
	# (this is necessary for the special case where Corpus = None)
	def __init__(self, n, corpus = None):
		# Initialize the number of distinct words to 0
		self._v = 0

		# Then call our base constructor
		super(LaplaceNGram, self).__init__(n, corpus)
	
	# Override the CountNGrams method to store the number
	# of distinct words in the corpus in V
	def CountNGrams(self, corpus):
		# Count the N-Grams normally
		super(LaplaceNGram, self).CountNGrams(corpus)

		# Then count the number of distinct words in the corpus
		# by counting the length of the set of all words in the corpus
		self._v = len(set(word for word in str.split(corpus)))

	# Overload the _calculateProbability helper method to calculate
	# Laplace Smoothed probabilities instead of normal probabilities
	def _calculateProbability(self, ngram):
		# First, we count the occurences of
		# our full N-Gram and add 1 to it
		fullCount = self._ngrams[ngram] + 1

		# Now we can count the occurences of
		# our provided history h and add V to it
		historyCount = self._ngrams[ngram[:-1]] + self._v

		# Finally, we calculate P_Laplace(w | h) = (C(hw)+1)/(C(h)+V)
		# See Equation 4.23
		# (note that we return 0.0 if we attempt to perform 0 division)
		return (0.0 if historyCount == 0 else fullCount / historyCount)

def main():
	print("---------------------------------------------------------------")
	print("This program performs Laplace Smoothing on the previous N-Grams")
	print("---------------------------------------------------------------\n")
	
	corpus = '<s> I am Sam </s>\n<s> Sam I am </s>\n<s> I do not like green eggs and ham </s>'

	print('Corpus:\n' + corpus + '\n')

	# Create a bigram object
	ngram = LaplaceNGram(2, corpus)

	print('Some test cases for bigrams (see p.89):')
	print('P(I | <s>) = ' + str(ngram.P('</s> | I am')))
	print('P(Sam | <s>) = ' + str(ngram.P('Sam | <s>')))
	print('P(am | I) = ' + str(ngram.P('am | I')))
	print('P(</s> | Sam) = ' + str(ngram.P('</s> | Sam')))
	print('P(Sam | am) = ' + str(ngram.P('Sam | am')))
	print('P(do | I) = ' + str(ngram.P('do | I')))

	print()

	# Create a unigram object
	ngram = LaplaceNGram(1, corpus)
	print('Some test cases for unigrams:')
	print('P(I) = ' + str(ngram.P('I')))
	print('P(am) = ' + str(ngram.P('am')))
	print('P(Sam) = ' + str(ngram.P('Sam')))
	print('P(the) = ' + str(ngram.P('the')))
	print('P(ham) = ' + str(ngram.P('ham')))

	print()

	# Create a trigram object
	ngram = LaplaceNGram(3, corpus)
	print('Some test cases for trigrams:')
	print('P(Sam | I am) = ' + str(ngram.P('Sam | I am')))
	print('P(am | Sam I) = ' + str(ngram.P('am | Sam I')))
	print('P(eggs | like green) = ' + str(ngram.P('eggs | like green')))
	print('P(ham | like green) = ' + str(ngram.P('ham | like green')))

if __name__ == "__main__":
	main()