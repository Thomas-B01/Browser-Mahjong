from flask import Flask, render_template, jsonify, request
from logic import RiichiMahjong

app = Flask(__name__)

game = RiichiMahjong

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get_game_state', methods= ['POST'])
def start_game():
    game.start_game()
    return jsonify({"status": "Game Started!"})

@app.route ('/get_game_state', methods= ['GET'])
def get_game_state():
        state = game.get_game_state()
        return jsonify(state)

@app.route('/take_turn', methods=['POST'])
def take_turn():
     action = request.json['action']
     game.process_turn(action)
     return jsonify({"status": "Turn processed"})

if __name__ == '__main__':
     app.run(debug=True)