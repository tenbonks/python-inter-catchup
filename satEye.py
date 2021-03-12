import requests
import json
from datetime import datetime


parameters = {
    "lat": 50.863484,
    "lon": -0.963463
}

response = requests.get(
    "http://api.open-notify.org/iss-pass.json",
    params=parameters)


pass_times = response.json()["response"]

# Itterate through pass_times response to get a list of the risetime values
rise_times = list()
for d in pass_times:
    time = d['risetime']
    rise_times.append(time)

print(rise_times)

times = []

for rt in rise_times:
    time = datetime.fromtimestamp(rt)
    times.append(times)
    print(time)

print(times)


# Pretty print a json object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# jprint(pass_times)

# Printing of the response data
# print("-------------------- \
#      \n Status Code: " + str(response.status_code),
#       end="\n--------------------")
# print("\n Headers: " + str(response.headers),
#       end="\n--------------------")
# print("\n Request: " + str(response.request),
#       end="\n--------------------")
