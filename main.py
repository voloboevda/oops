from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def data():
  return jsonify({'zdarova': 'zaebal'})

if __name__ == '__main__':
    app.run()
