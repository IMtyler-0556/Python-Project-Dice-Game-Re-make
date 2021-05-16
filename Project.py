# My program project (last edited 01/05/2021)
# Made by Tyler.
# using Python 3.8.2
# V 2.5
#

import random  # this helps the program pick random numbers.
import time  #module for time.
import sys  # This is for sys.exit() thing, it allows the user to exit the program.


# This lets the player make a new account or decide if they are an exiting user

print('  TIP:   Press Ctrl+C to exit the program                         ')
print('  Made By Tyler - Computer Science Project                        ') 
print('  This is just a text-based game... so there is NO GUI (yet)...   ')
#print(color.BOLD + 'This is just a text-based game... so there is NO GUI (yet)...' + color.END)
                                                                                            
print(' ')
print(' ')
print(' Just Loading. . .')
time.sleep(0.4)# Just to add some separtation... # 0.4secs.
#time.sleep(1) # code thats uneeded 
print(' ')
print(' ')

print(" ◊ ◊ ◊  Welcome  To  The  Dice  Game  ◊ ◊ ◊")   # some fancy text...
abc=input(" Please type in ['new'] if your are a new user type ['existing'] if you are a existing user:  ")
while abc not in ('existing','new'):                     # I add other opitions
    abc=input(" Please type in ['new'] if your are a new user type ['existing'] if you are a existing user: ")


# This allows the player to make a new account.

if abc =="new":
    print(" To Make an account ")
    print('')
    username=input(" Type in a username: ")
    password1=input(" Type in an pasword: ")
    password2=input(" Renter your password: ")
    if password1==password2:
        print(" Your password is... ",password1)
        f = open ("username + password.txt","a+")#Yes you need to know file handling. But we copied it from the internet...
        f.write(f"{username}:{password2}\n")
        f.close()
        abc=input(" Please type in 'new' if your are a new user type 'existing' if you are a existing user: ")
    else:
        print("   The password you entered is not matching, restart the program to start again! ")
        print(" You can do this by pressing Ctrl+C .")
        sys.exit()

if abc == "existing":
    check = True
    while check:
        print(" Player 1 please enter your details ")
        username1=input("Username = ")
        password=input("Password = ")
        with open("username + password.txt","r") as username_finder:
            for line in username_finder:
                if(username1 + ":" + password) == line.strip():
                    print(" You are now logged in ")
                    print(" Player 2 please enter your details ")
                    while check:
                        print("incorect password or username please try again")
                        username2=input("Username = ")
                        password=input("Password = ")
                        with open("username + password.txt","r") as username_finder:
                            for line in username_finder:
                                if(username2 + ":" + password) == line.strip():
                                    check = False
                                    #time.sleep(1)
                                    #time.sleep(1)
                                    #time.sleep(1)                                    
                                    print(" You are now logged on ")

                                    # this is the actual game.
                                    player1=0 #score(s) set = 0
                                    player2=0
                                    print(" *  Welcome  To  My  Dice  Game  * ")


                                    print(" PLAYER 1 READY ")
                                    time.sleep(1)
                                    print(" PLAYER 2 READY ") 

                                    totalscore1=0
                                    totalscore2=0



                                    # Player_1

                                    dice1 = random.randint(1,6)  # it's a fair dice so its 6.
                                    dice2 = random.randint(1,6)
                                    roundno = 1
                                    while roundno < 5:
                                        totalscore1=totalscore1+player1
                                        totalscore2=totalscore2+player2   #THIS IS JUST ADDING OF VARIBLES
                                        player1=dice1+dice2
                                        roundno=roundno+1
                                        print("round",roundno)
                                        time.sleep(0.9000)
                                        print("-----------------------------------------------------")
                                        asdf = input("player 1, press enter to roll")
                                        print(" Player 1 is rolling...   ")
                                        print(" Player 1's first roll is",dice1)
                                        time.sleep(1.3)
                                        print(" Player 1's second roll is...  ",dice2)
                                        time.sleep(1.2)
                                        print("-----------------------------------------------------")
                                        if player1 %2==0:
                                            print("This is an even number +10 points!  ")
                                            time.sleep(1)
                                            player1=player1+10
                                            time.sleep(1)
                                            print("score is",player1)
                                            if player1<= 0:
                                                print("You lost the game   ")
                                                sys.exit()
                                            print("-----------------------------------------------------")
                                            print('')

                                        else:
                                            print("This is an odd number.   ")
                                            time.sleep(2)
                                            player1=player1-5
                                            print("score is",player1)
                                            time.sleep(3)
                                            print("player 1 score",player1)
                                            print("-----------------------------------------------------")
                                            print('')



                                        time.sleep(1)
                                        # Player_2
                                        dice1 = random.randint(1,6)
                                        dice2 = random.randint(1,6)
                                        totalscore1=totalscore1+player1
                                        totalscore2=totalscore2+player2
                                        player2=dice1+dice2
                                        print("-----------------------------------------------------")
                                        asdf = input("player 2 press enter to roll")

                                        print("...player 2 is rolling...")
                                        time.sleep(1)
                                        print("...player 2's first roll is",dice1)
                                        time.sleep(1)
                                        asdf = input("...player 2 press enter to roll again")
                                        time.sleep(1)
                                        print("...player 2's second roll is",dice2)
                                        time.sleep(1)
                                        print("-----------------------------------------------------")
                                        print('')

                                        if player2 %2==0:
                                            print("This is an even number +10 points!  ")
                                            time.sleep(1)
                                            player2=player2+10
                                            print("score is",player2)
                                            time.sleep(1)
                                            if player2<= 0:
                                                print("You have lost the game...  ")
                                                sys.exit()
                                            print("-----------------------------------------------------")
                                            print('')
                                            
                                        else:
                                            print(" This is an odd number.  ")
                                            time.sleep(1)
                                            player2=player2-5
                                            print(" score is ",player2)
                                            time.sleep(3)
                                            print("player 2 score",player2)
                                            print("-----------------------------------------------------")
                                            print('')
                                            
                                    print(" the total score for player 1 is... ",totalscore1)
                                    print(" the total score for player 2 is... ",totalscore2)
                                    if totalscore1 > totalscore2:
                                        print("  Well done, player 1 you win!  ")
                                        file = open("scores.txt2","a+")
                                        file.write("player 1 ")
                                        file.write(username1)
                                        file.write(" has won overall with ")
                                        file.write(str(totalscore1))
                                        file.write(" points")
                                        file.write("\n")

                                    if totalscore2 > totalscore1:
                                        print("player 2 wins")
                                        file = open("scores.txt2","a+")
                                        file.write("player 2 ")
                                        file.write(username2)   # makes .txt files 
                                        file.write(" has won overall with ")
                                        file.write(str(totalscore2))
                                        file.write(" points")
                                        file.write("\n")     



                                else:

                                    print(" INCORECT PASSWORD and/or USERNAME ! ")

                else:
                    print(" INCORECT PASSWORD and/or USERNAME ! ")

#print('Help Test 1')
