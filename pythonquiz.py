# quiz.py

from string import ascii_lowercase

QUESTIONS = {
    "How do you say Apple in French?": [
        "pomme", "monde", "mela", "rouge"
    ],
    "How do you say red in French?": [
        "rouge",
        "blanc",
        "nombre",
        "rosso",
    ],
    "How do you say white in French?": [
        "blanc", "rouge", "bianco", "champagne"
    ],
}

#Keep track of how many questions the user answers correctly
num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("? Correct! ?")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")

