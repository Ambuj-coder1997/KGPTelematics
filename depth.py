import streamlit as st
import random
import time

def generate_depth_of_operation(implement):
    if implement == "Mould Board Plough":
        return random.randint(0, 300)  # Adjust the range as needed for the implement
    elif implement == "Cultivator":
        return random.randint(0, 200)  # Adjust the range as needed for the implement
    elif implement == "Rotavator":
        return random.randint(0, 190)  # Adjust the range as needed for the implement

def check_depth_limit(implement, depth_of_operation):
    if implement == "Mould Board Plough" and depth_of_operation < 248:
        return "Safe Limit", "green"
    elif implement == "Cultivator" and depth_of_operation < 158:
        return "Safe Limit", "green"
    elif implement == "Rotavator" and depth_of_operation < 110:
        return "Safe Limit", "green"
    else:
        return "Over Limit", "red"

def display_parameters():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5; /* Change background color */
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
            background-color: #30181d; /* Change table header color */
            color: white; /* Change table header text color */
        }
        .safe {
            color: green;
        }
        .over-limit {
            color: red;
        }
        .checkbox-style {
            font-size: 36px;
            text-align: center;
            color: #30181d;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image("depth.png")

    with col3:
        st.write("")

    output_placeholder = st.empty()
    implement = st.selectbox("Select Implement", ["Mould Board Plough", "Cultivator","Rotavator"])

    show_checkbox = st.checkbox("Show Depth Limit Check", value=False, key="checkbox")
    if show_checkbox:
        while True:
            depth_of_operation = generate_depth_of_operation(implement)
            limit_status, color = check_depth_limit(implement, depth_of_operation)

            output_content = f"""
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Depth of Operation</td>
                    <td class="{limit_status.replace(' ', '-')}">{depth_of_operation} mm</td>
                </tr>
            </table>
            <p style="color:{color};">{limit_status}</p>
            """

            output_placeholder.markdown(output_content, unsafe_allow_html=True)
            time.sleep(1)  # Display for 1 second

            output_placeholder.empty()  # Clear the content for new data

def show_depth_page():
    st.markdown("<h3 style='text-align: center; color: #30181d;'>Real-time Depth of Operation Display</h3>",
                unsafe_allow_html=True)
    display_parameters()