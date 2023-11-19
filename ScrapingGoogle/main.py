import requests

API_KEY = open("API_KEY").read()
SEARCH_ENGINE_ID = open("SEARCH_ENGINE_ID").read()

search_query = "Anarquismo"

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "q" : search_query,
    "key" : API_KEY,
    "cx" : SEARCH_ENGINE_ID,
    # "searchType" : "image",
    # "fileType" : "pdf",
    # "lr" : "lang_en",
    # "gl" : "us",
    # "dateRestrict": "2021-01-01:2021-12-31",
}

response = requests.get(url, params=params)
results = response.json()

results2 = response.json()["items"]
# print(results)

# if "items" in results:
#     print(results["items"][0]["link"])
    

for item in results2:
    print(item["link"])