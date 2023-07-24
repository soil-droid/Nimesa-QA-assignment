import requests

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

while True:
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    option = input("Enter an option: ")

    if option == "1":
        response = requests.get(url)
        data = response.json()
        weather = data["list"][0]["weather"][0]["description"]
        print(f"Weather: {weather}")
    elif option == "2":
        response = requests.get(url)
        data = response.json()
        wind_speed = data["list"][0]["wind"]["speed"]
        print(f"Wind Speed: {wind_speed}")
    elif option == "3":
        response = requests.get(url)
        data = response.json()
        pressure = data["list"][0]["main"]["pressure"]
        print(f"Pressure: {pressure}")
    elif option == "0":
        break
    else:
        print("Invalid option. Please try again.")