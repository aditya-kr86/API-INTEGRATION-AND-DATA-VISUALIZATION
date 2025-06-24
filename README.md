NAME: ADITYA KUMAR    
INTERN ID: CT04DF1784     
DOMAIN: PYTHON PROGRAMMING      
DURATION: 30th May 2025 TO 30th June 2025      
MENTOR NAME: NEELA SANTHOSH KUMAR  
---
# API-INTEGRATION-AND-DATA-VISUALIZATION

# Weather Forecast Dashboard

This project provides a **real-time weather dashboard** built using [Streamlit](https://streamlit.io/), which visualizes weather forecast data for any city using the [OpenWeatherMap API](https://openweathermap.org/api). The dashboard features interactive charts for temperature and humidity trends, as well as key weather metrics.

## Features

- **City Search:** Enter any city name to get its 5-day weather forecast.
- **Key Metrics:** Displays current temperature, humidity, and weather condition.
- **Interactive Visualizations:**
  - Line chart for temperature trends.
  - Bar chart for humidity forecast.
- **Raw Data Table:** Explore the processed forecast data in a tabular format.
- **Responsive UI:** Built with Streamlit for an easy-to-use, web-based interface.

## Demo

![Screenshot 2025-06-24 113611](https://github.com/user-attachments/assets/a548eb3f-3e6a-4a82-ab34-d6cadf8ebf32)
![Screenshot 2025-06-24 113628](https://github.com/user-attachments/assets/6233cd8b-993f-4025-815c-8d3b814f4ef4)


## Getting Started

### Prerequisites

- Python 3.7+
- [Streamlit](https://docs.streamlit.io/)
- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/aditya-kr86/API-INTEGRATION-AND-DATA-VISUALIZATION.git
   cd API-INTEGRATION-AND-DATA-VISUALIZATION
   ```

2. **Install required packages:**
   ```bash
   pip install streamlit requests pandas plotly
   ```

3. **Obtain an OpenWeatherMap API Key:**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/appid) to get a free API key.
   - Replace the `API_KEY` variable in `weather_app.py` with your own API key.

### Running the App

```bash
streamlit run weather_app.py
```

This will open the dashboard in your browser. Enter a city name (e.g., "Delhi") to see the weather forecast and visualizations.

## File Overview

- `weather_app.py`: Main Streamlit application file. Handles UI, API integration, data processing, and plotting.

## Code Highlights

- **API Integration:** Uses `requests` to fetch 5-day/3-hour interval forecasts from OpenWeatherMap.
- **Data Processing:** Utilizes `pandas` for data transformation and time series handling.
- **Visualization:** Employs Plotly for beautiful, interactive plots within Streamlit.
- **Error Handling:** Displays user-friendly messages for invalid city names or API issues.

## Customization

- You can style the dashboard or add more weather metrics by extending the `process_data` function.
- To change default city, modify the second argument of `st.text_input`.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)

---

*Made with ❤️ by [Aditya Kumar](https://adityakr.me)*
