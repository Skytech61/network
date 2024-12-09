
from simulator.SimulatedEntity import SimulatedEntity
from simulator.Event import Event

class NIC(SimulatedEntity):
    
    def __init__(self, sim, name, rate):
        super().__init__(sim, 'NIC')
        self._name = name
        self._rate = rate
        self.__link = None
        self.__host = None
        
    def get_rate(self):
        return self._rate
    
    def queue_depth(self):
        return len(self._q)
        
    def host(self):
        return self.__host
    
    def set_host(self, host):
        self.__host = host
        
    def attach(self, link):
        self.__link = link
        link.attach(self)
        
    def delay_tr(self, L):
        return L * 8 / self._rate
            
    def __received(self, pkt):
        self._debug(f'received {pkt}')
        self.__host.receive(self, pkt)
        
    def send(self, pkt):
        """Send a packet to the other end of the attached link. Buffering is not implemented,
        therefore multiple packets could be sent simultaneously.
        """
        self._debug(f'transmitting {pkt}')
        self._sim.add_event( Event(pkt, self.__link.other(self).__received), self.delay_tr(pkt.size) + self.__link.delay_pr() )
            
    def __repr__(self):
        return f'NIC({self.__host._name}:{self._name})'
            
            