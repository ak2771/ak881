def hangman():
  print("--------------------------------")
  print("Welcome to Hangman!")
  print("Hangman is a fun, quick game where you get to test your guessing skills around something like movie names,")
  print("just like in this game! The CPU comes up with a movie and hides it with blank spaces, each one representing a letter.")
  print("The player then tries to crack the code by guessing letters they think are in the word or guess the word itself.")

  print("Here's the twist: every time you guess wrong, you lose one life (don't worry though, since you have 2 short of a cat's lives - 7 lives).")
  print("Too many misses, and the lives go to zero, which means game over!")
  print("But if you can figure out the word before the counter ends, you win the round.")

  print("It's a simple game that gets your mind whooshing and heart thumping,")
  print("especially when the movies are ones you would think you know!")

  print("--------------------------------")
  
  def main():    
    
    starter = input("Do you wish to play? (yes/no): ").lower()

    if starter == "yes":
      print("Let the game begin!")

      while True:
        print("You can choose your game type (1. for 1v1 with a friend or 2. for CPU)")
        typeofgame = input("Enter your choice:")

        if typeofgame == '1':
          from HumanGame import humangame
          humangame()
          return main()

        elif typeofgame == '2':
          from CPUGame import cpugame 
          cpugame()
          return main()

        else:
          print("Invalid choice. Please choose 1 or 2.")
          continue
        
    else:
      print("Goodbye!")
      exit() 


  main()


hangman()