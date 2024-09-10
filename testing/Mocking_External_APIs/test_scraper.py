# To run use: pytest Mocking_External_APIs/test_scraper.py
import requests
from scraper import fetch_hotel_data
from unittest.mock import patch


@patch('scraper.requests.get')
def test_fetch_hotel_data(mock_get):
    mock_get.return_value.json.return_value = {
        "hotel_id": 1, "name": "Hotel Example", "rating": 4.5
    }

    hotel_data = fetch_hotel_data(1)
    assert hotel_data == {"hotel_id": 1,
                          "name": "Hotel Example", "rating": 4.5}
    mock_get.assert_called_once_with("https://api.example.com/hotels/1")
