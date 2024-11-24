import random
print("stein...paper...schere")
mal=int(input("return mal: "))
user_point=0
player_point=0
for i in range(1,mal+1):
    user=input("return your choise: ")
    number=random.randint(1,3)

    player=""
    if number==1 :
        player="stein"
        print("player choise stein")
    elif number==2 :
        player="paper"
        print("player choise paper")
    elif number==3 :
        player="shere"
        print("player choise shere")
    if player =="stein" and user=="paper" :
        user_point+=1
    elif player =="stein" and user=="shere" :
        player_point+=1
    elif player =="paper" and user=="stein" :
        player_point+=1
    elif player =="paper" and user=="shere" :
        user_point+=1
    elif player =="shere" and user=="paper" :
        player_point+=1
    elif player =="shere" and user=="stein" :
        user_point+=1
    else :
        print("equls!!")
print(player_point,user_point)
if player_point>user_point :
    print(f"player win{player_point}:{user_point}")
elif player_point<user_point :
    print(f"user win{player_point}:{user_point}")
else:
    print("equls")