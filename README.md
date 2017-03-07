# route_check_netq

## How to Use

Usage:
  route_check.py store <node>
  route_check.py check <node>
  route_check.py (-h | --help)

Options:
  -h --help   Show this screen


route_check.py store <node>
- stores the current routing table locally with the filename set to the node name

route_check.py check <node>
- compares the current routing table against the stored file

Examples:

All below output are done using cldemo_netq_l3

This is my hand made file for testing

    cumulus@oob-mgmt-server:~/route_check_netq$ cat leaf01
    10.254.0.2/32
    10.254.0.3/32
    10.254.0.4/32
    10.254.0.5/32
    10.254.0.6/32
    10.254.0.7/32
    10.254.0.10/32

-

    cumulus@oob-mgmt-server:~/route_check_netq$ python route_check.py check leaf01
    Routes missing from current routing table:
    10.254.0.20/32
    Additional routes unexpectedly found in routing table:
    0.0.0.0/0
    10.3.20.0/24
    10.1.20.0/24
    10.1.20.0/32
    10.1.20.253/32
    10.1.20.254/32
    10.1.20.255/32
    169.254.1.0/30
    169.254.1.0/32
    169.254.1.1/32
    169.254.1.3/32
    192.168.0.0/24
    192.168.0.0/32
    192.168.0.11/32
    192.168.0.255/32

-

    cumulus@oob-mgmt-server:~/route_check_netq$ python route_check.py store leaf01
    Routes have been stored

-

    cumulus@oob-mgmt-server:~/route_check_netq$ python route_check.py check leaf01
    All routes match!