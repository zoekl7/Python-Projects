
#parent class

class Soccer:
    teamName = 'No name provided'
    league = 'little league'
    field = 'Grass field'
    numbOfPlayers = '11 players'

#child class 1

class Player(Soccer):
    name = ' '
    age = 8
    practicesPerWeek = 2

#child class 2

class Coach(Soccer):
    name = ' '
    basePay = 15.00
    weeklyHours = 35
    
