import streamlit as st
import random
import time

def generate_field_capacity():
    return round(random.uniform(0.35, 0.48), 2)

def generate_field_efficiency():
    return random.randint(84, 87)

def display_parameters():
    #st.title("Real-time Parameters Display")
    st.markdown(
        """
        <style>
        body {
            background-color: #01403f; /* Change background color */
        }
        table {
            font-size: 24px; /* Set font size */
            border-collapse: collapse;
            width: 50%;
            margin-bottom: 20px;
            margin-left: auto;
            margin-right: auto;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #009688; /* Change table header color */
            color: white; /* Change table header text color */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image("f.png")

    with col3:
        st.write("")

    output_placeholder = st.empty()

    while True:
        field_capacity = generate_field_capacity()
        field_efficiency = generate_field_efficiency()

        output_content = f"""
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Field Capacity (ha/h)</td>
                <td>{field_capacity}</td>
            </tr>
            <tr>
                <td>Field Efficiency (%)</td>
                <td>{field_efficiency}</td>
            </tr>
        </table>
        """

        output_placeholder.markdown(output_content, unsafe_allow_html=True)
        time.sleep(3)  # Display for 3 seconds

        output_placeholder.empty()  # Clear the content for new data
        #time.sleep(1)  # Add a small delay before displaying new data

def show_fefficiency_page():
    st.markdown("<h3 style='text-align: center; color: #01403f;'>Real-time Field Capacity & Field Efficiency Display</h3>",
                unsafe_allow_html=True)
    display_parameters()

