import redis
import subprocess
import json
import time

# redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# print redis_db.keys()

# commands = ["ls -l","ls"]
commands = ["netq show ip route leaf01"]
failed_nodes = []

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
    if node['reason'] != '':
      #print node['reason']
      failed_nodes.append(node)
  print failed_nodes
