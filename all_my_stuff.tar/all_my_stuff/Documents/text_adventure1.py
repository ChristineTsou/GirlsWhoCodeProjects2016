start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “Don’t touch the walls. Try and get out.”
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left. The hallway opens up to a large room that you cannot see the edge of. \nThere is a river in front of you.") # finished the story by writing what happens
    user_input=input("You notice a small wooden boat at the edge of the river. Do you use it to get across? yes or no ")
    done = True
    if user_input=="no":
    	print("You decide not to take the boat thinking it might be rigged and instead walk along the river, trying to find a shallower area when you see a small house with smoke coming out of the chimneny.")
    	user_input=input("Do you go to the house and 'knock' or do you 'ignore it' and continue walking? ")
    	if user_input=="knock":
    		print("You knock at the door. There's a moment of silence and then the door creaks open. 'Hello?' You say. There's no answer.")
    		user_input=input("Will you go inside to look for people? ")
    		if user_input=="yes":
    			print(" You step inside and the door swings shut behind you.")
    			print("Frightened, you try to open the door but the knob will not turn and you realize that you are trapped. 'Hey hey~' a voice sounds behind you and you turn around just in time to get knocked unconsious by a club.")
    			print("...You wake up suddenly in the house with a bump on your head. Remembering the voice, you look around in panic, but there's no trace of anyone. You notice that there is an envelope on the floor.")
    			user_input=input("Should you pick the envelope up? yes or no ")
    			if user_input=="yes":
    				print("You pick up the envelope and open it. Inside is a piece of paper with the following written on it: Wardrobe cave")
    				print("You have no idea what it means. There is a wardrobe inside the house though.")
    				user_input=input("Should you look inside it? yes or no ")
    				if user_input=="yes":
    					print("You decide not to think too much and grab the handles of the wardrobe. You yank open the doors and prepare for the worst. Nothing happens. You look inside. The wardrobe is empty, except for a small, musty lantern. You pick up the lantern and stare at it. Then you hear a knocking sound at the door")
    					user_input=input("Should you open the door? yes or no ")
    					if user_input=="yes":
    						print("You remember that the door was locked but try it anyway. Surprisingly, the knob turns and you open the door to be confronted by a terrible greenish and slimy monster. A terrible smell spreads through out the room. You look up and scream as it squeezes in through the door. You try to get away, but the house is small and the door is blocked. The monster grabs you and you die.")									
    					if user_input=="no":
    						print("You decide not to open the door. However, the banging noises become louder and louder. You are terrified. The house has suddenly gotten dark and you hear more noises outside. As you move to a corner of the house you stumble and nearly fall. In the process, you switch on the lantern by mistake. There are sounds of screams and then it abruptly gets quiet again.")
    						print("You get up and look out a window. There is nothing outside. Then you realize the door has been unlocked. It has gotten brighter and you decide to leave the house in search of the cave as written on the note.")
					    	print("...\nYou walk all day. just as you are about to give up, you see the hallway that you came in from. Is that the cave? You go inside, and a door closes behind you, cutting you off from the river. A glowing circle is on the floor. You stare at it.")
					    	user_input=input("Do you get on it? yes or no ")
					    	if user_input=="no":		
					    		print("Nothing happens. You stand there and stare at it. Then the hallway collapses and you die.")
					    	if user_input=="yes":
						    	print("The scenery changes. You are in a cave, lit by only the lantern in your hand. You begin to walk. Eventually, you see a door. There is a keyhole and you have no key.")
						    	print("Just then, you catch a glimpse of a man. He runs away the moment you meet eyes with him.")
						    	print("You chase him. You catch up to him by throwing the lantern at him. You search him. Bingo! He has a key. You rush to the door and try the lock. The door opens and you see...")
						    	print("You see the room connected by the two hallways that you came in. There is a note on the floor. You pick it up and read the following: Have a nice day! lol")    							
    				if user_input=="no":
    					print("You decide not to mess with the envelope. It might be a trap after all. Then you realize that the door is still locked. You look around, but there is no way out...")
    					print("Some time passes and it gets dark again. 'It's way too soon for night.' you think. Suddenly the door swings open. A terrible smell spreads through out the room. You look up and scream as a slimy, greenish monster squeezes in through the door. You try to get away, but the house is small and the door is blocked. The monster grabs you and you die.")
    			if user_input=="no":
    				print("You decide not to mess with the wardrobe. It might be a trap after all. Then you realize that the door is still locked. You look around, but there is no way out...")
    				print("Some time passes and it gets dark again. 'It's way too soon for night.' you think. Suddenly the door swings open. A terrible smell spreads through out the room. You loop up and scream as a slimy, greenish monster squeezes in through the door. You try to get away, but the house is small and the door is blocked. The monster grabs you and you die.")
    		if user_input=="no":	
    			print("You decide that the house is too suspicious and back out. The next moment, the door swings shut. You try the door but it is locked. 'Oh well' you say. As you walk away from the house you notice a strange fog approaching. Suspecting no good, you try to run away, but it is too late. The poisonous fog catches up to you, and you suffocate.")
    	if user_input=="ignore it":
    		print(" You continue walking. It becomes dark. Suddenly, a poison cloud sweeps through and you have no place to run. You collapse and die.")
    		done = True
    elif user_input=="yes":
    	print("You get into the boat. There is a wooden paddle and you use it to row.\n when you about halfway through, you notice that you are getting wet! The boat is leaking!")
    	print("The water looks a bit rough and there may be hidden rocks, but\n the river doesn't seem that wide. You are not sure how much \nlonger the boat will last. \n")
    	user_input=input("Do you 'continue rowing' or 'jump out and swim'? ")
    	done = True
    	if user_input=="jump out and swim":
    			print("The current is harder to swim across than expected. You drown.")
    	if user_input=="continue rowing":
    		print("The boat hits a rock and capsizes. You are flung into the water.\n A piece of wood from the boat floats by.")
    		print("You can either hold on to it or simply swim as hard as you can towards the riverbank.")
    		user_input=input("Will you 'grab the wood' or 'swim hard'? ")
    		done = True
    		if user_input=="swim hard":
    			print("The current is harder to swim across than expected. You drown")
    		if user_input=="grab the wood":
    			print("The current is strong but you manage to get to the bank. As you stumble ashore,\n you notice that it is getting dark. A cave lies before you. There is no other place to go.")
    			print("You can wait here until it becomes brighter to venture in the cave or you can head in now.")
    			user_input=input("Which will you choose? 'wait' or 'head in now' ")
    			done = True
    			if user_input=="wait":
    				print("You wait. It becomes darker and you begin to fall asleep. Just as you nearly do, you notice that it is getting harder to breathe. A poisonous fog has drifted in. Your last thoughts as you die")
    				print(" are that you are in a maze created by someone, and not in nature.")
    			if user_input=="head in now":
    				print("You take a deep breath and enter the cave. It gets dark and you slow down. Suddenly, you hear a faint cry.")
    				user_input=input("Do you 'investigate the noise' or ignore it and 'continue'? ") 
    				done = True
    				if user_input=="investigate the noise":
    					print("You find a tattered man, stuck between two rocks. You have no idea how he got there, but he is asking for help.")
    					user_input=input("Do you 'help the man' or 'turn around and leave him'? ")
    					done = True
    					if user_input=='help the man':
    						print("You bend down and attempt to push the rocks away from the man. The rocks do not move and suddenly you feel hands around your throat. You try to struggle, but it is hopeless. You are strangled to death.")
    					elif user_input=='turn around and leave him':
    						print("The man is crying out for help but you turn your back and head away from him. All of a sudden a hand grabs you from behind and you hear the man say 'how terrible you are, to leave someone stranded like that.' A knife stabs into you and you die.")
    				if user_input=='continue':
    					print("You decide that it's better not to be curious. As you continue, you notice that it is getting harder to breathe. Due to your slow walking speed, a poisonous fog has caught up to you. You collapse and suffocate.") 
	
elif user_input == "right":
    print("You choose to go right. The hallway opens up to a large room filled with trees. It is a mini forest. It begins to downpour.") # finished the story writing what happens
    user_input=input("You can either 'stay in hallway' or 'head out in the rain'. Which do you choose? ")
    done = True
    if user_input=="stay in hallway":
    	print("A door comes down and seals the entreway to the forest. You have decided to stay in the hallway where the rain cannot catch you. Going out in the rain might cause a cold after all. You look around as you wait for the rain to die down and the door to reopen when you see a ominous mist heading towards you from the way you came. There is nowhere to run and you suffocate.")
    if user_input=="head out in the rain": 
    	print("The rain is heavy and makes it hard to see. You blunder towards the forest. Just as you reach it, you trip, tumbling down a slope. You come to a rest and realize that you have been bitten by a snake.")
    	print("The snake may be poisonous. As you stare through the rain while clutching your bitten leg, you notice a light in the distance. A light in this rain?")
    	user_input=input("Should you check it out? it could be a trap. On the other hand, the bite you've gotten might need some attention. 'check it out' or 'stay here'" )
    	if user_input=="stay here":
    		print("The bite is more serious than you thought. You lose consiousness and die.")
    	if user_input=="check it out":
    		print("It's a hard journey to get to the source of the light. Your leg feels like it's begin stabbed by needles and it's all you can do to keep going. Finally you reach the light. And it is just a light! A lantern, with a cover to keep out the rain. You are disappointed as you collapse and die.") 

    