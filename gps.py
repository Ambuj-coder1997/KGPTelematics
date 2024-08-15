import streamlit as st
import random
import time
from datetime import date
import folium
from streamlit_folium import st_folium

def generate_number_of_satellite():
    return random.randint(4, 7)

def generate_latitude(current_lat):
    return round(current_lat + random.uniform(0.0001, 0.0005), 5)

def generate_longitude(current_long):
    return round(current_long + random.uniform(0.0001, 0.0005), 5)

def generate_speed():
    return round(random.uniform(2.95, 3.15), 2)

def display_parameters():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5;
        }
        table {
            font-size: 20px;
            border-collapse: collapse;
            width: 50%;
            margin-bottom: 10px;
            margin-left: auto;
            margin-right: auto;
        }
        th, td {
            padding: 0px;
            text-align: center;
        }
        th {
            background-color: #009688;
            color: white;
        }
        .over-limit {
            color: red;
        }
        .safe-limit {
            color: green;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image("gps.png")

    with col3:
        st.write("")
    
    output_placeholder = st.empty()
    map_placeholder = st.empty()

    current_lat = 22.31278
    current_long = 87.33152

    while True:
        num_satellite = generate_number_of_satellite()
        today = date.today().strftime("%d-%m-%Y")
        current_lat = generate_latitude(current_lat)
        current_long = generate_longitude(current_long)
        speed = generate_speed()

        output_content = f"""
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Number of Satellite</td>
                <td>{num_satellite}</td>
            </tr>
            <tr>
                <td>Date</td>
                <td>{today}</td>
            </tr>
            <tr>
                <td>Latitude (N)</td>
                <td>{current_lat}</td>
            </tr>
            <tr>
                <td>Longitude (E)</td>
                <td>{current_long}</td>
            </tr>
            <tr>
                <td>Speed (km/h)</td>
                <td>{speed}</td>
            </tr>
        </table>
        """

        output_placeholder.markdown(output_content, unsafe_allow_html=True)
        
        # Create a Folium map centered on the current coordinates
        m = folium.Map(location=[current_lat, current_long], zoom_start=15)
        folium.Marker(
            location=[current_lat, current_long],
            popup=f"Lat: {current_lat}, Long: {current_long}, Speed: {speed} km/h"
        ).add_to(m)

        # Display the map in the Streamlit app
        map_placeholder.st_folium(m, width=700, height=500)

        time.sleep(3)  # Display for 3 seconds

        output_placeholder.empty()  # Clear the content for new data
        map_placeholder.empty()  # Clear the map for new data

def show_gps_page():
    st.markdown("<h3 style='text-align: center; color: DarkGreen;'>Real-time Geo-location Parameters Display</h3>", unsafe_allow_html=True)
    display_parameters()

