import http.client
import json
socketserver.TCPServer.allow_reuse_adress = True
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET","/drug/label.json?search=active_ingredient:acetylsalicylic&limit=4", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()
repos = json.loads(repos_raw)
for i in range(len(repos["results"])):
    try:
        print("The name of the manufactor is" , repos['results'][i]['openfda']['manufacturer_name'])
    except KeyError:
        pass
