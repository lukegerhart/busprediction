#Imports#
import requests
import json

#getroutes
"""
r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getroutes', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json'})
response = r.json()
routes = response['bustime-response']['routes']
routes_list = []
new_route = ''
for route in routes:
	rt = route['rt']
	rtnm = route['rtnm']
	print(rt + ', ' + rtnm)
	#new_route = '{\'rt\':\'' + rt + '\', \'rtnm\':\'' + rtnm +'\'}' 
	new_route = {'rt':rt, 'rtnm':rtnm}
	routes_list.append(new_route)
all_routes = open('allroutes.json', 'w')
all_routes.write(json.dumps(routes_list, sort_keys=True))
all_routes.close()
"""
"""
for i in range(0, len(routes_list)):
	if i == 0:
		all_routes.write('[' + str(routes_list[i]) + ',\n')
	elif i == len(routes_list)-1:
		all_routes.write(' ' + str(routes_list[i]) + ']')
	else:
		all_routes.write(' ' + str(routes_list[i]) + ',\n')
"""

#getdirections
"""
all_routes = None
try:
	all_routes = open('allroutes.json', 'r')
except FileNotFoundError:
	print("ERROR: file allroutes.json does not exist")
	exit()
routes_list = json.loads(all_routes.read())
all_routes.close()

#get datafeed
r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getrtpidatafeeds', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json'})
response = r.json()
feeds = response['bustime-response']['rtpidatafeeds']
datafeed = ''
for feed in feeds:
	if feed['enabled'] == 'true':
		datafeed = feed['name']

#get directions for each route
dirs_list = []
for route in routes_list:
	if route['rt'].startswith('6'):
		param_dict = {'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':route['rt'], 'rtpidatafeed':datafeed}
		r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getdirections', params=param_dict)
		directions = r.json()['bustime-response']['directions']
		#print(directions)
		for direction in directions:
			print(route['rt'] + ', ' + route['rtnm'] + ', ' + direction['name'])
			dir = {'rt':route['rt'], 'rtnm':route['rtnm'], 'dir':direction['name']}
			dirs_list.append(dir)

all_dirs = open('6routes.json', 'w')
all_dirs.write(json.dumps(dirs_list))
all_dirs.close()
"""
#getstops

all_dirs = None
try:
	all_dirs = open('6routes.json', 'r')
except FileNotFoundError:
	print('ERROR: file 6routes.json does not exist')
	exit()
dirs_list = json.loads(all_dirs.read())
all_dirs.close()


















#r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getroutes', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':''})
