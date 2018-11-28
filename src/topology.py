#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

#import module
from mininet.util import dumpNodeConnections
#dump every hosts and switches connections
#dumpNodeConnections(net.hosts)
#dumpNodeConnections(net.switches)
#import module
from mininet.cli import CLI
# do not use net.stop()
#CLI(net)

class MultiSwitchTopo(Topo):
    def build(self):
        # Add a switch to a topology
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        #switches=[s1,s2,s3,s4,s5,s6,s7]
        # Add the host and link to a topology
        # Add a host to a topology
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        #h7 = self.addHost('h7')
        #h8 = self.addHost('h8')
        #hosts=[h1,h2,h3,h4,h5,h6,h7,h8]
        # Add a bidirectional link to a topology
        self.addLink( 
            s8, #how to refer to specific host?
            s1, #how to refer to specific switch?
            bw = 20,
            delay = '7ms',
            loss = 15)
        self.addLink(#2
            s8,
            s4,
            bw = 23,
            delay = '6ms',
            loss = 10)	
        self.addLink(#3
            s8,
            s2,
            bw = 25,
            delay = '6ms',
            loss = 14)
        self.addLink(#4
            s8,
            s6,
            bw = 30,
            delay = '1ms',
            loss = 12)
        self.addLink(#5
            s9,
            s2,
            bw = 30,
            delay = '3ms',
            loss = 18)
        self.addLink(#6
            s9,
            s5,
            bw = 30,
            delay = '3ms',
            loss = 20)
        self.addLink(#7
            s9,
            s3,
            bw = 35,
            delay = '2ms',
            loss = 17)
        self.addLink(#8
            s9,
            s7,
            bw = 33,
            delay = '8ms',
            loss = 10)
        self.addLink(#9
            h1,
            s1,
            bw = 12,
            delay = '6ms',
            loss = 2)
        self.addLink(#10
            h5,
            s4,
            bw = 14,
            delay = '5ms',
            loss = 2)
        self.addLink(#11
            h6,
            s5,
            bw = 15,
            delay = '4ms',
            loss = 3)
        self.addLink(#12
            h4,
            s3,
            bw = 13,
            delay = '3ms',
            loss = 5)
        self.addLink(#13
            h3,
            s7,
            bw = 18,
            delay = '6ms',
            loss = 6)
        self.addLink(#14
            h2,
            s6,
            bw = 18,
            delay = '2ms',
            loss = 3)

def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = MultiSwitchTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo,
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    # Stop a network
    CLI(net)
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    #CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()

