"""
Author: Lucas Emanuel Oliveira de Carvalho
Project: Create an adventure using if/else
"""


print("  There wasn't much left of the ship after it got stuck on the rocks near the beach. "
     "Even after looking in places nearby, on the surrounding beaches, no one appeared to "
      "have survived. The morning after the shipwreck didn't look very inviting, with lots of black "
      "clouds and thunder, it was clear that a new storm was approaching. It was time to make a decision. ")

choice = input("\nWhat will you do: look for SHELTER or look for OBJECTS on the ship?\n")

if choice.upper() == 'SHELTER': 
    print("Because of the rain, it seems like a better idea to look for shelter. "
          "There didn't seem to be anything around that looked like a decent place.")
    
    kind = input("Do you prefer to BUILD a shelter or find a CAVE to use as shelter?\n")

    if kind.upper() == 'BUILD':
            print("Even without many tools, building became the best option." 
                      "There weren't many places that would serve as good shelter available in the wild." 
                      "Nor would it be safe to enter a cave without knowing if there might be any animals.")
            
            what = input("Will you first build a ROOF, a FENCE or an ELEVATED place to sleep?\n")

            if what.upper() == 'ROOF':
                    print("Unfortunately you don't have enough tools to put together a good roof." 
                        "As soon as the storm began to fall, its roof went with it and because it was " 
                        "too exposed to rain. you got sick and, without medicine, you died. END OF ADVENTURE.")
            
            elif what.upper() == "FENCE":
                         print("The rain made you sick, with nothing to cover and protect you, you died. "
                        "YOUR ADVENTURE HAS COME TO AN END")
                  
            elif what.upper() == 'ELEVATED':
                        print("The tree you chose was strong enough to support you, "
                              "and the leaves and branches were able to protect enough from the rain. " 
                              "YOU WILL LIVE TO SEE ANOTHER DAY...")
                  
            else:
                   print("Your choice is not valid. START AGAIN.")
                
    
    
    elif kind.upper() == "CAVE":
            print("Without having time to collect the tools to build a good place, finding a cave in the mountain"
                "range that formed near the beach did not seem like a difficult task." 
                "And indeed it was not. But she could still hold some surprises...")

            cave = input("Are you going to use this cave as a COVER from the rain or are you going to LIVE in it?\n")

            if cave.upper() == "COVER":
                  print("That's a good choice. YOU WILL SEE ANOTHER DAY BEGIN.")

            elif cave.upper() == "LIVE":
                  print("You relaxed too much. THIS IS THE END FOR YOU.")

            else:
                  print("Your choice is not valid. START AGAIN.")
          
    else:
          print("Your choice is not valid. START AGAIN.")

elif choice.upper() == 'OBJECTS':
      print("  Even if the storm was approaching, the risk of losing the few objects" 
          "that were still inside the wreckage of the stranded ship or that were floating was greater" 
          "than the need to seek shelter.")
    
      where = input("Are you going to look for objects on the BEACH or on the stranded SHIP?\n")

      if where.upper() == "BEACH":
            print("Even with the storm approaching, the fear of losing all the objects is greater." 
                 "It seems like a good idea to collect some of them.")
            which = input("Do you prefer to collect the SMALL or BIG objects?\n")

            if which.upper() == "SMALL":
                  print("The small objects are too scattered," 
                        "your idea was bad and you got lost in the middle of the storm.")

            elif which.upper() == "BIG":
                  print("Even heavy, you've gathered some chests that may have valuable things. GOOD CHOICE.")

            else:
             print("Your choice is not valid. START AGAIN.")
      
      elif where.upper() == "SHIP":
            print("The ship seems to be well fixed in the sand on the beach.")
      
            better = input("What's better: use the ship as HOUSE or GET what you can and leave?\n")

            if better.upper() == "HOUSE":
                  print("That was the best choice. The tide is low and you will be" 
                   "able to choose a better house at dawn. CONGRATULATIONS.")
      
            elif better.upper() == "GET":
                  print("Your choice wasn't bad, but you can't leave the ship carrying a lot" 
                   "of things from the ship. YOU ARE STUCK.")
             

            else:
                  print("Your choice is not valid. START AGAIN.")
              


else:
      print("You must choose between SHELTER or OBJECTS")