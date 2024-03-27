import random

questions = [
    {
        "prompt": "The Eiffel Tower is located in which country?",
        "options": ["a) Italy", "b) Spain", "c) France", "d) Germany"],
        "answer": "c"
    },
    {
        "prompt": "Which country is known for the Great Wall?",
        "options": ["a) China", "b) Russia", "c) India", "d) Brazil"],
        "answer": "a"
    },
    {
        "prompt": "Which country is famous for its maple syrup?",
        "options": ["a) Japan", "b) Canada", "c) Sweden", "d) Brazil"],
        "answer" : "b"
    },
    {
        "prompt": "Which country is known for its kangaroos and koalas?",
        "options": ["a) South Africa", "b) Australia", "c) Argentina", "d) Peru"],
        "answer": "b"
    }, 
    {
        "prompt": "Where is the Statue of Liberty located?",
        "options": ["a) United Kingdom", "b) United States", "c) France", "d) Italy"],
        "answer": "b"
    }
]

def run_quiz(questions):
    score = 0
    print("Country Quiz Time!\nThere are a total of 5 marks!\n Good Luck!\n")
    
    # Randomize the order of questions
    random.shuffle(questions)
    
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        # User input validation
        while True:
            answer = input("Enter your answer (a, b, c, or d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid input. Please enter a valid option (a, b, c, or d).\n")
        
        if answer == question["answer"]:
            print("Correct! \n")
            score += 1
        else:
            print("Not correct!", "\nThe answer is ", question["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)
