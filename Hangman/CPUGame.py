from ChoosingMovies import movie_Selection


def cpugame():
    
    print("")
    print("Welcome to Hangman CPU verion!")
    print("You will choose the difficulty and category of movie you want to guess.")
    print("The CPU presents word to you and you have to guess it.")
    print("Your aim is to not only win, but save as many lives as possible.")
    print("Good luck!")
    print("")

    #counter = 7
    name = movie_Selection('')  #stays 

    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")

    import GameAlgo
    counter = GameAlgo.GameAglo(name)
    print("You won with", counter, "lives itact!")
        
#cpugame()