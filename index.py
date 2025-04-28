import requests, os
from dotenv import load_dotenv

load_dotenv()
ACCES_KEY = os.getenv("ACCES_KEY")
base_url = "https://api.unsplash.com"
api_url =  f"{base_url}/photos/random"

headers = {
  "Authorization": f"Client-ID {ACCES_KEY}"
}

params = {
  "query": "bird"
}

response = requests.get(api_url, headers=headers, params=params)

def save_img(filename, image):
  with open (f"{filename}.jpg",'wb') as file:
    file.write(image.content)
    print(f"Image was saved: {filename}.jpg")



if response.status_code == 200:
  data = response.json()
  bird_img = data['urls']['full']
  print(f"Bird: ", bird_img)
  image_resp = requests.get(bird_img)
  if image_resp.status_code == 200:
      filename = input("Enter filename: ")
      save_img(filename, image_resp)
  else:
    print("Failed image")
else:
  print(f"Error: {response.status_code}")
