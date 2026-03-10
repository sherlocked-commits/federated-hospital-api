from flask import Flask
import pandas as pd

app = Flask(__name__)

hospital1 = pd.read_csv("hospital1.csv")
hospital2 = pd.read_csv("hospital2.csv")

@app.route("/")
def home():
    return "Federated Hospital API"

@app.route("/hospital1")
def get_hospital1():
    return hospital1.to_json(orient="records")

@app.route("/hospital2")
def get_hospital2():
    return hospital2.to_json(orient="records")

if __name__ == "__main__":
    app.run()