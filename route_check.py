import redis
import subprocess
import json
import time

commands = ["netq show ip route leaf01 json"]

# stored_routes = ["10.254.0.2/32","10.254.0.3/32","10.254.0.4/32","10.254.0.5/32","10.254.0.6/32","10.254.0.7/32","10.254.0.8/32"]
found_routes = []
lost_routes = []

fname = "route_list"

with open(fname) as f:
  stored_routes = f.readlines()

stored_routes = [x.strip() for x in stored_routes]

print stored_routes

for command in commands:
  result = subprocess.check_output(command, shell=True)
  # print result
  parsed_json =  json.loads(result)
  # print parsed_json
  # print
  # print parsed_json[0]
  # print
  # print parsed_json[0][0]

  for node in parsed_json[0]:
    # print "Current route check:" + node['ip']
    if str(node['ip']) in stored_routes:
      # print "Found The Route"
      # print "before: " + str(check_routes)
      stored_routes.remove(node['ip'])
      # print "after: " + str(check_routes)
    else:
      lost_routes.append(str(node['ip']))

print "Routes not in current routing table: " + str(stored_routes)
print "Routes unexpectedly found in routing table: " + str(lost_routes)