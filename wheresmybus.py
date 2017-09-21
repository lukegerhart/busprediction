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
"""
all_routes.close()
"""
#getdirections

all_routes = None

try:
	all_routes = open('allroutes.json', 'r')
except FileNotFoundError:
	print("ERROR: file allroutes.json does not exist")
	exit()
routes_list = json.loads(all_routes.read())
all_routes.close()
for route in routes_list:
	if route['rt'].startswith('6'):
		param_dict = {'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':route['rt'], 'rtpidatafeed':'acmeta'}
		#r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getdirections', params=param_dict)
		r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getdirections', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json'55}
		response = r.json()
		directions = response['bustime-response']#['directions']
		print(directions)
		#for direction in directions:
			#print(route['rt'] + ', ' + route['rtnm'] + ', ' + direction['name'])

#r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getroutes', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':''})
