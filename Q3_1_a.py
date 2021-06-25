import collections

# This class represents an N-Gram and provides
# the capability to calculate its associated
# Maximum Likelihood Estimation
class NGram:
	# Our constructor specifies N for the N-Gram
	# and its Corpus to be trained on (None by default)
	def __init__(self, n, corpus = None):
		# Initialize N 
		# (Unigram: N = 1, Bigram: N = 2, Trigram: N = 3, etc.)
		self._n = n

		# We will store the tally of all N-Grams in a dictionary
		# (a default dictionary is used because the N-Grams may
		# not exist when we attempt to increment their counts)
		# of key-value pairs (e.g., {..., ('some', 'words'): 4 ,...}).
		# This eliminates the need to manually count
		# duplicates.
		self._ngrams = collections.defaultdict(lambda: 0)

		if corpus is not None:
			# Count all distinct N-Grams
			# if Corpus is supplied
			self.CountNGrams(corpus)

	# Count the number of distinct N-Grams in Corpus
	# for all lengths up to N
	def CountNGrams(self, corpus):
		# First, let's convert Corpus to a list of words
		# (we assume that Corpus is passed as a string)
		corpus = str.split(corpus)
		
		# The very first element in our dictionary
		# will contain the number of words in our corpus,
		# so that we can handle the special case of unigrams
		# where we need to divide the occurences of a word by
		# the total number of words
		self._ngrams[()] = len(corpus)

		# For every word in Corpus
		for i in range(len(corpus)):
			# For every N-Gram length up to N + 1
			for j in range(1, self._n + 1):
				# Ensure that we can construct an N-Gram with the
				# remaining words
				if i + j <= len(corpus):
					# Construct our N-Gram as a tuple containing our words
					# (we need to convert our N-Gram into a tuple so that
					# it can be hashed and stored in our dictionary)
					ngram = tuple([corpus[k] for k in range(i, i + j)])

					# Increment the count for this N-Gram
					self._ngrams[ngram] += 1

	# Calculate and return the probability of
	# a word w given some history h, or P('w | h')
	# E.g. P('the | its water is so transparent that')
	def P(self, input):
		# First, let's extract w and h from our Input
		input = str.split(input)
		w = input[0]
		h = input[2:]

		# Now we concatenate w to h to form our list of words
		# in the intended order (e.g. 'its water is so transparent
		# that the')
		words = h + [w]

		if len(words) <= self._n:
			# We can calculate the probablity directly
			return self._calculateProbability(tuple(words))
		else:
			# We need to multiply the probabilities
			# of all possible N-Grams we can form with Words
			p = 1

			for i in range(len(words) - self._n + 1):
				ngram = tuple(words[i:i + self._n])
				p *= self._calculateProbability(ngram)

			return p

	# A helper method to calculate the probability
	# for a given N-Gram (ngram is assumed to be a tuple)
	def _calculateProbability(self, ngram):
		# First, we count the occurences of
		# our full N-Gram
		fullCount = self._ngrams[ngram]

		# Now we can count the occurences of
		# our provided history h
		historyCount = self._ngrams[ngram[:-1]]

		# Finally, we calculate P(w | h) = C(hw)/C(h)
		# See Equation 4.14
		# (note that we return 0.0 if we attempt to perform 0 division)
		return (0.0 if historyCount == 0 else fullCount / historyCount)
def main():
	print("-----------------------------------------------------")
	print("This program computes unsmoothed unigrams and bigrams")
	print("-----------------------------------------------------\n")
	
	corpus = '<s> I am Sam </s>\n<s> Sam I am </s>\n<s> I do not like green eggs and ham </s>'

	print('Corpus:\n' + corpus + '\n')

	# Create a bigram object
	ngram = NGram(2, corpus)

	print('Some test cases for bigrams (see p.89):')
	print('P(I | <s>) = ' + str(ngram.P('</s> | I am')))
	print('P(Sam | <s>) = ' + str(ngram.P('Sam | <s>')))
	print('P(am | I) = ' + str(ngram.P('am | I')))
	print('P(</s> | Sam) = ' + str(ngram.P('</s> | Sam')))
	print('P(Sam | am) = ' + str(ngram.P('Sam | am')))
	print('P(do | I) = ' + str(ngram.P('do | I')))

	print()

	# Create a unigram object
	ngram = NGram(1, corpus)
	print('Some test cases for unigrams:')
	print('P(I) = ' + str(ngram.P('I')))
	print('P(am) = ' + str(ngram.P('am')))
	print('P(Sam) = ' + str(ngram.P('Sam')))
	print('P(the) = ' + str(ngram.P('the')))
	print('P(ham) = ' + str(ngram.P('ham')))

	print()

	# Create a trigram object
	ngram = NGram(3, corpus)
	print('Some test cases for trigrams:')
	print('P(Sam | I am) = ' + str(ngram.P('Sam | I am')))
	print('P(am | Sam I) = ' + str(ngram.P('am | Sam I')))
	print('P(eggs | like green) = ' + str(ngram.P('eggs | like green')))
	print('P(ham | like green) = ' + str(ngram.P('ham | like green')))

if __name__ == "__main__":
	main()