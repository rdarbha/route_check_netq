import redis
import subprocess
import json
import time

# redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# print redis_db.keys()

# commands = ["ls -l","ls"]
commands = ["netq show ip route leaf01 json"]
failed_nodes = []

check_routes = ["10.254.0.2","10.254.0.5","10.254.0.5","10.254.0.6","10.254.0.7"]
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
    #print node['reason']
    print node['ip']
    if node['ip'] in current_routes:
      print "Found The Route"
      print "before"
      print current_routes
      current_routes.remove(node['ip'])
      print "after"
      print current_routes
    else:
      lost_routes.append(str(node['ip']))

print current_routes
print lost_routes