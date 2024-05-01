import json
import requests

# completion_query = 'NeuralNine'
completion_query = 'Nvidia'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.gent"
}

response = requests.get(
    f"https://www.google.com/complete/search?client=chrome&q={completion_query}"
)

for completion in json.loads(response.text)[1]:
    print(completion)
