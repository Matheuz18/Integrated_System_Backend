import requests
import json

headers = {'Content-Type': 'application/json'}

url = "http://192.168.0.42:5005"

data = {
    "user":"matheus.coelho",
    "psw": "1234"
}

def try_login(infos):
    resp = requests.post(url+"/api/cadastrar", headers=headers, data=json.dumps(infos))
    print("Status Code: " + str(resp.status_code))
    print(resp.text)


try_login(data)





