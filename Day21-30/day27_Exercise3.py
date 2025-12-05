#Day27 - Exercise3 KBC

# 1 - Create a program capable of displaying questions to 
# the user like KBC
# 2 - Use List data type to store the questions and their 
# correct answers.
# 3 - Display the final amount the person is taking home 
# after playing the game.

def takewin(a): 
    print("1) Do you wish to take your win?\n"
    "2) Do you want to continue to play?")
    pass
        
win_amt = 0;

print("Welcome to KBC")
input("Press Enter to Play")

q1 = print("What is the capital of India?")
ans1 = input(["A) Navi Mumbai",
            "B) Chennai",
            "C) Delhi", 
            "D) Gorakhpur"]) 
if ans1 == 'c':
    win_amt = win_amt + 1000
    print("Hurray you have won Ruppes", win_amt,"!!")
elif ans1 == 'a' or ans1 == 'b' or ans1 == 'd':
    print("Oops, You Lose"+":(" )
    print("You have won total of", win_amt,"ruppes.")
else:
    print("Invalid Option")


q2 = print("Which is the most sang song in the world?")
ans1 = input(["A) Savage Love", 
            "B) Birthday Song",
            "C) Experience", 
            "D) Shape of You"]) 
if ans1 == 'b':
    win_amt = win_amt + 2000
    print("Hurray you have won Ruppes", win_amt,"!!")
elif ans1 == 'a' or ans1 == 'c' or ans1 == 'd':
    print("Oops, You Lose"+":(" )
    print("You have won total of", win_amt,"ruppes.")
else:
    print("Invalid Option")


q3 = print("Which animal bleeds blue?")
ans1 = input(["A) Horse", 
            "B) Platypus",
            "C) Alligator", 
            "D) Octopus"]) 
if ans1 == 'd':
    win_amt = win_amt + 3000
    print("Hurray you have won Ruppes", win_amt,"!!")
elif ans1 == 'a' or ans1 == 'b' or ans1 == 'c':
    print("Oops, You Lose"+":(" )
    print("You have won total of", win_amt,"ruppes.")
else:
    print("Invalid Option")


q4 = print("Who is the God of war in Greek Mythology?")
ans1 = input(["A) Ares", 
            "B) Posidon",
            "C) Zeus", 
            "D) Medusa"]) 
if ans1 == 'a':
    win_amt = win_amt + 4000
    print("Hurray you have won Ruppes", win_amt,"!!")
elif ans1 == 'b' or ans1 == 'c' or ans1 == 'd':
    print("Oops, You Lose"+":(" )
    print("You have won total of", win_amt,"ruppes.")
else:
    print("Invalid Option")


q5 = print("How much is a byte?")
ans1 = input(["A) 2 bits", 
            "B) 4 bits",
            "C) 6 bits", 
            "D) 8 bits"]) 
if ans1 == 'd':
    win_amt = win_amt + 5000
    print("Hurray you have won Ruppes", win_amt,"!!")
elif ans1 == 'a' or ans1 == 'b' or ans1 == 'c':
    print("Oops, You Lose"+":(" )
    print("You have won total of", win_amt,"ruppes.")
else:
    print("Invalid Option")