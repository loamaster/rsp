from flask import Flask, redirect, send_file, render_template, request
import requests
import random
import io
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data={})

# rock -> 0
# scissors -> 1
# paper -> 2

def winner(a, b):
    if a == b:
        return None
    if a == 0 and b == 1:
        return True
    if a == 1 and b == 2:
        return True
    if a == 2 and b == 0:
        return True
    return False

@app.route('/game')
def game():
    move = int(request.args.get('move'))
    server_move = random.randint(0, 3)
    result = winner(move, server_move)
    return render_template('game.html', move=move, server_move=server_move, result=result)