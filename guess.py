import random
#to get input from user

def get_guess():
    return list(input("What is your guess?Guess a 3 digit number "))

#to generate the random code

def generate_code():
    digits= [str(num) for num in range(10)]
    #to shuffle the digits from 0 to 9
    random.shuffle(digits)
    #to get the first 3 digits
    return digits[:3]

#to generate clues

def generate_clues(code,user_guess):
    if(code==user_guess):
        return "Hurray!! Code guessed"

    clues=[]

    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")

        elif num in code:
            clues.append("close")

    if clues==[]:
        return ["Nope"]
    else:
        return clues

# Running code logic
print("Welcome to Code Breaker!!")
secret_code=generate_code()
clue_report=[]
while clue_report!="Hurray!! Code guessed":
    guess=get_guess()
    clue_report=generate_clues(guess,secret_code)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)



