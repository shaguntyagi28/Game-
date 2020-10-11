from random import random

wrong_reply = [" dont be silly! ", " Nope - this is not the right answer :( "]

def ask(number, text, ans):
    question = text.split(',')
    if len(question) == 4:
        print("Q" + str(number) + " - " + question[0])
        print("a - " + question[1])
        print("b - " + question[2])
        print("c - " + question[3])
        i = input("-> ").lower()
        if int(ans) == ord(i) - 97:
            print(" correct!! :), you have got the right option! ", end="")
            return 1
        else:
            print(wrong_reply[int(random() * 2)])
    return 0


if __name__ == "__main__":
    print("\n\n\nWelcome to the most interesting quiz, The ShinChan Quiz\n")
    question_data = ""
    answers = ""
    
    with open("question-data.csv") as f:
        question_data = f.readlines()

    with open("answer-data.csv") as f:
        answers = f.readlines()
    
    l = len(question_data)
    resp = 0
    for i in range(l):
        resp = ask(i+1, question_data[i], answers[i])
        if resp == 0: break
        if i < l-1: print(" Moving ahead\n")
    
    if resp == 1:
        print("\nCongratulations you completed the game successfully! :) :)")
    else:
        print("The game has been terminated")