from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Average speeds in km/h
WALKING_SPEED = 5          # Walking speed
DRIVING_SPEED = 60         # Average car driving speed in urban areas
MOTORCYCLE_SPEED = 50      # Average motorcycle speed

# Initialize geolocator
geolocator = Nominatim(user_agent="distance_calculator")

def get_location_coordinates(location):
    """
    Get the geographical coordinates (latitude and longitude) of a location.
    """
    try:
        loc = geolocator.geocode(location)
        if loc:
            return (loc.latitude, loc.longitude)
        else:
            print(f"Could not find location: {location}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None