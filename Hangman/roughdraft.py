from ChoosingMovies import movie_Selection

def rough():
    name = movie_Selection('')
    print(name)

rough()

#     counter = 7
#     name = movie_Selection('')
#     nameLower = name.lower()
#     movie = [] 
#     for i in nameLower:
#       movie.append(i)
      
#     hidden = []
#     for i in range(len(movie)):
#       if movie[i] == " ":
#         hidden.append(" ")
#       else:
#         hidden.append("_")
    
#     while counter > 0:
        
#       print("Your Movie name is:", " ".join(hidden))
#       print("You have", str(counter), "chances")
      
# #      update_hidden = ''.join(hidden) 

#       guess = input("Guess a letter, digit or movie name:").lower()

#       if guess == nameLower:
#         print("Congratulations! You guessed the movie correctly.")
#         return
      
#       elif guess not in "abcdefghijklmnopqrstuvwxyz1234567890":
#         print("Wrong input :(")
#         counter -= 1

#       else:
#         if guess in movie:
#           for i in range(len(movie)):
#             if movie[i] == guess:
#               hidden[i] = guess
# #              update_hidden = ''.join(hidden)  
#           print("Your Guess is correct")
      
#         else:
#           print("The letter", guess, "is not in the movie.")
#           counter -= 1
                
#         if "_" not in hidden:
#           print("Congratulations! You guessed the movie correctly.")
#           return
                
#         if counter == 0:
#           print("You have run out of chances. The movie was:", name)
#           return