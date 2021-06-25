import re

def main():
	print("--------------------------------------------------")
	print("This program implements a simplistic ELIZA program")
	print("--------------------------------------------------\n")
	
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

if __name__ == "__main__":
	main()