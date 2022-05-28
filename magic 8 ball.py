#need to import the random module IOT use the randint function which generates random values.
import random

name = "kris"
question = "Will it rain today?"
answer = ""
random_number = random.randint(1,5)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply Hazy, try again."
elif random_number == 5:
    answer = "Better not to tell anyone"
else: 
    answer = "error"
print(name + "asks:" + question)
print ("Magic 8-ball's answer: " + answer)

