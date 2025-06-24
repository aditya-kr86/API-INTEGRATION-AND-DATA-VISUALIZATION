import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_KEY = 'd67f4c6e4dd22025bc01ee4b94e96392'

def fetch_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_data(data):
    forecast = data['list']
    df = pd.DataFrame([{
        "datetime": item["dt_txt"],
        "temp": item["main"]["temp"],
        "humidity": item["main"]["humidity"],
        "weather": item["weather"][0]["description"]
    } for item in forecast])
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df

# ---------- Streamlit UI ----------
st.set_page_config(layout="wide", page_title="Weather Forecast Dashboard")
st.title("🌤️ Real-time Weather Dashboard")

city = st.text_input("Enter city name:", "Delhi")

if city:
    data = fetch_weather(city)
    if data:
        df = process_data(data)

        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Current Temp", f"{df.iloc[0]['temp']} °C")
        col2.metric("💧 Humidity", f"{df.iloc[0]['humidity']}%")
        col3.metric("⛅ Condition", df.iloc[0]['weather'].capitalize())

        st.subheader("📈 5-Day Temperature Trend")
        fig1 = px.line(df, x="datetime", y="temp", title="Temperature Forecast", markers=True)
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("💧 Humidity Trend")
        fig2 = px.bar(df, x="datetime", y="humidity", title="Humidity Forecast", color="humidity", color_continuous_scale='Blues')
        st.plotly_chart(fig2, use_container_width=True)

        with st.expander("📋 Raw Forecast Data"):
            st.dataframe(df)
    else:
        st.error("City not found or API error.")
