import requests
from datetime import datetime

API_ID = "02c82649"
API_KEY = "8e155d9aea6553f5d075136ab5d54209"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/e7e36a5ace33f7e20350048cd9b28918/workouts/workouts"

exercise_input = input("Enter the exercise you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 25
}

# Request Nutritionix API
response = requests.post(url=nutritionix_endpoint, headers=headers, json=body)
data = response.json()
print("Nutritionix response:", data)  

for exercise in data["exercises"]:
    duration = exercise.get("duration_min", 0)
    calories = exercise.get("nf_calories", 0)

    workout_data = {
        "workout": {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": duration,   
            "calories": calories    
        }
    }

    # POST to Sheety API
    sheety_response = requests.post(url=sheety_endpoint, json=workout_data)
    print("Sheety response:", sheety_response.text)  
