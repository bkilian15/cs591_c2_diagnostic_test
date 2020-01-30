import requests


r = requests.post("http://localhost:5000/auth/register", json={'email':'benjaminsmail@gmail.com',
                                                           'password':'password634'})

print(r.json()['message'])
