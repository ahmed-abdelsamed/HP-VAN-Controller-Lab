"""Custom topology example


Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        h1 = self.addHost( 'h1', ip='10.10.2.1/24', defaultRoute='via 10.10.2.254' )
        h2 = self.addHost( 'h2', ip='10.10.2.2/24', defaultRoute='via 10.10.2.254' )
        h3 = self.addHost( 'h3', ip='10.10.2.3/24', defaultRoute='via 10.10.2.254' )
        h4 = self.addHost( 'h4', ip='10.10.2.4/24', defaultRoute='via 10.10.2.254' )
        h5 = self.addHost( 'h5', ip='10.10.2.5/24', defaultRoute='via 10.10.2.254' )
        h6 = self.addHost( 'h6', ip='10.10.2.6/24', defaultRoute='via 10.10.2.254' )
        g1 = self.addHost( 'g1', ip='10.10.2.254/24')
        
        s1 = self.addSwitch( 's1', dpid='0000000000000001',protocols='OpenFlow13' )
        s2 = self.addSwitch( 's2', dpid='0000000000000002',protocols='OpenFlow13' )
        s3 = self.addSwitch( 's3', dpid='0000000000000003',protocols='OpenFlow13' )
        s4 = self.addSwitch( 's4', dpid='0000000000000004',protocols='OpenFlow10' )
        s5 = self.addSwitch( 's5', dpid='0000000000000005',protocols='OpenFlow13' )
        s6 = self.addSwitch( 's6', dpid='0000000000000006',protocols='OpenFlow13' ) 
 
        #core
        self.addLink ( s1, s2 )
 
        #distribution
        self.addLink ( s1, s3 )
        self.addLink ( s1, s4 )
        self.addLink ( s1, s5 )
        self.addLink ( s1, s6 )
 
        self.addLink ( s2, s3 )
        self.addLink ( s2, s4 )
        self.addLink ( s2, s5 )
        self.addLink ( s2, s6 )
 
        #acccess
        self.addLink( s3, h1 )
        self.addLink( s3, h2 )
        self.addLink( s4, h3 ) 
        self.addLink( s4, h4 ) 
        self.addLink( s5, h5 ) 
        self.addLink( s5, h6 ) 
        self.addLink( s6, g1) 

topos = { 'mytopo': ( lambda: MyTopo() ) }

"""
#
how to run:
sudo mn --custom topology.py --topo mytopo --controller=remote,ip=10.0.0.11
"""
