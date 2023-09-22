from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/factorial/<int:n>')
def factorial(n):
    def calculate_factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * calculate_factorial(num - 1)

    result = calculate_factorial(n)
    return jsonify({"factorial": result, "IP Address": "123-456-789"})

if __name__ == '__main__':
    app.run(debug=True)
