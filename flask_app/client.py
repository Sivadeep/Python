url = "http://localhost:5000/users"
import requests
resp = requests.get(url)
print resp.json()
resp=requests.post(url,json={'user':'user1','password':'pwd2'})