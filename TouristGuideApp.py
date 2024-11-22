
from distance_calculator import calculate_distance_and_time

class TouristAttraction:
    def __init__(self, name, description, location, best_time, entry_fee, activities):
        self.name = name
        self.description = description
        self.location = location
        self.best_time = best_time
        self.entry_fee = entry_fee
        self.activities = activities

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Location: {self.location}")
        print(f"Best Time to Visit: {self.best_time}")
        print(f"Entry Fee: {self.entry_fee}")
        print(f"Activities: {self.activities}\n")

class TouristGuideApp:
 
    def main_menu(self):
        while True:
            print("\n--- Tourist Guide ---")
            print("1. View Countries")
            print("2. Search for an Attraction")
            print("3. Calculate Distance and Cost")
            print("4. Exit")
            choice = input("Select an option (1-4): ")
            
            if choice == '1':
                self.display_countries()
            elif choice == '2':
                self.search_attraction()
            elif choice == '3':
                self.calculate_distance_and_cost()
            elif choice == '4':
                print("Exiting the Tourist Guide.")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_countries(self):
        print("\nCountries:")
        for idx, country in enumerate(self.attractions, start=1):
            print(f"{idx}. {country}")
        country_choice = input("Select a country by name or number: ")
        
        if country_choice.isdigit():
            country_list = list(self.attractions.keys())
            if 1 <= int(country_choice) <= len(country_list):
                country_name = country_list[int(country_choice) - 1]
                self.display_attractions(country_name)
            else:
                print("Invalid number.")
        elif country_choice in self.attractions:
            self.display_attractions(country_choice)
        else:
            print("Country not found.")

    def display_attractions(self, country_name):
        print(f"\n--- Tourist Attractions in {country_name} ---")
        for idx, attraction in enumerate(self.attractions[country_name], start=1):
            print(f"{idx}. {attraction.name}")
        attraction_choice = input("Select an attraction by number or type 'back' to return: ")

        if attraction_choice.isdigit() and 1 <= int(attraction_choice) <= len(self.attractions[country_name]):
            self.attractions[country_name][int(attraction_choice) - 1].display_info()
        elif attraction_choice.lower() == 'back':
            return
        else:
            print("Invalid choice.")

    def search_attraction(self):
        search_name = input("Enter the name of the attraction to search for: ").lower()
        found = False
        for country, attractions in self.attractions.items():
            for attraction in attractions:
                if search_name in attraction.name.lower():
                    print(f"\nFound in {country}:")
                    attraction.display_info()
                    found = True
        if not found:
            print("No matching attractions found.")

    def calculate_distance_and_cost(self):
        user_location = input("Enter your current location: ")
        destination_name = input("Enter the name of the attraction you want to visit: ")
        
        for country, attractions in self.attractions.items():
            for attraction in attractions:
                if destination_name.lower() in attraction.name.lower():
                    result = calculate_distance_and_time(user_location, attraction.location)
                    if result:
                        print(f"Distance to {attraction.name}: {result['distance_km']:.2f} km")
                        print(f"Walking Time: {result['time_walking_hr']:.2f} hours")
                        print(f"Driving Time: {result['time_driving_hr']:.2f} hours")
                        print(f"Motorcycle Time: {result['time_motorcycle_hr']:.2f} hours")
                    else:
                        print("Could not calculate distance and time.")
                    return
        print("Attraction not found.")

if __name__ == "__main__":
    app = TouristGuideApp()
    app.main_menu()
