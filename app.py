# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Xin chào! Đây là web app Flask đầu tiên của bạn 🚀"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
