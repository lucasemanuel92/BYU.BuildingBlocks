"""
AUTHOR: Lucas Emanuel Oliveira de Carvalho
PROJECT: For this assignment, you will implement a program that asks the user for a series of words and 
then displays the story with the user's words inserted into the appropriate places.
The program should begin by asking the user for each of the words.
It should then, fill those words into the appropriate places in the story.
"""


print('Please, choose the features')
time = input('Choose a period the day (morning, afternoon, evening, etc.):\n ')
soccer = input('\nChoose a soccer team:\n')
wheater = input('\nChoose a weather:\n')
humor = input('\nChoose a humor state:\n ')
celebration = input('\nHow would you celebrate a goal?\n ')
frustration = input('\nHow would you react when they score against you team?\n')
song = input('\nChoose a song to sing after the game ends\n')
transport = input('\nChoose a transport\n')

print('Matchday')
print('It was a Saturday ' + time.lower() + ' when me and my friends were heading to the Morumbi Stadium, to watch the game between São Paulo and '
      + soccer + '. Because it was ' + wheater + ' we were ' + humor.lower() + '. It was a hard game and at the minute 90 we start ' + 
      celebration.lower() + ' because our striker Calleri scored, but we did not had time to celebrate because ' + soccer + 
      ' tied. The whole crowd was ' + frustration.lower() + '. Even after the game was over in a tie the fans were not that mad.' +
      ' All of us end up leaving in a ' + transport.lower() + ' while singing ' + song) 