from pyactor.context import set_context, create_host, shutdown,sleep
from Peer import *
from GroupTest import *
import queue

if __name__ == "__main__":
    set_context()
    h = create_host()

    group = h.spawn("group1", Group)

    peer0 = h.spawn("peer0", Sequencer)
    peer1 = h.spawn("peer1", Sequencer)
    peer2 = h.spawn("peer2", Sequencer)
    peer3 = h.spawn("peer3", Sequencer)
    peer4 = h.spawn("peer4", Sequencer)


    group.set_sequencer(peer4)

    group.join(peer0)
    group.join(peer1)
    group.join(peer2)
    group.join(peer3)


    group.init_start()

    peer0.multicast("mensaje1")
    peer2.multicast("mensaje2")
    peer1.multicast("mensaje3")
    peer3.multicast("mensaje4")

    sleep(2)
    print "nuevo sequencer elegido"
    print peer0.get_sequencer()

    print peer0.get_messages()








    sleep(5)

    shutdown()