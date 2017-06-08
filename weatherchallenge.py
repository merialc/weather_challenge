import sys
from weather import Weather
from prettytable import PrettyTable

if len(sys.argv) > 1:
    weather = Weather ()
    location = weather.lookup_by_location((sys.argv[1]))
    atmosphere = location.atmosphere()
    forecast = location.forecast()
    city = location.location()

averageTotal = 0.0
for f in location.forecast():
    averageTotal += (int(f['high']) + int(f['low'])) / 2	


x = PrettyTable()

x.add_column("Postcode", [sys.argv[1]])
x.add_column("City", [city['city']])
x.add_column("Pressure", [atmosphere['pressure']])
x.add_column("Average 10-day temp",[(((averageTotal / 10) - 32) / 9.0 * 5.0)])

print x
