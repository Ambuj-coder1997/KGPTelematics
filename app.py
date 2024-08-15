import streamlit as st
from gps import show_gps_page
from speednslip import show_speednslip_page
from fc import show_fc_page
from pto import show_pto_page
from draft import show_draft_page
from depth import show_depth_page
from fefficiency import show_fefficiency_page
from PIL import Image
image = Image.open("logo.png")
st.sidebar.image(image)
st.sidebar.title("AI-IoT based Tractor Advisory System")
page = st.sidebar.selectbox("Select an option", ("GPS Position", "Speed and Slip","Fuel Consumption","Draft Requirement","Depth of Operation","PTO Torque","Field Capacity & Field Efficiency"))

if page == "GPS Position":
    show_gps_page()
else:
    if page == "Speed and Slip":
        show_speednslip_page()
    else:
        if page == "Fuel Consumption":
            show_fc_page()
        else:
            if page == "PTO Torque":
                show_pto_page()
            else:
                if page == "Draft Requirement":
                    show_draft_page()
                else:
                    if page == "Depth of Operation":
                        show_depth_page()
                    else:
                        show_fefficiency_page()


