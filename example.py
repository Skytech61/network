import logging

from simulator.Simulator import Simulator

from NIC import NIC
from Router import Router
from Link import Link

logging.getLogger('simulator').setLevel(logging.INFO)
logging.getLogger('NIC').setLevel(logging.INFO)

logging.getLogger('simulator').debug('Creating simulator...')
sim = Simulator()

#                          Example Topology
#
#    ┌──────────┐            ┌──────────┐            ┌──────────┐
#    │          │eth0    eth0│          │eth1    eth0│          │
#    │ Router 1 ├────────────┤ Router 2 ├────────────┤ Router 3 │
#    │          │            │          │            │          │
#    └────┬────┬┘            └────┬─────┘            └──────────┘
#     eth1│    │eth2              │eth2                          
#         │    │                  │                              
#         │    └──────────────┐   │                              
#         │                   │   │                              
#         │                   │   │                              
#     eth0│               eth2│   │eth1                          
#    ┌────┴─────┐            ┌┴───┴─────┐                        
#    │          │eth1    eth0│          │                        
#    │ Router 4 ├────────────┤ Router 5 │                        
#    │          │            │          │                        
#    └──────────┘            └──────────┘                                              


# Router instantiation
R1 = Router(sim, 'R1')
nic1_0 = NIC(sim, 'eth0', 1e6)
R1.add_nic(nic1_0)
nic1_1 = NIC(sim, 'eth1', 2e6)
R1.add_nic(nic1_1)
nic1_2 = NIC(sim, 'eth2', 7e5)
R1.add_nic(nic1_2)

R2 = Router(sim, 'R2')
nic2_0 = NIC(sim, 'eth0', 1e6)
R2.add_nic(nic2_0)
nic2_1 = NIC(sim, 'eth1', 1.5e6)
R2.add_nic(nic2_1)
nic2_2 = NIC(sim, 'eth2', 5e6)
R2.add_nic(nic2_2)

R3 = Router(sim, 'R3')
nic3_0 = NIC(sim, 'eth0', 1.5e6)
R3.add_nic(nic3_0)

R4 = Router(sim, 'R4')
nic4_0 = NIC(sim, 'eth0', 2e6)
R4.add_nic(nic4_0)
nic4_1 = NIC(sim, 'eth1', 5e5)
R4.add_nic(nic4_1)

R5 = Router(sim, 'R5')
nic5_0 = NIC(sim, 'eth0', 5e5)
R5.add_nic(nic5_0)
nic5_1 = NIC(sim, 'eth1', 5e6)
R5.add_nic(nic5_1)
nic5_2 = NIC(sim, 'eth2', 7e5)
R5.add_nic(nic5_2)

# Link instantiation
L1 = Link(100, 2e8) # R1 <-> R2
nic1_0.attach(L1)
nic2_0.attach(L1)

L2 = Link(100, 2e8) # R2 <-> R3
nic2_1.attach(L2)
nic3_0.attach(L2)

L3 = Link(100, 2e8) # R1 <-> R4
nic1_1.attach(L3)
nic4_0.attach(L3)

L4 = Link(100, 2e8) # R4 <-> R5
nic4_1.attach(L4)
nic5_0.attach(L4)

L5 = Link(100, 2e8) # R5 <-> R2
nic5_1.attach(L5)
nic2_2.attach(L5)

L6 = Link(100, 2e8) # R1 <-> R5
nic1_2.attach(L6)
nic5_2.attach(L6)

# Router start
R1.start()
R2.start()
R3.start()
R4.start()
R5.start()

sim.run()