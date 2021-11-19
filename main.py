import random

def heads_or_tails():
  user_choice = input("\nHeads or Tails? ")
  user_choice = user_choice.lower()

  # Bot choice is opposite of user_choice
  if user_choice == "heads":
    bot_choice = "tails"
    print("Okay, the bot chose " + bot_choice)
  elif user_choice == "tails":
    bot_choice = "heads"
    print("Okay, the bot chose " + bot_choice)
  else:
    heads_or_tails()
  
  result = random.randint(1,2)

  # Result is either heads (1) or tails (2)
  if result == 1:
    result = "heads"
  elif result == 2:
    result = "tails"
  
  # Prints out who won
  if result == "heads" and user_choice == "heads":
    print("\n" + result.capitalize() + "!" + " User wins")
  elif result == "tails" and user_choice == "tails":
    print("\n" + result.capitalize() + "!" + " User wins")
  else:
    print("\n" + result.capitalize() + "!" + " Bot wins")

  # Rematch?
  global try_again
  try_again = input("Would you like to try again? ")
  try_again.lower()

heads_or_tails()

while try_again == 'yes':
  heads_or_tails()

print("Okay, the program has ended")