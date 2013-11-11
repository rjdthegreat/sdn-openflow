"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
import mininet.util
from mininet.node import Switch
from mininet.node import Node

hosts = []
class MyTopo( Topo ):
#    hosts = []
#    switches = []
    "Simple topology example."
    def createTopology(self):
	global hosts
	with open("ip.txt","r") as f:
		lines = f.readlines()
    		self.addHosts(int(lines[0]))
		self.addSwitches(int(lines[1]))
		self.addLinks(lines[2:])
		#for i in range(len(hosts)):
			#node = Node(hosts[i])
			#print "Blahhhhh"
			#print node
			#mac = Node.MAC(node,hosts[i]+'-eth0') 
			#print "Mac"
			#print mac
	
    def addSwitches(self,n):
	with open("SwitchMapping.txt","a") as f2:
		for i in range(n):
			sName = self.addSwitch('s'+`i+1`)
			#sDpid = getDpidFromName(sName)
			print "DPID"
			print Switch(sName).dpid
			f2.write(sName+","+str(Switch(sName).dpid)+"\n")
        	f2.close()
        #print "Node iNFO"
	#z=self.nodeInfo("s1")
	#print z
	#print type(z)
	#print "End of node info"
        #print vars(self.g)
	#print type(self.g)
	#print type(self.switches)
	#dipids=self.hosts()
	#print dipids
	#print type(dipids)
	#print "Nodes"
	#print self.nodes()[0]
	#print dipids[0]
	#for s in self.switches:
	#	print s

    def addHosts(self,n):
	global hosts
	#print hosts	
	for i in range(n):
		hosts.append(self.addHost('h'+`i+1`))
		
		#k=node.defaultIntf();
		
		#print "printing K and Node";
		#print k,node;
		#macOfHost = Node.MAC(node,hosts[i]+'-eth0')
		#mac2 = hostName.MAC()
		#mac = Node.MAC(node,k);
		#mac = node.MAC(self,k)
		#m1 = Node.hostName.MAC()
		#print mac
	print hosts
    def addLinks(self,links):
#	n = int(links[0])
	for i in range(1,len(links)):
		#print links
		nodes = links[i].rstrip().split(' ');
		#print nodes
		self.addLink(nodes[0],nodes[1].rstrip())
	
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	self.createTopology();
	#net = Mininet(MyTopo);
	#print net.switches
        """ leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        """
		

topos = { 'dup': ( lambda: MyTopo() ) }
