import Q2_2
import Q2_3
import Q3_1_a
import Q3_1_b
import Q3_2

options = ["Question 2.2 (Q2_2)", "Question 2.3 (Q2_3)", "Question 3.1 a (Q3_1_a)", "Question 3.1 b (Q3_1_b)", "Question 3.2 (Q3_2)", "Exit"]

while True:
	print("\n========================================")
	print("62760858 - COS4861 - Assignment 1 - 2021")
	print("========================================\n")
	print("Please enter the question you wish to run: (e.g. Q2_2)")
	for option in options:
		print(">> " + option)
	questionNumber = input(":: ").upper()
	print()

	if questionNumber == "EXIT":
		break
	elif questionNumber == "Q2_2":
		Q2_2.main()
	elif questionNumber == "Q2_3":
		Q2_3.main()
	elif questionNumber == "Q3_1_A":
		Q3_1_a.main()
	elif questionNumber == "Q3_1_B":
		Q3_1_b.main()
	elif questionNumber == "Q3_2":
		Q3_2.main()
	else:
		print("Error: Invalid input")