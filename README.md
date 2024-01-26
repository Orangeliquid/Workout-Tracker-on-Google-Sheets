# Workout Tracker

## Overview
This Python script uses the Nutritionix and Sheety APIs to track your exercises and log them into a Google Sheet. It prompts you to input the exercise you did, fetches data from Nutritionix to estimate calories burned, and then logs the information in a Google Sheet via the Sheety API.

## Prerequisites
Before running the script, make sure you have the following environmental variables set:
- `GENDER`: Your gender (string).
- `WEIGHT_KG`: Your weight in kilograms (integer).
- `HEIGHT_CM`: Your height in centimeters (float).
- `AGE`: Your age (integer).
- `APP_ID`: Your Nutritionix API application ID.
- `API_KEY`: Your Nutritionix API key.
- `NUTRITION_ENDPOINT`: Nutritionix exercise endpoint.
- `SHEET_ENDPOINT`: Sheety endpoint for Google Sheets.
- `BEARER_TOKEN`: Bearer token for Sheety authentication.

## Usage
1. Run the script using:
    ```bash
    python fitness_tracker.py
    ```
2. Input the exercise you did when prompted.
3. The script will estimate calories burned using Nutritionix and log the exercise information into a Google Sheet via Sheety.

## API Limits
- Nutritionix allows 2 active users for free.
- Sheety allows 200 free calls per month.

## Note
- Ensure that all environmental variables are set correctly before running the script.

## Dependencies
- requests
- os
- datetime

## License
This project is licensed under the [MIT License](LICENSE).
