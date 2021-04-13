import random
def hangman ():
	word_list = ("""ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""").split ()
	random_number = random.randint (0, len(word_list) -1)
	word = word_list [random_number] 
	wrong = 0
	stages = ["",
	         "__________         ",
	         "|                  ",
	         "|          |       ",
	         "|          O       ",
	         "|         /|\      ",
	         "|         / \      ",
	         "|                  "
	         ]
	rletters = list (word)
	board = ["__"] * len(word)
	win = False
	print ("Welcome to the Hangman game ! ")
	print ("You need to find an animal name")
	while wrong < len (stages) - 1:
		print ("\n")
		msg = "Guess a letter: "
		char = input (msg).lower ()
		if char in rletters:
			cind = rletters.index (char)
			board [cind] = char
			rletters[cind] = "$"
		else:
			wrong += 1
		print ((" ".join(board)))	
		print (("\n".join(stages[0: wrong +1])))
		if "__" not in board:
			print ("You win ! The word was: ")
			print (" ".join(board))
			win = True 
			break
	if not win:
		print ("\n".join (stages[0: wrong]))
		print ("You lose.. It was {}.".format (word))

hangman ()

