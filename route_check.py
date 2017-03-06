import redis
import subprocess
import json
import time

# redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# print redis_db.keys()

# commands = ["ls -l","ls"]
commands = ["netq show ip route leaf01 json"]
failed_nodes = []

check_routes = ["10.254.0.2/32","10.254.0.3/32","10.254.0.4/32","10.254.0.5/32","10.254.0.6/32","10.254.0.7/32","10.254.0.8/32"]
found_routes = []
lost_routes = []

for command in commands:
  # call(["ls", "-l"])
  result = subprocess.check_output(command, shell=True)
  # print result
  parsed_json =  json.loads(result)
  # print parsed_json
  # print
  # print parsed_json[0]
  # print
  # print parsed_json[0][0]

  for node in parsed_json[0]:
    print "Current route check:" + node['ip']
    if str(node['ip']) in check_routes:
      print "Found The Route"
      print "before: " + str(check_routes)
      check_routes.remove(node['ip'])
      print "after: " + str(check_routes)
    else:
      lost_routes.append(str(node['ip']))

print "Routes not in current routing table: " + str(check_routes)
print "Routes unexpectedly found in routing table: " + str(lost_routes)