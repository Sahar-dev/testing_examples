# scraper.py
import requests


def fetch_hotel_data(hotel_id):
    url = f"https://api.example.com/hotels/{hotel_id}"
    response = requests.get(url)
    return response.json()
