import streamlit as st
from seatmap_class import SeatMap
from heatmap_generator import HeatmapGenerator

st.set_page_config(page_title="Airline Heatmap Generator", layout="centered")

st.title("✈️ Airline Seating Heatmap Generator")

st.write("Select an aircraft type and generate seat occupancy heatmap.")

# Aircraft options
aircraft_options = [
    "Airbus A320",
    "Boeing 737",
    "Embraer E175",
    "Boeing 787 Dreamliner"
]

selected_aircraft = st.selectbox("Select Aircraft Type", aircraft_options)

if st.button("Generate Heatmap"):

    my_flight = SeatMap()

    st.info("Loading aircraft layout...")
    my_flight.load_layout("layout.json", selected_aircraft)

    st.info("Loading seating data...")
    my_flight.load_seating_data("seating.csv")

    generator = HeatmapGenerator(my_flight)

    st.success("Heatmap Generated!")

    heatmap_fig = generator.generate_heatmap()
    st.pyplot(heatmap_fig)

    st.success("Trend Analysis Generated!")

    trend_fig = generator.analyze_patterns()
    st.pyplot(trend_fig)
