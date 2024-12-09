from simulator.SimulatedEntity import SimulatedEntity
from Packet import Packet

class Router(SimulatedEntity):
    
    def __init__(self, sim, name):
        super().__init__(sim)
        self._name = name
        self._nics = []
        self._last_rx = None
        
    def add_nic(self, nic):
        assert nic.host() == None
        nic.set_host( self )
        self._nics.append( nic )
    
    def start(self):
        # Send a default packet to all neighbors
        for nic in self._nics:
            p = Packet(content=f'Hello from {self}')
            nic.send(p)
            print(f'@{self._now():.6f}, {self} sends {p} on {nic}')
    
    def receive(self, nic, pkt):
        assert nic in self._nics
        print(f"@{self._now():.6f}, {pkt} received by {self} on {nic}")
        
    def __repr__(self):
        return f'Router({self._name})'

