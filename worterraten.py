import random
name_list=["Sara","Zahra","Neda","Mina","Maryam"]
name=random.choice(name_list).lower()
guess_count=len(name)
guess_list=["_"] * len(name)
print(" ".join(guess_list))
while (guess_count+2) > 0 :
    guess_char=input("enter a char: ")
    if guess_char.isalpha():
        if guess_char in name:
            if guess_char in guess_list:
                print("try new char")
            else:
                for idx,char in enumerate(name):
                    if char==guess_char :
                        guess_list[idx]=guess_char
                        print(f"perfect {" ".join(guess_list)}")#ویرگول لیست را حذف میکند

                        if not "_" in guess_list:
                            print("won")
                            guess_count=0
        else:
            print("wrong")                      
        
    else:
        print("enter a char")
    guess_count-=1