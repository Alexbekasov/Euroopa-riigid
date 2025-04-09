from random import *
import tkinter as tk

def file_to_dict(f: str):
    country_capital = {}  # Dictionary {"Country": "Capital"}
    capital_country = {}  # Dictionary {"Capital": "Country"}
    countries = []  # List to store country names
    capitals = []

    file = open(f, 'r', encoding="utf-8-sig")  # Open file with utf-8-sig encoding
    for line in file:
        k, v = line.strip().split('-', 1)  # Split each line by '-'
        country_capital[k] = v  # Fill country_capital dictionary
        capital_country[v] = k  # Fill capital_country dictionary
        countries.append(k)  # Append the country name to countries list
        capitals.append(v)
    file.close()
    return country_capital, capital_country, countries, capitals  # Return the dictionaries and list

def save_to_file(f:str, country_capital:dict):
   file = open(f, 'w', encoding="utf-8-sig")  # Open file with utf-8-sig encoding
   for country, capital in country_capital.items():
        file.write(f"{country}-{capital}\n")
   file.close()

while True:
    # Call the function and assign the result to variables
    country_capital, capital_country, countries, capitals = file_to_dict("riigid_pealinnad.txt")

    # Display menu to the user
    print("Welcome to the Country & Capital Quiz!\n")
    print("Menu: \n\n1 -- Find a country by capital \n\n2 -- Find a capital by country\n\n3 -- Test your knowledge!\n\n0 -- Exit")
    
    action = int(input("\nPlease enter the number of your choice: "))

    if action in [0, 1, 2, 3]:

        ###################### MENU ACTIONS
        if action == 0:
            print("Goodbye!")
            break

        elif action == 1:
            while True:
                capital = input("Enter a capital city (in Estonian): ").capitalize()
                if capital in capitals:
                    print("The country is:", capital_country[capital])
                    ans = input("Is there a mistake in the country name? (y/n): ").lower()
                    if ans == "y":
                        del capital_country[capital]
                        country = input("Please enter the correct country name (in Estonian): ")
                        capital_country[capital] = country
                        country_capital[country] = capital
                        save_to_file("riigid_pealinnad.txt", country_capital)
                        print("The update has been saved successfully.")
                        break
                    else:
                        break
                else:
                    ans = input("No such capital found. Would you like to add this capital to the list? (y/n): ").lower()
                    if ans == "y":
                        country = input("Please provide the country for this capital (in Estonian): ")
                        capital_country[capital] = country
                        country_capital[country] = capital
                        save_to_file("riigid_pealinnad.txt", country_capital)
                        print("The capital has been added successfully.")
                        break
                    else:
                        break

        elif action == 2:
            while True:
                country = input("Enter a country (in Estonian): ").capitalize()
                if country in countries:
                    print("The capital is:", country_capital[country])
                    ans = input("Is there a mistake in the capital name? (y/n): ").lower()
                    if ans == "y":
                        del country_capital[country]
                        capital = input("Please enter the correct capital name (in Estonian): ")
                        country_capital[country] = capital
                        save_to_file("riigid_pealinnad.txt", country_capital)
                        print("The update has been saved successfully.")
                        break
                    else:
                        break
                    
                else:
                    ans = input("No such country found. Would you like to add this country to the list? (y/n): ").lower()
                    if ans == "y":
                        capital = input("Please provide the capital for this country (in Estonian): ")
                        country_capital[country] = capital
                        save_to_file("riigid_pealinnad.txt", country_capital)
                        print("The country has been added successfully.")
                        break
                    else:
                        break

        elif action == 3:
            p = 0
            print("You will be given 10 countries or capitals, and you must guess the correct pair!\n")
            for i in range(1, 11):
                c_or_c = randint(1, 2)  # Randomly choose between country or capital
                if c_or_c == 2:
                    country = choice(countries)
                    capital = country_capital[country]
                    print(f"Country: {country}")
                    ans = input("What is the capital? ").capitalize()
                    if ans == capital:
                        print("Correct!\n")
                        p += 1
                    else:
                        print("Wrong...\n")

                elif c_or_c == 1:
                    capital = choice(capitals)
                    country = capital_country[capital]
                    print(f"Capital: {capital}")
                    ans = input("What is the country? ").capitalize()
                    if ans == country:
                        print("Correct!\n")
                        p += 1
                    else:
                        print("Wrong...\n")
            score = p * 100 / 10
            print(f"Your score: {score}%")

    else:
        print("Invalid input! Please select a valid option.")
