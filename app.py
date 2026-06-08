from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)

    return render_template(
        "index.html",
        weather=weather_data
    )

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)