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
    def __init__(self):
        self.attractions = {
            "Kenya": [
                TouristAttraction("Maasai Mara", "Famous wildlife reserve", "Narok County", "July to October", "$70", "Game drives, bird watching"),
                TouristAttraction("Mount Kenya", "Highest mountain in Kenya", "Central Kenya", "December to March", "$50", "Hiking, mountain climbing")
            ],
            "Egypt": [
                TouristAttraction("Pyramids of Giza", "Ancient pyramids", "Giza", "All year round", "$20", "Sightseeing, photography"),
                TouristAttraction("Nile River Cruise", "Scenic river cruise", "Various locations", "October to April", "$100", "Boat rides, sightseeing")
            ]
        }

    def main_menu(self):
        while True:
            print("\n--- Tourist Guide ---")
            print("1. View Countries")
            print("2. Search for an Attraction")
            print("3. Exit")
            choice = input("Select an option (1-3): ")
            
            if choice == '1':
                self.display_countries()
            elif choice == '2':
                self.search_attraction()
            elif choice == '3':
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

if __name__ == "__main__":
    app = TouristGuideApp()
    app.main_menu()
