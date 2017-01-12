# Trivia Quiz

print("This is a quiz that tests your knowledge of sports")
name = input('Enter your name: ')

print('\nHi there' , name + ' Are you ready to take this quiz?')
print('I will ask you 10 questions and give you three choices for each question')
print('Select the right choice by pressing A, B or C')

print("---------------------------------------------------------------------------")

#set quiz score to 0

score = 0
score = int(score) # convert 0 into a number so we can add scores


# question 1

print('QUESTION 1: What position does LeBron James play?')
print("A. Point Guard")
print("B. Small Foward")
print("C. Power Foward")
print('')

Q1answer = 'B' # right answer to question 1
Q1response = input('Your answer: ')

if Q1response =="B" or Q1response == 'b':
    print('Well done ' + Q1response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect!, keep trying :)!')

print('Your current score is ' + str(score) + ' out of 10')

# question 2

print('\nQUESTION 2: Who won the NBA Final in 2016?')
print("A. San Antonio Spurs")
print("B. Cleveland Cavaliers")
print("C. Golden State Warriors")
print('')

Q2answer = 'B' # right answer to question 2
Q2response = input('Your answer: ')

if Q2response =="B" or Q2response == 'b':
    print('Well done ' + Q2response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! come on you got this!')

print('Your current score is ' + str(score) + ' out of 10')

# question 3

print('\nQUESTION 3: Which sport involves kicking a field goal?')
print("A. American Football")
print("B. Soccer")
print("C. Lacroste")
print('')

Q3answer = 'A' # right answer to question 3
Q3response = input('Your answer: ')

if Q3response =="A" or Q3response == 'a':
    print('Well done ' + Q3response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! Never Give Up!')

print('Your current score is ' + str(score) + ' out of 10')

# question 4

print('\nQUESTION 4: Which player belong in the sport American Football?')
print("A. David Beckham")
print("B. Kevin Durant")
print("C. Odell Beckham Jr")
print('')

Q4answer = 'C' # right answer to question 4
Q4response = input('Your answer: ')

if Q4response =="C" or Q4response == 'c':
    print('Well done ' + Q4response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! This question is easy come on!')

print('Your current score is ' + str(score) + ' out of 10')

# question 5

print('\nQUESTION 5: What team does Paul Pierce used to played for?')
print("A. New York Giants")
print("B. Boston Celtics")
print("C. Los Angeles Clippers")
print('')

Q5answer = 'B' # right answer to question 5
Q5response = input('Your answer: ')

if Q5response =="B" or Q5response == 'b':
    print('Well done ' + Q5response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! Tricky Question')

print('Your current score is ' + str(score) + ' out of 10')

# question 6

print('\nQUESTION 6: How many Referee are there is one game of NBA?')
print("A. 3")
print("B. 4")
print("C. 2")
print('')

Q6answer = 'A' # right answer to question 6
Q6response = input('Your answer: ')

if Q6response =="A" or Q6response == 'a':
    print('Well done ' + Q6response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! Try watching a NBA game and come back to answer this later!')

print('Your current score is ' + str(score) + ' out of 10')

# question 7

print('\nQUESTION 7: Which NBA team blew a 3-1 lead in the Playoff?')
print("A. Oklahoma Thunders")
print("B. Golden State Warriors")
print("C. A and B")
print('')

Q7answer = 'C' # right answer to question 7
Q7response = input('Your answer: ')

if Q7response =="C" or Q7response == 'c':
    print('Well done ' + Q7response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! Sadly both team did!')

print('Your current score is ' + str(score) + ' out of 10')

# question 8

print('\nQUESTION 8: Who lost the first Superbowl of the 70s')
print("A. Minnesota Vikings")
print("B. New York Giants")
print("C. Miami Dophins")
print('')

Q8answer = 'A' # right answer to question 8
Q8response = input('Your answer: ')

if Q8response =="A" or Q8response == 'a':
    print('Well done ' + Q8response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! HaHa')

print('Your current score is ' + str(score) + ' out of 10')

# question 9

print('\nQUESTION 9: What is the oldest stadium in MLB?')
print("A. Yankee Stadium")
print("B. Wrigley Field")
print("C. Fenway Park")
print('')

Q9answer = 'C' # right answer to question 9
Q9response = input('Your answer: ')

if Q9response =="C" or Q9response == 'c':
    print('Well done ' + Q9response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! BOO BOO')

print('Your current score is ' + str(score) + ' out of 10')

# question 10

print('\nQUESTION 10: Which sport has the largest audience?')
print("A. Soccer")
print("B. Football")
print("C. Basketball")
print('')

Q10answer = 'A' # right answer to question 10
Q10response = input('Your answer: ')

if Q10response =="A" or Q10response == 'a':
    print('Well done ' + Q10response + ' is correct!')
    score = score +1

else:
    print('Sorry, that is incorrect! Game Over')

print('Your current score is ' + str(score) + ' out of 10')






