import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "hello world, berhasil terhubung ke db"

if __name__ == "__main__":
    app.run()