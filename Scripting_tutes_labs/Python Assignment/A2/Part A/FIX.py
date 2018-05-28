
# out of scope
import requests
import datetime

response = requests.get('https://ipapi.co/json')
latitude = response.headers.get('latitude')
longitude = response.headers.get('longitude')
tz = response.headers.get('utc_offset')
RiseSetURL = "api.sunrise-sunset.org/json?lat=" + str(latitude) + "&lng=" + str(longitude)
time = datetime.datetime.now(tz)
response = requests.get('https://' + RiseSetURL)
sunrise = response.headers.get('sunrise')
print(longitude,latitude,sunrise,time,tz)
print(response)

# returned: None None None 2018-05-27 10:02:09.815786 None
# we have a problem accessing data...
# nb: datetime had no tz but got local time.

# Call Process Error Checking...
cpe = subprocess.CompletedProcess.check_returncode()
print("CP Error Report:",cpe.cmd,"\toutput:",cpe.output)
