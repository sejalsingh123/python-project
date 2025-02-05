#                 S W G
# computer =      1 2 3  #3:l,-1:d,5:w  player
# player =  S  1  d w l
#           W  2  l d w#fisrt one is player and seconad for computer
#           G  3  w l d
import random

print("*************Welcome to snake water and gun.*************")

com =[1,2,3]
for x in range(1,1000):
 print("  ")
 print(f"Game no: {x} ")
 print("  ")
 player=int(input("Enter '1'for snake ,'2' for water, '3' for gun, and '0' for quit the game:"))
 if player==0:
     print("Game finished.")
     break
 else:
  computer=random.choice(com)
  print(f"Computer chooses the {computer}")
  
  answer={"11":-1,"12":5,"13":3,
    "21":3,"22":-1,"23":5,
    "31":5,"32":3,"33":-1
      }

  ans=str(player)+str(computer)

  check_ans=answer[ans]

  if check_ans==-1:
    print("Match is draw.")
  elif check_ans==5:
    print("You win the match.Bravo!")
  else:
    print("You loss the match.Better luck next time.")


    