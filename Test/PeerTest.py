from pyactor.context import set_context, create_host, sleep, shutdown
from Peer import *
from Group import *

if __name__ == "__main__":
    set_context()
    h = create_host()

    group = h.spawn('tracker1',Group)

    peer0 = h.spawn("peer0", Sequencer)
    peer1 = h.spawn("peer1", Sequencer)
    peer2 = h.spawn("peer2", Sequencer)
    peer3 = h.spawn("peer3", Sequencer)
    peer4 = h.spawn("peer4", Sequencer)
    peer5 = h.spawn("peer5", Sequencer)
    peer6 = h.spawn("peer6", Sequencer)
    peer7 = h.spawn("peer7", Sequencer)
    peer8 = h.spawn("peer8", Sequencer)
    peer9 = h.spawn("peer9", Sequencer)


    group.join(peer0)
    group.join(peer1)
    group.join(peer2)
    group.join(peer5)
    group.join(peer6)
    group.join(peer3)
    group.join(peer4)
    group.join(peer7)
    group.join(peer8)
    group.join(peer9)

    group.init_start()

    peer0.multicast("mensaje1")
    #peer1.multicast("mensaje2")
