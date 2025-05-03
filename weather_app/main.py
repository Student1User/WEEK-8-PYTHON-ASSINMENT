import tkinter as tk
import threading
import webbrowser
from flask import Flask, render_template, request
from apis.openweathermap import get_weather

# === Flask App ===
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if "error" in weather_data:
            error = weather_data["error"]
        else:
            weather_data = {
                "city": weather_data["city"],
                "temperature": weather_data["temperature"],
                "description": weather_data["description"],
                "humidity": weather_data["humidity"],
                "wind_speed": weather_data["wind_speed"],
            }
    return render_template('index.html', weather=weather_data, error=error)

# === Functions ===
def run_flask_app():
    app.run(debug=False, use_reloader=False)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

def launch_gui():
    root = tk.Tk()
    root.title("🌦️ Weather App Launcher")
    root.geometry("400x220")
    root.configure(bg="#e0f7fa")

    title = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"), bg="#e0f7fa", fg="#00796b")
    subtitle = tk.Label(root, text="Launching in your browser...", font=("Helvetica", 12), bg="#e0f7fa", fg="#004d40")
    footer = tk.Label(root, text="Enjoy weather updates ☁️☀️🌧️", font=("Helvetica", 10), bg="#e0f7fa", fg="#00796b")

    title.pack(pady=(30, 10))
    subtitle.pack(pady=5)
    footer.pack(pady=(40, 0))

    root.mainloop()

# === Main Entry Point ===
if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()
    threading.Timer(1.5, open_browser).start()
    launch_gui()
