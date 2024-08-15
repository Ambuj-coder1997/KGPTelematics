import streamlit as st
import random
import time

def generate_pto_torque():
    return random.randint(210, 230)

def display_parameters():
    #st.title("Real-time Parameters Display")
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
        </style>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image("pto.png")

    with col3:
        st.write("")


    output_placeholder = st.empty()

    while True:
        pto_torque = generate_pto_torque()

        output_content = f"""
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>PTO Torque</td>
                <td>{pto_torque} Nm</td>
            </tr>
        </table>
        """

        output_placeholder.markdown(output_content, unsafe_allow_html=True)
        time.sleep(1)  # Display for 3 seconds

        output_placeholder.empty()  # Clear the content for new data
        #time.sleep(1)  # Add a small delay before displaying new data
def show_pto_page():
    st.markdown("<h3 style='text-align: center; color: #30181d;'>Real-time PTO Torque Display</h3>",
                unsafe_allow_html=True)
    display_parameters()