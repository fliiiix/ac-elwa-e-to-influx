import requests
import json

BOILER = {
    "url": "http://hostname/data.jsn",
    "name": "lename":
}

INFLUX = {
    "url": "https://hostname:8086/write?db=databasename", 
    "username":"leuser", 
    "password":"lepassword"
}

response = requests.get(BOILER["url"])
device = json.loads(response.text)

status = 1
power = device["power_elwa2"]
watertemp = int(device["temp1"]) / 10

data = "boiler,name={} status={}i,power={}i,watertemp={}".format(
    BOILER["name"],
    status,
    power,
    watertemp,
)

r = requests.post(INFLUX["url"], data=data, auth=(INFLUX["username"], INFLUX["password"]))

print(data)
print(r.status_code)
print(r.text)

"""
Docs
-----------------
Power: in watts 
Boostpower: in watts
Watertemp: in celsius / 10
Targettemp: in celsius
Boosttemp: in celsius
Boostactive: True/False
Time: date
Status:
    - 1  : No Communication
    - 2  : Heating
    - 3  : Standby
    - 4  : Boost Heating
    - 5  : Heating finished
    - 9  : Setup Mode
    - 201: Overtemp Fuse Error
    - 202: Overtemp Error
    - 203: Device Overheat Error
    - 204: Hardware Error
    - 205: Temp Sensor Error
"""
