questions = ("Which data structure uses LIFO (Last In First Out) principle?: ",
             "Which planet is known as the 'Red Planet'?: ",
             "Which macronutrient is the body’s primary source of energy?: ",
             "What is the default value of a boolean variable in Java?: ",
             "If A = 1, B = 2, ..., Z = 26, what does the word “CAB” equal?: ")

options = (("A) Queue", "B) Array", "C) Stack", "D) LinkedList"),
           ("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),
           ("A) Protein", "B) Fat", "C) Carbohydrate", "D) Fiber"),
           ("A) true", "B) 1", "C) 0", "D) false"),
           ("A) 6", "B) 9", "C) 12", "D) 5"))

answers = ("C", "B", "C", "D" ,"B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("----------------------------")
print("----------RESULTS-----------")
print("----------------------------")

print("answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()


score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")