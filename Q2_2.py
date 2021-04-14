# This class calculates the Minimum Edit Distance between a Target and a Source
# 62760858_COS4861_01
class MinimumEditDistanceCalculator:
	# The default arguments to our constructor
	# specifies the cost for each action
	# (note there will be no cost for substituting a letter for itself)
	def __init__(self, deleteCost = 1, insertCost = 1, substitutionCost = 2):
		self._deleteCost = 1
		self._insertCost = 1
		self._substitutionCost = 2

	# Calculate the Minimum Edit Distance between Target and Source
	def CalculateDistance(self, target, source):
		target = target
		source = source
		
		# Initialize the lengths of Target and Source
		n = len(target)
		m = len(source)

		# Make life easier for ourselves by specifying the ranges once
		# (note that we won't be accessing the zeroth row/column every time,
		# hence the starting value of 1)
		rows = range(1, m + 1)
		cols = range(1, n + 1)

		# Create and initialize (to 0) the distance matrix: distance[n + 1, m + 1]
		distance = [[0 for i in range(m + 1)] for j in range(n + 1)]

		# Now initialize the zeroth row/column to be the distance from the empty string
		# (keep in mind that the costs are not constant, so we cannot simply count
		# from 0 to len(Target/Source) to initialize the values)

		# First, the upper-left element
		distance[0][0] = 0

		# Next, the rows (note that we need to use DeleteCost)
		for row in rows:
			distance[0][row] = distance[0][row - 1] + self._deleteCost

		# Finally, the columns (we use InsertCost in this case)
		for col in cols:
			distance[col][0] = distance[col - 1][0] + self._insertCost

		# Now that we've initialized the zeroth row/column,
		# we can populate the rest of the distance matrix
		for col in cols:
			for row in rows:
				# Let's calculate our possible values for this cell
				# Note that there is no cost for substituting a letter for itself
				leftValue = distance[col - 1][row] + self._insertCost
				diagonalValue = distance[col - 1][row - 1] + (self._substitutionCost if source[row - 1] != target[col - 1] else 0)
				upperValue = distance[col][row - 1] + self._deleteCost

				# Now we assign the minimum of our three possible values to this cell
				distance[col][row] = min(leftValue, diagonalValue, upperValue)

		# The last row and column represents the Minimum Edit Distance between Target and Source
		print("There is a distance of " + str(distance[n][m]) + " between '" + target + "' and '" + source + "':")

		# Print a neat little table showing our calculations
		buffer = "\t#\t"
		for char in rows:
			buffer += source[char - 1] + "\t"
		print(buffer)
		for row in range(n + 1):
			buffer = ("#" if row == 0 else target[row - 1]) + "\t"
			for col in range(m + 1):
				buffer += str(distance[row][col]) + "\t"
			print(buffer)

# ***** Moved to main.py *****		
# # Handle basic I/O
# print("### Levenshtein Distance Calculator ###")
# Target = input("Please enter the Target string: ")
# Source = input("Please enter the Source string: ")
# print()

# # Calculate and display the Minimum Edit Distance between Target and Source
# MinimumEditDistanceCalculator = MinimumEditDistanceCalculator()
# MinimumEditDistanceCalculator.CalculateDistance(Target, Source)