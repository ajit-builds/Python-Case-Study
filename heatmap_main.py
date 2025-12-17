from seatmap_class import SeatMap
from heatmap_generator import HeatmapGenerator

def main():
    print("--- Starting Airline Heatmap System ---")


    my_flight = SeatMap()

    # which plane to load
    print("Available: Airbus A320, Boeing 737, Embraer E175,Boeing 787 Dreamliner")
    target_name = input("Enter Aircraft Name: ") 

    print("Loading Aircraft Layout...")
    
    
    my_flight.load_layout('layout.json', target_name)

    print("Loading Passenger Manifest...")
    my_flight.load_seating_data('seating.csv')


    generator = HeatmapGenerator(my_flight)

    # 4. DRAW THE CHARTS
    print("Generating visuals...")
    hm_plot = generator.generate_heatmap()
    hm_plot.show() 

    trend_plot = generator.analyze_patterns()
    trend_plot.show()

    

if __name__ == "__main__":
    main()

    