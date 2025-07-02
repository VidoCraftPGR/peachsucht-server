from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hallo, der Server läuft!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render setzt PORT automatisch
    app.run(host="0.0.0.0", port=port)
