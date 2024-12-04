from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller

class myTopo( Topo ):
	
	def build( self ):
	#Hosts and Switches
		host1 = self.addHost( 'h1' )
		host2 = self.addHost( 'h2' )
		host3 = self.addHost( 'h3' )
		host4 = self.addHost( 'h4' )
		host5 = self.addHost( 'h5' )

		mainSwitch = self.addSwitch( 's1' )

	#Links
		self.addLink( host1, mainSwitch )
		self.addLink( host2, mainSwitch )
		self.addLink( host3, mainSwitch )
		self.addLink( host4, mainSwitch )
		self.addLink( host5, mainSwitch )

topos = { 'mytopo' : ( lambda: myTopo() ) }
