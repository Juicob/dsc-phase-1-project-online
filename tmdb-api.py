import pandas as pd
import requests
import json
import api_info
url = f"https://api.themoviedb.org/3/genre/movie/list?{api_key}&language=en-US"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data = response.json()
df = pd.DataFrame.from_dict(data['genres'])
print(df)
df.to_csv(r'C:\Users\Juice\Python_Projects\flatiron\class-materials\section01\projects\dsc-phase-1-project-online\unzipped_data\genre_ids.csv')
# print(response.text.encode('utf8'))
