from Q2_2 import MinimumEditDistanceCalculator
import re
from Q3_1_a import NGram
from Q3_1_b import NGramStatistics
from Q3_2 import LaplaceNGram

options = ["Question 2.2 (Q2_2)", "Question 2.3 (Q2_3)", "Question 3.1 a (Q3_1_a)", "Question 3.1 b (Q3_1_b)", "Question 3.2 (Q3_2)", "Exit"]

while True:
	print()
	print("===== 62760858 COS4861 Assignment 01 2021 =====")
	print("Please enter the question you wish to run: (e.g. Q2_2)")
	for option in options:
		print(">> " + option)
	questionNumber = input(":: ").upper()
	print()

	if questionNumber == "EXIT":
		break
	elif questionNumber == "Q2_2":
		# Handle basic I/O
		print("### Levenshtein Distance Calculator ###")
		Target = input("Please enter the Target string: ")
		Source = input("Please enter the Source string: ")
		print()

		# Calculate and display the Minimum Edit Distance between Target and Source
		MinimumEditDistanceCalculator = MinimumEditDistanceCalculator()
		MinimumEditDistanceCalculator.CalculateDistance(Target, Source)
	elif questionNumber == "Q2_3":
		# First, let's specify our patterns and substitutions in a list of tuples
		expressions = [
			# Change I'M and I AM to YOU ARE
			(r"\b(I\'M|I AM)\b", "YOU ARE"),

			# Change I and ME to YOU
			(r"\b(I|ME)\b", "YOU"),

			# Change MY to YOUR
			(r"\b(MY)\b", "YOUR"),

			# We want to simulate the example given, so we need to handle this special case
			# by removing Well, from the start of a sentence.
			(r"^(WELL,) ", ""),

			# If we have previously replaced I'M|I AM DEPRESSED|SAD, then
			# add some sincerity
			(r".*\bYOU ARE (DEPRESSED|SAD)\b.*",
			r"I AM SORRY TO HEAR YOU ARE \1"),
			(r".*\bYOU ARE (DEPRESSED|SAD)\b.*",
			r"WHY DO YOU THINK YOU ARE \1"),

			# If we encounter ALL, then replace the entire sentence with IN WHAT WAY
			(r".*\bALL\b.*", "IN WHAT WAY"),

			# If we encounter ALWAYS, then replace the entire sentence with
			# CAN YOU THINK OF A SPECIFIC EXAMPLE
			(r".*\bALWAYS\b.*", "CAN YOU THINK OF A SPECIFIC EXAMPLE"),

			# Respond appropriately when the user is grateful
			(r".*\bTHANKS?(\sYOU)?\b.*", "YOU ARE MOST WELCOME"),
		]

		# Get the next sentence
		sentence = input("You:\t")

		# Convert the user's sentence to uppercase
		sentence = sentence.upper()

		# Only respond if the user doesn't want to leave
		while not(re.match(r".*BYE.*", sentence)):
			# Perform the substitutions in expressions on sentence (in the order listed)
			for regularExpression, replacement in expressions:
				sentence = re.sub(regularExpression, replacement, sentence)

			# Print our response
			print("ELIZA:\t" + sentence.upper())

			# Get the next sentence and convert it to uppercase for the next iteration
			sentence = input("You:\t")
			sentence = sentence.upper()
	elif questionNumber == "Q3_1_A":
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
	elif questionNumber == "Q3_1_B":
		# We'll use the text files from Additional Resources
		# on myUnisa as our corpora 
		# (both have been truncated to exactly 1000 words)
		with open('test1000.txt') as f:
			corpus1 = f.read()
		with open('training1000.txt') as f:
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
	elif questionNumber == "Q3_2":
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
	else:
		print("Error: Invalid input")