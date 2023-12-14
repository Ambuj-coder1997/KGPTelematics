import streamlit as st
import random
import time

def generate_lower_right_link_draft():
    return round(random.uniform(2.09, 4.01), 2)

def generate_lower_left_link_draft():
    return round(random.uniform(2.19, 3.84), 2)

def generate_upper_link_draft():
    return round(random.uniform(-3.11, -0.71), 2)

def generate_total_draft():
    return round(random.uniform(3.5, 8.7), 2)

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
            background-color: #062b01; /* Change table header color */
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
        st.image("draft.png")

    with col3:
        st.write("")

    output_placeholder = st.empty()

    while True:
        lower_right_link_draft = generate_lower_right_link_draft()
        lower_left_link_draft = generate_lower_left_link_draft()
        upper_link_draft = generate_upper_link_draft()
        total_draft = generate_total_draft()

        output_content = f"""
        <table>
            <tr>
                <th>Parameter</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Lower Right Link Draft</td>
                <td>{lower_right_link_draft}</td>
            </tr>
            <tr>
                <td>Lower Left Link Draft</td>
                <td>{lower_left_link_draft}</td>
            </tr>
            <tr>
                <td>Upper Link Draft</td>
                <td>{upper_link_draft}</td>
            </tr>
            <tr>
                <td>Total Draft</td>
                <td>{total_draft}</td>
            </tr>
        </table>
        """

        output_placeholder.markdown(output_content, unsafe_allow_html=True)
        time.sleep(1)  # Display for 3 seconds

        output_placeholder.empty()  # Clear the content for new data
        #time.sleep(1)  # Add a small delay before displaying new data

def show_draft_page():
    st.markdown("<h3 style='text-align: center; color: #062b01;'>Real-time Draft Requirement Display</h3>",
                unsafe_allow_html=True)
    display_parameters()



