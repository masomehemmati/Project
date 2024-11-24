
import random
number=random.randint(0,100)
guess_count=5
while guess_count>0 :
    try:
        guess=int(input(f"remaind guess:{guess_count} , enter your next guess(0,100): "))
        if number== guess :
            print("Great")
            break
        elif number> guess :
            print("number is higher")
            
        else:
            print("numner is lower")
        guess_count-=1
    except:
        print("enter a valid number")
if guess_count==0 :
    print("sorry")
print(f"number war {number}")