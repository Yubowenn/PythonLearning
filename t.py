from flask import Flask, Blueprint

app = Flask(__name__)

# 定义视图
@app.route("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.run()
