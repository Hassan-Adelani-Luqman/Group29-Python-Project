from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Average speeds in km/h
WALKING_SPEED = 5          # Walking speed
DRIVING_SPEED = 60         # Average car driving speed in urban areas
MOTORCYCLE_SPEED = 50      # Average motorcycle speed

# Initialize geolocator
geolocator = Nominatim(user_agent="distance_calculator")

def get_location_coordinates(location):
    try:
        location = geolocator.geocode(location)
        if location:
            return (location.latitude, location.longitude)
        else:
            print("Could not find location:", location)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def calculate_distance_and_time(start_location, destination_location):
    # Get coordinates for each location
    start_coords = get_location_coordinates(start_location)
    dest_coords = get_location_coordinates(destination_location)
    
    if start_coords and dest_coords:
        # Calculate distance
        distance = geodesic(start_coords, dest_coords).kilometers
        
        # Calculate time estimates for each mode
        time_walking = distance / WALKING_SPEED
        time_driving = distance / DRIVING_SPEED
        time_motorcycle = distance / MOTORCYCLE_SPEED

        # Display results
        print(f"Distance between {start_location} and {destination_location}: {distance:.2f} km")
        print(f"Estimated time if walking: {time_walking:.2f} hours")
        print(f"Estimated time if driving: {time_driving:.2f} hours")
        print(f"Estimated time if on motorcycle: {time_motorcycle:.2f} hours")
    else:
        print("Could not calculate distance or time due to location errors.")

# User input
start_location = input("Enter your current location: ")
destination_location = input("Enter your destination: ")

# Calculate and display results
calculate_distance_and_time(start_location, destination_location)
