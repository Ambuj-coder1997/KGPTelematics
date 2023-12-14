import streamlit as st
import random
import time
from datetime import date

def generate_number_of_satellite():
    return random.randint(4, 7)

def generate_latitude(current_lat):
    return round(current_lat + random.uniform(0.0001, 0.0005), 5)

def generate_longitude(current_long):
    return round(current_long + random.uniform(0.0001, 0.0005), 5)

def generate_speed():
    return round(random.uniform(2.95, 3.15), 2)

def display_parameters():
    #st.title("Real-time Parameters Display")
    st.markdown(
        """
        <style>
        
        body {
            background-color: #f5f5f5; /* Change background color */
        }
        table {
            font-size: 20px; /* Set font size */
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
            background-color: #009688; /* Change table header color */
            color: white; /* Change table header text color */
        }
        .over-limit {
            color: red; /* Change font color for 'Over Limit' */
        }
        .safe-limit {
            color: green; /* Change font color for 'Safe Limit' */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    #st.image("logo.png", width=100)
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image("gps.png")

    with col3:
        st.write("")
    output_placeholder = st.empty()

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
                <td>Latitude (N) </td>
                <td>{current_lat}</td>
            </tr>
            <tr>
                <td>Longitude (E) </td>
                <td>{current_long}</td>
            </tr>
            <tr>
                <td>Speed (km/h)</td>
                <td>{speed}</td>
            </tr>
        </table>
        """

        output_placeholder.markdown(output_content, unsafe_allow_html=True)
        time.sleep(1)  # Display for 3 seconds

        output_placeholder.empty()  # Clear the content for new data
        #time.sleep(1)  # Add a small delay before displaying new data

def show_gps_page():
    st.markdown("<h3 style='text-align: center; color: DarkGreen;'>Real-time Geo-location Parameters Display</h3>", unsafe_allow_html=True)
    display_parameters()


