from flask import Flask , render_template
from random import randint


app= Flask('stone paper')

def computer_move():
    options = ['stone','paper','pencil','scissors']
    move = options[randint(0,3)]
    return move

def winner(computer_move , player_move):
    if computer_move == player_move:
        winner ='tie'
    elif player_move == 'stone' and computer_move == 'paper':
        winner= computer
    elif player_move == 'paper' and computer_move == 'scissors':
        winner= computer
    elif player_move == 'scissors' and computer_move == 'stone':
        winner= computer
    elif player_move == 'paper' and computer_move == 'pencil':
        winner= computer
    else:
        winner = 'player'

    return winner
    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prejith/<choice>')
def prejith(choice):
    #return'<h1>{winner}</h1>'
    player_move= choice
    computer = computer_move()
    winner_g=winner(computer,player_move)
    print(winner_g)
    
    return render_template('winner.html',prejith = winner_g,computer=computer,player_move=player_move)

if __name__=='__main__':
    app.run(port=7000)