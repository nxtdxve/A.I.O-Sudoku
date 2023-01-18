from flask import Flask, jsonify, request
from generator import Generator
from solver import Solver

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    generator = Generator()
    generator.generate_number()
    grid = generator.grid
    solved = generator.solved
    return jsonify(grid=grid,solved=solved)

""" @app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    grid = data['grid']
    solver = Solver(grid)
    if solver.solved_string == data['solved']:
        return jsonify(correct=True)
    else:
        return jsonify(correct=False) """

if __name__ == '__main__':
    app.run(debug=True)
