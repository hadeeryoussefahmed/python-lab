import requests

class WeatherApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.weatherapi.com/v1'

    def get_current_temperature(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Error getting current temperature")
        data = response.json()
        return data['current']['temp_c']

    def get_temperature_after(self, city, days, hour=None):
        url = f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Error getting temperature forecast")
        data = response.json()
        if hour is not None:
            for forecast in data['forecast']['forecastday']:
                if forecast['date'] == f"{days}-{'{:02d}'.format(hour)}-{'{:02d}'.format(1)}":
                    return forecast['hour'][0]['temp_c']
            raise Exception("Error getting temperature forecast")
        return data['forecast']['forecastday'][0]['day']['avgtemp_c']

    def get_lat_and_long(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Error getting location")
        data = response.json()
        return (data['location']['lat'], data['location']['lon'])


weather = WeatherApiClient("16e566c8a5884448862202852232408")
print(weather.get_current_temperature('cairo'))
print(weather.get_temperature_after('cairo', 1))
print(weather.get_lat_and_long('cairo'))