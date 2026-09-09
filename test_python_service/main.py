from langchain import ask_question

def main():
    question = "What is the capital of France?"
    answer = ask_question(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")


if __name__ == "__main__":
    print("Hello, World!")