############################################
# Title: Project 4- Loops Game: Spin to Win!
# Programmer: Anika Sharma
# Date: 23/03/2021
# Purpose: To create a game that gives the user money for spinning certain special cases between two numbers.
############################################

#imports, count for console line, playagain variable to make another run
import random
import time
lines = 70
playagain = "y" 

#bonus- timer
starttime = time.time()

#welcome message
print("_" * lines)
print("\n        **************Welcome to Spin to Win!**************")
print("_" * lines)

#take user input to read Game rules 
rulesorno = input("\nIf you would like to read the rules, type y. If not, type n: \n")

while True:
  #print the Game rules if user wants to check
  if rulesorno == "y" or rulesorno == "Y":
    print("_" * lines)
    print("\nRULES OF SPIN TO WIN:")
    print("\n1. In order to start the game, you have to purchase the number of spins (1 spin = $0.25). The total cost of spins is your initial game money.")
    time.sleep(1)
    print("\n2. All win profits are applied to your initial game money.")
    time.sleep(1)
    print("\n3. You can win multiple profits in one spin.")
    time.sleep(1)
    print("\n4. You gain money if:")
    time.sleep(0.5)
    print("\ta. Both of your numbers are 9, you win the Jackpot! It is triple your game money.")
    time.sleep(0.5)
    print("\tb. Both of your numbers are the same and EVEN, you get 20% of your initial game money.")
    time.sleep(0.5)
    print("\tc. Both of your numbers are the same and ODD, you get 30% of your initial game money.")
    time.sleep(0.5)
    print("\td. You have consecutive numbers, you get 25% of your initial game money.")
    time.sleep(0.5)
    print("\te. Both numbers are MULTIPLES, you get 5% of your initial game money.")
    time.sleep(0.5)
    print("\tf. If the LEFT number is greater than the right, you get 15% of your initial game money.")
    time.sleep(1)
    print("\n5. You lose money if:")
    time.sleep(0.5)
    print("\ta. Both of your numbers are 0, your money will become $0 as well.")
    time.sleep(0.5)
    print("\tb. Your numbers do not have any special qualities that make you win, your money will become $0.")
    time.sleep(1)
    break

  #if user dont want to read the rules then start the game
  elif rulesorno == "n" or rulesorno == "N":
    print("Alright, you must know the game pretty well then.")
    time.sleep(0.5)
    break

  #take correct choice from user again to read rules
  else:
    rulesorno = input("\nThat is an invalid answer. Please answer with 'y' or 'n': \n")

#let's play announcement
print("_" * lines)
print("\nNow that you have read the rules, or already know them, let's play the game! Good luck and have fun!")
time.sleep(0.5)
print("_" * lines)

#variable to track initial invested money
displaymoney = 0

#main loop to play the game
while playagain == "y" or playagain == "Y":
  #intial money input
  print("\n1 spin = $0.25\n")
  spins = int(input("How many spins do you want to buy? (must be a whole number): "))

  #spins cost
  initialmoney = round(spins * 0.25, 2)
  displaymoney = initialmoney
  print("You have purchased", spins, "spins of $" + str(initialmoney),"\n \nLet's begin the game.")
  
  #variable to track game money
  money = initialmoney
  print("_" * lines)

  #for loop that runs for how many spins user has bought
  for i in range(0, spins):

    #to determine if they win or not
    winningornot = "no"

    #get two random numbers for spinning
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    #get user input to spin
    input("\nType s or any key, and press enter for spin " + str(i+1) + ": ")
    
    #show spinning numbers
    for k in range(0,num1 + 1): 
      for j in range(0,num2 + 1):
        print(k,"|", j, end = "\r") 
        time.sleep(0.03)  
  
    #printing the two final numbers
    time.sleep(0.5)
    print("\nAlright, the machine has spun! Here are your numbers!")
    time.sleep(0.5)
    print("\n \t \t \t \t \t", num1, "\t | \t", num2)
    print('')
    
    #win case 1: 9|9: Jackpot
    if num1 == 9 and num2 == 9:
      winningornot = "yes"
      money = money + (initialmoney * 3)
      print("YOU WON THE JACKPOT!!!! Congratulations! You win three times your money which is now: $" + str(round(money, 2)))
      break

    #win case 2: same even numbers e.g 2 2
    if num1 == num2 and num1 % 2 == 0 and num1 != 0 and num2 != 0:
      winningornot = "yes"
      money = money + (initialmoney * 0.2)
      print("You got both even numbers! Wow! You win 20% of your money which is now: $" + str(round(money, 2)))

    #win case 3: same odd numbers e.g. 3 3
    if num1 == num2 and num1 % 2 != 0:
      winningornot = "yes"
      money = money + (initialmoney * 0.3)
      print("Wow! You got both odd numbers! You win 30% of your money which is now: $" + str(round(money, 2)))
    
    #win case 4: consecutive numbers e.g 3 4
    if num1 - 1 == num2 or num2 - 1 == num1:
      winningornot = "yes"
      money = money + (initialmoney * 0.25)
      print("Oh! You got adjacent numbers! You win 25% of your money which is now: $" + str(round(money, 2)))
      
    #win case 5: multiples e.g. 4 2
    if num1 != 0 and num2 != 0 and (num1 % num2 == 0 or num2 % num1 == 0):
      winningornot = "yes"
      money = money + (initialmoney * 0.05)
      print("Hooray! You got multiples! You get 5% of your money which is now: $" + str(round(money, 2)))
      
    #win case 6: left number > right number e.g. 7 3
    if num1 > num2:
      winningornot = "yes"
      money = money + (initialmoney * 0.15)
      print("Yippee! Your left number is greater than your right number! You win 15% of your money which is now: $" + str(round(money, 2)))

    #lose case 1: 0|0
    if num1 == num2 and num1 == 0:
      print("Oh no! You got both zeroes. You lose all of your money which is now $0.")
      money = 0

    #lose case 2: if none of the above cases e.g. 0 7 or 2 9
    if winningornot != "yes":
      print("Sorry, your numbers do not match any winning combination. You lost all of your money which is now $0.")
      money = 0

    #spins left
    spinsleft = spins - (i+1) 
    time.sleep(0.5)
    
    #show message of spin counter left 
    if spinsleft > 1:
      print("\nYou still have", spinsleft, "spins left! Keep playing and good luck!")

    #if only 1 spin is left
    elif spinsleft == 1:
      print("\nYou still have 1 more spin! Good luck!")
    
    #if no spins are left
    elif spinsleft == 0:
      print("\nYou're out of spins! Good game.")

    #formatting
    print("_" * lines)

  time.sleep(1)
  
  #total amount earned in game
  totalmoney = round(money, 2)
  print("\nYou played well! Your total money earned is: $" + str(totalmoney))

  #show message to encourage user to be in Game 

  if totalmoney < initialmoney:
    print("\nIt seems that you did not earn much, you should play again to earn money!")

  elif totalmoney > initialmoney:
    print("\nWow! You earned so much money! You should play again to earn even more!")

  else:
    print("\nThat was fun! You should play again!")
  
  #get user input for playing again
  playagain = input("\nPress 'y' then enter to play again. To quit the game, press any key then enter: \n")
  print("_" * lines)

  #end of main while loop 

#timer calculation- calculates total elapsed time of the program
endtime = round(time.time() - starttime)

#final output
print("\nThank you for playing Spin to Win! See you next time. Following are your details. \n \nYou started with: $" + str(displaymoney), "\nYour final money = $" + str(round(money, 2)), "\nYou have finished your spins in =", endtime, "seconds" )