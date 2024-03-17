value = input("Do you want to play??")
if value.lower() != "yes":
    quit()
    
print("lets Play..!!!")
score = 0
ques1 = input("What is the largest planet in our solar system?")
if ques1.lower() == 'jupiter':
    print("correct..!!")
    score = +1
else:
    print("Incorrect")
        
ques2 = input("What is the tallest mammal in the world?")
if ques2.lower() == 'giraffe':
    print("correct..!!")
    score = score+1
else:
    print("Incorrect")
    
ques3 = input(" What is the chemical symbol for gold?")
if ques3.lower() == 'au':
    print("correct..!!")
    score = score+1
else:
    print("Incorrect")
    
ques4 = input("What is the largest ocean on Earth?")
if ques4.lower() == 'pacific':
    print("correct..!!")
    score = score+1   
else:
    print("Incorrect")
    
ques5 = input(" Which planet is known as the 'Red Planet'?")
if ques5.lower() == 'mars':
    print("correct..!!")
    score = score+1
else:
    print("Incorrect")

print("Well Play...:)")
print("Your Score.."   + str(score))    


       