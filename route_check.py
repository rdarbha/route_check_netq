import redis
import subprocess
import json
import time

# redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# print redis_db.keys()

# commands = ["ls -l","ls"]
commands = ["netq show ip route leaf01 json"]
failed_nodes = []

current_routes = ["10.254.0.2","10.254.0.5","10.254.0.5","10.254.0.6","10.254.0.7"]
new_routes = []

for command in commands:
  # call(["ls", "-l"])
  result = subprocess.check_output(command, shell=True)
  print result
  parsed_json =  json.loads(result)
  print parsed_json
  print
  print parsed_json[0]
  print
  print parsed_json[0][0]

  for node in parsed_json[0]:
    #print node['reason']
    print node['ip']
    if node['ip'] in check_list:
      current_routes.remove(node['ip'])
    else:
      new_routes.append(node['ip'])

print current_routes
print new_routes