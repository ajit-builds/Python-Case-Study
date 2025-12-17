import matplotlib.pyplot as plt
import numpy as np

class HeatmapGenerator:
    def __init__(self, seat_map_obj):
        
        self.seat_map = seat_map_obj

    def generate_heatmap(self):
        data = self.seat_map.grid
        get_title = lambda flight: f"Seat Occupancy Heatmap: {flight}"
    
        plt.figure(figsize=(8, 6))    
       
        plt.imshow(data, cmap='YlGnBu', interpolation='nearest')
     
        plt.colorbar(label='Occupancy (1.0=Booked, 0.5=Blocked, 0=Vacant)')
        
        plt.title(get_title(self.seat_map.layout['aircraft_type']))
        plt.xlabel("Seat Columns (A-F)")
        plt.ylabel("Row Numbers")

        cols = self.seat_map.layout['columns']
        rows = self.seat_map.layout['rows']

        col_labels = [chr(65+i) for i in range(cols)] 
        
        plt.xticks(range(cols), col_labels)
        plt.yticks(range(rows), range(1, rows+1))
        
        plt.tight_layout()
        print("Heatmap generated.")
        return plt

    def analyze_patterns(self): 
        row_occupancy = np.sum(self.seat_map.grid, axis=1)
        
        plt.figure(figsize=(8, 4))
        
        # Draw the Bar Chart
        plt.bar(range(1, len(row_occupancy) + 1), row_occupancy, color='teal')
        
        plt.title("Seat Preference by Row (Trend Chart)")
        plt.xlabel("Row Number")
        plt.ylabel("Total Occupied Seats")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        print("Trend Chart generated.")
        return plt