import my_functions

def main():
    # Test: Personendaten erstellen
    person = my_functions.build_person("Simon", "Krainer", "male", 23)
    print("Personendaten:", person)

    # Test: Experiment erstellen
    experiment = my_functions.build_experiment("Herzfrequenz-Test", "2025-03-18", "Dr. Who", "Simon Krainer")
    print("Experiment:", experiment)

if __name__ == "__main__":
    main()
