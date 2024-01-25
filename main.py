import requests
import os
from datetime import datetime as dt

# Nutritionix allows 2 active users for free
# Sheety allows 200 free calls per month

GENDER = os.environ["GENDER"]  # string
WEIGHT_KG = int(os.environ["WEIGHT_KG"])  # int
HEIGHT_CM = float(os.environ["HEIGHT_CM"])  # float
AGE = int(os.environ["AGE"])  # int

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

nutritionix_exercise_endpoint = os.environ["NUTRITION_ENDPOINT"]
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_prompt = input("What exercise did you do?: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

nutritionix_body = {
    "query": exercise_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_body, headers=nutritionix_headers)
result = response.json()

result_narrowed = result["exercises"][0]
duration = result_narrowed["duration_min"]
exercise_name = result_narrowed["name"].title()
calories_burned = result_narrowed["nf_calories"]

# POST request for Google Sheets row
today_date_formatted = dt.now().strftime("%m/%d/%Y")
now_time = dt.now().strftime("%X")

sheet_inputs = {
    "workout": {
        "date": today_date_formatted,
        "time": now_time,
        "exercise": exercise_name,
        "duration(mins)": int(duration),
        "calories": calories_burned
    }
}

bearer_token = os.environ["BEARER_TOKEN"]

bearer_headers = {
    'Authorization': bearer_token
}
sheet_post = requests.post(
    sheety_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
print(sheet_post.text)
