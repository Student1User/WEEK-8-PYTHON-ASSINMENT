

# Weather App

This project is a dynamic weather application built using **Flask** for the web interface, **Tkinter** for a graphical user interface (GUI), and **OpenWeatherMap API** for fetching weather data. The app provides users with current weather information for any city they enter, and displays animated weather icons and a stunning background for a more engaging experience.

## Features

* **Weather Information**: Get real-time weather data, including temperature, humidity, wind speed, and weather description.
* **Dynamic UI**: The weather data is presented with CSS animations, and animated weather icons (cartoon-like images) that change based on the weather conditions.
* **Background Animations**: A smooth gradient background transitions, creating a dynamic and atmospheric experience.
* **Flask & Tkinter Integration**: The Flask web server runs alongside a Tkinter window that notifies the user when the app has launched.

## Technologies Used

* **Python**: Backend logic for handling requests and data processing.
* **Flask**: Web framework for building the server and serving the weather data.
* **Tkinter**: A Python library used to create the GUI that launches alongside the web interface.
* **OpenWeatherMap API**: External API used to fetch real-time weather data based on the city name.
* **HTML/CSS**: For structuring and styling the web interface.


## Setup Instructions

Follow these steps to run the app on your local machine.

### Prerequisites

Ensure you have the following installed:

* **Python 3.x**: Download from [Python's official website](https://www.python.org/downloads/).
* **Flask**: Install Flask using the following command:

  ```bash
  pip install flask
  ```
* **Requests**: Install the Requests library (if not already installed):

  ```bash
  pip install requests
  ```
* **Tkinter**: Tkinter is typically bundled with Python. If not, you can install it using your package manager.

### Get OpenWeatherMap API Key

1. Sign up for an API key at [OpenWeatherMap](https://openweathermap.org/).
2. Replace `YOUR_API_KEY` in the `apis/openweathermap.py` file with your own key.

### File Structure

```
/weather_app
│
├── /static
│   ├── /icons           # Weather icon images (e.g., sunny.png, rainy.png)
│   └── styles.css       # CSS styles
│
├── /templates
│   └── index.html       # The main HTML template
│
├── apis
│   └── openweathermap.py # API logic for fetching weather data
│
├── main.py              # Main Python file to run the app
└── README.md            # Project README file
```

### Running the Application

1. **Clone the repository** or download the project files.

2. **Install dependencies** (if any):

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   Open your terminal or command prompt, navigate to the project folder, and run the following command:

   ```bash
   python main.py
   ```

   This will start the Flask server, and you should see the Tkinter GUI window appear, along with the Flask web app running. The browser window will automatically open with the Flask web app, and you can interact with it by entering the city name to retrieve weather information.

4. **Access the Web App**:

   * The web app will be accessible in your browser at:

     ```
     http://127.0.0.1:5000
     ```

### Example Usage

1. Open the app by running `python main.py`.
2. A Tkinter window will pop up saying "Weather App launched! Browser window will open."
3. The web browser will open automatically, displaying the weather interface.
4. Enter the name of a city (e.g., "London") and click the "Get Weather" button.
5. The page will display the weather information with animated weather icons and background effects.

### Weather Data

Once you enter a city, the following information is displayed:

* **Temperature**: The current temperature in Celsius.
* **Description**: A brief description of the weather (e.g., "Clear sky", "Cloudy", "Rainy").
* **Humidity**: The current humidity percentage.
* **Wind Speed**: The current wind speed in meters per second.

### Animations

* **Background Animation**: The background color will transition smoothly, creating a dynamic feel.
* **Weather Icons**: Animated weather icons rotate subtly to make the app more interactive.
* **Weather Data**: When displayed, the weather data will animate into view.

## Screenshots

1. **Tkinter GUI Window**:
![image](https://github.com/user-attachments/assets/dae89d5b-1b95-49a7-9799-a11b62a1e907)


2. **Web Interface**:
   ![image](https://github.com/user-attachments/assets/67dc26a8-4d79-4c3e-9dde-8bc1b73d7f8a)
   ![image](https://github.com/user-attachments/assets/9802cecb-659b-422f-9baa-98a6d35bc733)


## Customizations

You can further customize the app by:

* Adding more weather data or features like forecasts.
* Changing the look and feel of the app using CSS.
* Extending the functionality to show additional details (e.g., weekly forecasts, weather maps).

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Added new feature'`).
4. Push to your fork (`git push origin feature-branch`).
5. Create a new Pull Request to merge your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

