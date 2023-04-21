"""
Two tuples for questions and answers  instead of List, Set or dictionary.
The touples will store the variables i will need later in the code.

"""

questions = ("What is the highest-grossing R-rated movie of all time?: ",
               "What 1994 crime film revitalized John Travolta's career?: ",
               'In Apocalypse Now, Robert Duvall says, \
               "I love the smell of ___ in the morning.": ',
               'Which Alfred Hitchcock thriller is notorious for \
               its shocking "shower scene"??: ',
               "How many suns does Luke's home planet of \
               Tatooine have in Star Wars?: ")

options = (("A. Joker", "B. Blade", "C. Dark Knight", "D. Django Unchained"),
          ("A. Grease", "B. Two of a kind", "C. Pulp Fiction", "D. A civil action"),
          ("A. Diesel", "B. Napalm", "C. Gun Powder", "D. Rotten eggs"),
          ("A. Notorius!", "B. Frenzy", "C. Marnie", "D. Psycho"),
          ("A. 5", "B. 2", "C. 7", "D. 3"))

"""
4 variables set to the correct values to be used later.
Guesses will be stored in a list and compared against
the correct answers later in the code.
Score is set to 0 by default.
question number is set to  0.

"""


answers = ("A", "C", "B", "D", "B")
guesses = []
score = 0
question_num = 0


"""

Main function that has for a loop to get the questions from the tuple.
Then prints them, we also have a for loop that get the options from the other
tuple and prints them to the terminal. THen we have an input that asks you 
to input A,B,C,D that is corresponding to the guesses.
We also have a if statment that asks if the guess is equal to the 
correct answer and if it's not.

"""

for questions in questions:
    print("...")
    print(question)
    for options in options[question_num]:
       print(option)

    guess = input("PICK ONE (A,B,C,D) THEN PRESS ENTER:").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
    print("CORRECT")
    else:
        print(f"INCORRECT {answers[question_num]} IS THE CORRECT ANSWER!")