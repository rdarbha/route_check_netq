"""

Usage:
  route_check.py store <node>
  route_check.py check <node>
  route_check.py (-h | --help)

Options:
  -h --help   Show this screen

"""

import redis
import subprocess
import json
import time
import docopt

def GetCommandOutput(command):

  result = subprocess.check_output(command, shell=True)
  parsed_json = json.loads(result)

  #Need to return parsed_json[0] because netq nests json in two arrays
  return parsed_json[0]

def CheckRoutes(parsed_json, stored_routes):

  found_routes = []
  lost_routes = []

  for node in parsed_json:
    # print "Current route check:" + node['ip']
    if str(node['ip']) in stored_routes:
      # print "Found The Route"
      # print "before: " + str(check_routes)
      stored_routes.remove(node['ip'])
      # print "after: " + str(check_routes)
    else:
      lost_routes.append(str(node['ip']))

  if len(stored_routes) != 0:
    print "Routes missing from current routing table: "
    for route in stored_routes:
      print route
  if len(lost_routes) != 0:
    print "Additional routes unexpectedly found in routing table: "
    for route in lost_routes:
      print route
  if len(stored_routes) == 0 and len(lost_routes) == 0:
    print "All routes match!"

if __name__ == '__main__':
  arguments = docopt.docopt(__doc__)

  command = "netq show ip route " + arguments['<node>'] + " json"

  #Commented out because reading in routes from file now
  # stored_routes = ["10.254.0.2/32","10.254.0.3/32","10.254.0.4/32","10.254.0.5/32","10.254.0.6/32","10.254.0.7/32","10.254.0.8/32"]

  found_routes = []
  lost_routes = []

  # Read in file. Each line is a route statement
  fname = arguments['<node>']

  if arguments['check']:
    f = open(fname, 'r')
    stored_routes = f.readlines()
    stored_routes = [x.strip() for x in stored_routes]
    command_output = GetCommandOutput(command)
    CheckRoutes(command_output, stored_routes)

  if arguments['store']:
    f = open(fname, 'w')
    routes_list = GetCommandOutput(command)
    for route in routes_list:
      f.write(route['ip'])
      f.write("\n")
    print "Routes have been stored"
  f.close()
