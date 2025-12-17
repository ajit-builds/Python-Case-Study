import json #For importing Json data
import csv #for importing CSV data
import numpy as np #importing numpy

def validate_seat_data(func):  
    def wrapper(self, *args, **kwargs):  
        if not self.layout:  
            print("Error: Seat layout data is not loaded.")
            return None
        return func(self, *args, **kwargs) 
    return wrapper 

class SeatMap: 
    def __init__(self): 
        self.layout = {}  #Layout as an empty dictionary
        self.grid = []    # Grid as an empty list
    
    
    def load_layout(self, file_path, aircraft_name):
    
        with open(file_path, "r") as f:
            fleet_data = json.load(f)  #Load the list of all planes
            
        # 2. Search for the plane by name
        selected_plane = None
        for plane in fleet_data:
            if plane['aircraft_type'] == aircraft_name:
                selected_plane = plane
                break
        
        # 3. If found, set up the grid
        if selected_plane:
            self.layout = selected_plane
            self.grid = np.zeros((self.layout['rows'], self.layout['columns']))
            print(f" Loaded Aircraft: {self.layout['aircraft_type']}")
        else:
            print(f" Error: Could not find '{aircraft_name}' in {file_path}")
            self.layout = {} 
    
    @validate_seat_data
    def load_seating_data(self, filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            all_passengers = [row for row in reader]
        self._map_seats_to_grid(all_passengers)

    def _map_seats_to_grid(self, passenger_list):
        letter_to_index = {chr(65+i): i for i in range(26)} 
        
        for p in passenger_list:
            seat_code = p['seat_number']
            status = p['status']

            try:
                # separate "1" and "A"
                row_str = seat_code[:-1] 
                col_str = seat_code[-1]   

                # Convert to computer numbers (0-based index)
                row_idx = int(row_str) - 1        
                col_idx = letter_to_index[col_str] 

              
                # 1.0 = Booked, 0.5 = Blocked, 0.0 = Vacant
                if status == 'booked':
                    self.grid[row_idx][col_idx] = 1.0 # Booked seat
                elif status == 'blocked':
                    self.grid[row_idx][col_idx] = 0.5 # Blocked seat
                    
            except Exception as e:
                print(f"Skipping invalid seat: {seat_code}")