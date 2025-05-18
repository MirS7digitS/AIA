from core.agent import Agent

def main():
    agent = Agent()
    print("Simulated AI Agent started. Type something to give it experience, or 'exit' to quit.")

    while True:
        user_input = input("You> ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        agent.perceive_and_remember(user_input)
        agent.recall_all()

if __name__ == "__main__":
    main()