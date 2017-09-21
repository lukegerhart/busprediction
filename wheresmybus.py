#Imports#
import requests
import json
import sys

#function definitions
def response_error(response):
	try:
		error = response['error']
		return str(error)
	except KeyError:
		return None

def get_data_feed():
	r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getrtpidatafeeds', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json'})
	response = r.json()['bustime-response']
	error = response_error(response)
	if error is not None:
		print('There was an error with the API call: ' + error)
		exit()
	feeds = response['rtpidatafeeds']
	datafeed = ''
	for feed in feeds:
		if feed['enabled'] == 'true':
			datafeed = feed['name']
	return datafeed

#getroutes
if sys.argv[1] == 'getroutes':
	r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getroutes', params={'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json'})
	response = r.json()['bustime-response']
	error = response_error(response)
	if error is not None:
		print('There was an error with the API call: ' + error)
		exit()
	routes = response['routes']
	routes_list = []
	new_route = ''
	for route in routes:
		rt = route['rt']
		rtnm = route['rtnm']
		print(rt + ', ' + rtnm)
		new_route = {'rt':rt, 'rtnm':rtnm}
		routes_list.append(new_route)
	all_routes = open('allroutes.json', 'w')
	all_routes.write(json.dumps(routes_list, sort_keys=True))
	all_routes.close()
elif sys.argv[1] == 'getdirections':
	
	all_routes = None
	try:
		all_routes = open('allroutes.json', 'r')
	except FileNotFoundError:
		print("ERROR: file allroutes.json does not exist")
		exit()
	
	routes_list = json.loads(all_routes.read())
	all_routes.close()
	
	datafeed = get_data_feed()

	#get directions for each route
	dirs_list = []
	for route in routes_list:
		if route['rt'].startswith('6'):
			param_dict = {'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':route['rt'], 'rtpidatafeed':datafeed}
			r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getdirections', params=param_dict)
			response = r.json()['bustime-response']
			error = response_error(response)
			if error is not None:
				print('There was an error with the API call: ' + error)
				exit()
			directions = response['directions']
			for direction in directions:
				#print result
				print(route['rt'] + ', ' + route['rtnm'] + ', ' + direction['name'])
				dir = {'rt':route['rt'], 'rtnm':route['rtnm'], 'dir':direction['name']}
				dirs_list.append(dir)

	all_dirs = open('6routes.json', 'w')
	all_dirs.write(json.dumps(dirs_list))
	all_dirs.close()
elif sys.argv[1] == 'getstops':
	#getstops
	if len(sys.argv) != 4:
		print('Error: run program as python3 wheresmybus.py getstops routeID direction')
		exit()
	route_id = sys.argv[2].upper()
	direction = sys.argv[3].upper()
	
	all_dirs = None
	try:
		all_dirs = open('6routes.json', 'r')
	except FileNotFoundError:
		print('ERROR: file 6routes.json does not exist')
		exit()
	dirs_list = json.loads(all_dirs.read())
	all_dirs.close()
	
	found_rt_dir = False
	for dir in dirs_list:
		if dir['rt'] == route_id and dir['dir'] == direction:
			found_rt_dir = True
	if not found_rt_dir:
		print('ERROR: invalid route/direction combination: routeID/directon')
		exit()
	
	datafeed = get_data_feed()
	param_dict = {'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'rt':route_id, 'dir':direction, 'rtpidatafeed':datafeed}
	r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getstops', params=param_dict)
	response = r.json()['bustime-response']
	error = response_error(response)
	if error is not None:
		print('There was an error with the API call: ' + error)
		exit()
	stops = response['stops']
	
	inner_stops = []
	for stop in stops:
		print(stop['stpid'] + ', ' + stop['stpnm'])
		inner_stop = {'stpid':stop['stpid'], 'stpnm':stop['stpnm']}
		inner_stops.append(inner_stop)
	stops_list = {'rt':route_id, 'dir':direction, 'stops':inner_stops}
	
	all_stops = open('mystops.json', 'w')
	all_stops.write(json.dumps(stops_list))
	all_stops.close()
elif sys.argv[1] == 'getarrivals':
	if len(sys.argv) != 3:
		print('Error: run program as python3 wheresmybus.py getarrivals stopID')
		exit()
	stpid = [sys.argv[2]]
	
	all_dirs = None
	try:
		all_dirs = open('6routes.json', 'r')
	except FileNotFoundError:
		print('ERROR: file 6routes.json does not exist')
		exit()
	dirs_list = json.loads(all_dirs.read())
	all_dirs.close()
	
	datafeed = get_data_feed()
	
	param_dict = {'key':'k2HrcvhLbdHdxHHKpJnRgr7bj', 'format':'json', 'stpid':'a', 'rtpidatafeed':datafeed}
	r = requests.get('http://truetime.portauthority.org/bustime/api/v3/getpredictions', params=param_dict)
	response = r.json()['bustime-response']
	error = response_error(response)
	if error is not None:
		print('There was an error with the API call: ' + error)
		exit()
	predictions = response['prd']
	stop_info = []
	for prd in predictions:
		rtnm = 'TBD'
		for dir in dirs_list:
			if prd['rt'] == dir['rt']:
				rtnm = dir['rtnm']
		print('%s, %s, %s, %s, %s, %s' % (prd['rt'], rtnm, prd['rtdir'], prd['stpid'], prd['stpnm'], prd['tmstmp']))
		bus_info = {'rt':prd['rt'], 'rtn':rtnm, 'rtdir':prd['rtdir'], 'stpid':prd['stpid'], 'stopnm':prd['stpnm'], 'timstmp':prd['tmstmp']}
		stop_info.append(bus_info)
	stop_file = open('myarrivals.json', 'w')
	stop_file.write(json.dumps(stop_info))
	stop_file.close()
else:
	print('Error: run program as python3 wheresmybus.py command optional_arguments')
	exit()