from sense_hat import SenseHat
import electronicDie
import csv
import time

sense = SenseHat()

WINNING_SCORE = 4
SCROLL_SPEED = 0.07

def checkForWinner(scoreP1, scoreP2):
    winner = "P?"
    didWin = False
    winnerScore = 0
    if scoreP1 >= WINNING_SCORE:
        winner = "P1"
        didWin = True
        winnerScore = scoreP1
    elif scoreP2 >= WINNING_SCORE:
        winner = "P2"
        didWin = True
        winnerScore = scoreP2

    if didWin == True:
        sense.show_message(winner + " won! Thanks for playing",scroll_speed=SCROLL_SPEED)
        saveScore(winnerScore)

    return didWin

def saveScore(score):
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    with open('winners.csv', 'a') as winnersFile:
        writer = csv.writer(winnersFile)
        writer.writerow([current_time, score])


sense.show_message("Take turns shaking Pi until a player reaches " + str(WINNING_SCORE) + " points.", scroll_speed=SCROLL_SPEED)

p1 = 0
p2 = 0
winnerExists = False
while winnerExists == False:
    sense.show_message("P1 Shake...",scroll_speed=SCROLL_SPEED)
    p1 = p1 + electronicDie.rollDie()
    sense.show_message("P1 Score: " + str(p1),scroll_speed=SCROLL_SPEED)

    winnerExists = checkForWinner(p1, p2)
    if winnerExists == False:
        sense.show_message("P2 Shake...",scroll_speed=SCROLL_SPEED)
        p2 = p2 + electronicDie.rollDie()
        sense.show_message("P2 Score: " + str(p2),scroll_speed=SCROLL_SPEED)

        winnerExists =  checkForWinner(p1, p2)

