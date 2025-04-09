import sys
import requests
from collections import defaultdict
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("תחזית מזג אוויר לשבוע")
        self.setGeometry(300, 100, 400, 600)
        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)

        city_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.get_weather_btn = QPushButton("Get Weather")
        self.get_weather_btn.clicked.connect(self.get_weather)
        city_layout.addWidget(self.city_input)
        city_layout.addWidget(self.get_weather_btn)
        self.main_layout.addLayout(city_layout)

        self.temp_label = QLabel("Temperature will appear here")
        self.temp_label.setFont(QFont("Arial", 20))
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.temp_label)

        self.description_label = QLabel("Weather description will appear here")
        self.description_label.setFont(QFont("Arial", 20))
        self.description_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.description_label)

        self.icon_label = QLabel("⛅")
        self.icon_label.setFont(QFont("Arial", 50))
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.icon_label)

        self.forecast_text_edit = QPlainTextEdit()
        self.forecast_text_edit.setReadOnly(True)
        self.forecast_text_edit.setPlaceholderText(
            "Forecast for the upcoming week will appear here")
        self.main_layout.addWidget(self.forecast_text_edit)

        self.setLayout(self.main_layout)

    def get_weather(self):
        api_key = "ed318647442addba36a2f24a01ad7077"
        city_name = self.city_input.text().strip()
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()
        self.display_weather(data)

    def display_weather(self, data):
        forecast = data["list"][0]
        temp_c = forecast["main"]["temp"]
        weather_description = forecast["weather"][0]["description"]

        self.temp_label.setText(f"{temp_c:.1f} °C")
        self.description_label.setText(weather_description)

        icon_code = forecast["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_response.raise_for_status()
        pixmap = QPixmap()
        pixmap.loadFromData(icon_response.content)
        self.icon_label.setPixmap(pixmap)

        daily_temps = defaultdict(list)
        for fc in data["list"]:
            date = fc.get("dt_txt", "").split()[0]
            if date:
                daily_temps[date].append(fc["main"]["temp"])

        forecast_text = "\n".join(
            f"{date}: {sum(temps)/len(temps):.1f} °C" for date, temps in daily_temps.items())
        self.forecast_text_edit.setPlainText(forecast_text)


def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
