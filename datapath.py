#!/usr/bin/env python
#
#    traffic route between H1 TO G1 Server
# H1 ---- S3 ---- S2----- S1-----S6 ------G1
#   


import hpsdnclient as hp

def main():
    #initialize the api
    controller = '192.168.79.131'
    auth = hp.XAuthToken(user='sdn', password='skyline', server=controller)
    api = hp.Api(controller=controller, auth=auth)

    #create the match object
    match = hp.datatypes.Match(eth_type="ipv4", ipv4_src="10.10.2.1",
                               ipv4_dst="10.10.2.254",ip_proto="tcp",
                               tcp_dst="80")

    #create the action objects
    output1 = hp.datatypes.Action(output=1)
    output2 = hp.datatypes.Action(output=2)
    output3 = hp.datatypes.Action(output=3)
    output5 = hp.datatypes.Action(output=5)

    #create the flows
    flow1 = hp.datatypes.Flow(priority=30000, idle_timeout=300,
                              match=match, actions=output5)
    flow2 = hp.datatypes.Flow(priority=30000, idle_timeout=300,
                              match=match, actions=output1)
    flow3 = hp.datatypes.Flow(priority=30000, idle_timeout=300,
                              match=match, actions=output2)
    flow6 = hp.datatypes.Flow(priority=30000, idle_timeout=300,
                              match=match, actions=output3)


    #push the flows to the datatpaths
    api.add_flows('00:00:00:00:00:00:00:03', flow3)
    api.add_flows('00:00:00:00:00:00:00:02', flow2)
    api.add_flows('00:00:00:00:00:00:00:01', flow1)
    api.add_flows('00:00:00:00:00:00:00:06', flow6)

if __name__ == "__main__":
    main()
