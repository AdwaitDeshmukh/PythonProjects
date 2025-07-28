import requests

API_ID = "your_id"
API_KEY = "your_key"
end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Enter the exercise you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 25
}

response = requests.post(url=end_point, headers=headers, json=body)
print(response.json())
