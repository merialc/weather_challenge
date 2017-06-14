from urllib2 import urlopen
import requests
import json
from prettytable import PrettyTable

response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Bristol,uk&appid=1ac5db62be3852d13313466234712716")

response = json.loads(response.text)

y = PrettyTable()
dates = []
temps = []
for x in response['list']:
	dates.append( x['dt_txt'])
	temps.append(x['main']['temp']-273.15)

y.add_column("Date", dates)
y.add_column("Temperature", temps)

avg = float(sum(temps)/len(temps))

print y
print (int(avg))
print (u'\u00b0'+ " C")



