from classes import engine
import json

if __name__ == '__main__':
	with open('config.json') as f:
		data = json.load(f)
		api_key = data.get('api_key')
	
	search = engine.SearchEngine(input("Search request: "), api_key)
	search.parse()