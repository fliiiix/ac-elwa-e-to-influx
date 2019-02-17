import requests
import xml.etree.ElementTree as ET

BOILER = {
    "url": "http://hostname/data.xml",
    "name": "lename":
}

INFLUX = {
    "url": "https://hostname:8086/write?db=databasename", 
    "username":"leuser", 
    "password":"lepassword"
}

response = requests.get(BOILER["url"])
root = ET.fromstring(response.text)
device = root.find("DeviceStatus")

status = device.find("Status").text
power = device.find("Power").text
watertemp = int(device.find("Watertemp").text) / 10
boostpower = device.find("Boostpower").text
boostactive = device.find("Boostactive").text

data = "boiler,name={} status={}i,power={}i,watertemp={},boostpower={}i,boostactive={}i".format(
    BOILER["name"],
    status,
    power,
    watertemp,
    boostpower,
    boostactive
)

r = requests.post(INFLUX["url"], data=data, auth=(INFLUX["username"], INFLUX["password"]))

print(data)
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
