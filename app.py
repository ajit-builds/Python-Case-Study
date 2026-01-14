import streamlit as st
import pandas as pd
from seatmap_class import SeatMap
from heatmap_generator import generate_heatmap

st.title("Airline Seating Heatmap Generator")

uploaded_file = st.file_uploader("Upload a seating CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    fig = generate_heatmap(df)  # adapt this function
    st.pyplot(fig)
