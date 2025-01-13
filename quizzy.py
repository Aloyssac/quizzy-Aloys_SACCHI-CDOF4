import time
import threading

def display_intro():
    print("\nWelcome to the Bitcoin Quiz!")
    print("Answer 7 questions correctly to win the game.")
    print("You have 30 seconds to answer each question.")
    print("Good luck!\n")
    time.sleep(1)

def timer(stop):
    for i in range(30, 0, -1):
        if stop():
            break
        time.sleep(1)
    if not stop():
        print("\nTime's up!")

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    stop_timer = False
    timer_thread = threading.Thread(target=timer, args=(lambda: stop_timer,))
    timer_thread.start()

    answer = None
    while answer is None and timer_thread.is_alive():
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                stop_timer = True
            else:
                print("Please enter a number between 1 and 4.")
                answer = None
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
        except EOFError:
            # This handles the case when input is interrupted
            break
    
    stop_timer = True
    timer_thread.join()  # Wait for the timer thread to finish
    
    if answer is None:
        return False
    
    return answer == correct_option

def main():
    display_intro()

    questions = [
        ("Who created Bitcoin?", ["Elon Musk", "Satoshi Nakamoto", "Vitalik Buterin", "Charlie Lee"], 2),
        ("What year was Bitcoin created?", ["2005", "2009", "2011", "2013"], 2),
        ("What is the maximum supply of Bitcoin?", ["21 million", "42 million", "100 million", "Unlimited"], 1),
        ("What is the smallest unit of Bitcoin?", ["MilliBitcoin", "MicroBitcoin", "Satoshi", "Bit"], 3),
        ("What technology underpins Bitcoin?", ["Blockchain", "Artificial Intelligence", "Cloud Computing", "Quantum Computing"], 1),
        ("What is Bitcoin's consensus mechanism?", ["Proof of Stake", "Proof of Work", "Delegated Proof of Stake", "Byzantine Fault Tolerance"], 2),
        ("What is the name of Bitcoin's first block?", ["Genesis Block", "Master Block", "Alpha Block", "First Block"], 1),
    ]

    score = 0

    for i, (question, options, correct_option) in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        if ask_question(question, options, correct_option):
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")
        time.sleep(1)

    print(f"You answered {score} out of 7 questions correctly.")

    if score == 7:
        print("Congratulations! You are a Bitcoin expert!")
    elif score >= 4:
        print("Good job! You have some knowledge about Bitcoin.")
    else:
        print("Better luck next time! Keep learning about Bitcoin.")

if __name__ == "__main__":
    main()
