import json
from typing import Union
# Match the best response for the inputs we give for chatbot
from difflib import get_close_matches

# Return as a dictionary
def load_knowledge_base(file_path: str) -> dict:
    # Read file
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data
    
def save_knowledge_base(file_path: str, data: dict):
    # Wrote into a file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
# Load Json
def find_best_match(user_question: str, questions: list[str]) -> Union[str, None]:
    # if it is 60% similar
    matches : list = get_close_matches(user_question, questions, n=1, cutoff = 0.6)
    return matches[0]  if matches else None
    
# Get answer
def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
            
def chat_bot():
    print("\nWelcome to ChatBot!")
    print("Type in your question or 'quit' to quit\n")
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    
    while True:
        user_input: str = input('You: ')
        
        if user_input.lower() == 'quit':
            print("ChatBot: Thank you for using ChatBot!")
            break
        
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'ChatBot: {answer}\n')
        else:
            print('ChatBot: Can you teach me how to answer this?')
            new_answer: str = input('Type the answer or "skip" to skip: ')
            
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('ChatBot: Thank you! I learned something new!\n')

if __name__ == "__main__":
    chat_bot()