import json
import requests
from rich import print

from classes import exceptions

class SearchEngine():
	def __init__(self, user_request, API_KEY):
		self.__user_request = user_request
		self.__user_request = self.__user_request.replace(" ", "+")
		self.__url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={self.__user_request}"
		self.__headers = {
			"X-User-Agent": "desktop",
			"X-Proxy-Location": "EU",
			"X-RapidAPI-Host": "google-search3.p.rapidapi.com",
			"X-RapidAPI-Key": API_KEY
		}
		self.__response = requests.request("GET", self.__url, headers=self.__headers)
		self.__json_data = json.loads(self.__response.text).get("results")

	
	def parse(self):
		if self.__json_data is None:
			raise(exceptions.MissingApiKey("\n\nYou are don't have API_KEY! Please, get it in https://rapidapi.com/, and subscribe to https://rapidapi.com/apigeek/api/google-search3/ api!"))
		else:
			for result in self.__json_data:
				print(f"[b blue]{result.get('title')}\n"
				      f"[purple]{result.get('link')}\n"
				      f"[green]{result.get('description')}\n\n")