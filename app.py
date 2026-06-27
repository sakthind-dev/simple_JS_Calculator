from flask import Flask, request, jsonify
from flask_cors import CORS

# Serve the existing static files (index.html, script.js) from this folder
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)


def my_python_function(text: str) -> str:
    """Example Python function that processes input from the frontend."""
    # Replace this logic with whatever you need the backend to do
    return f"Python received: {text}"


@app.route('/run', methods=['POST'])
def run():
    data = request.get_json() or {}
    text = data.get('text', '')
    result = my_python_function(text)
    return jsonify({'result': result})


@app.route('/')
def index():
    # Serve the calculator page
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

def my_python_function(value):
    return f"Hello from Python, you sent: {value}"

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    result = my_python_function(data.get("text", ""))
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)