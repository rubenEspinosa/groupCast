from pyactor.context import set_context, create_host, shutdown
from Group import *
from Peer import *


if __name__ == "__main__":
    set_context()
    h = create_host()

    group = h.spawn('group1', Group)

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

    #comprobar que funciona el annnounce
    print "comprobacion announce"
    sleep(11)
    print group.get_members()
    print group.get_members_name()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "peer0, peer1 y peer2 simularan que han caido:"
    peer0.stop_interval()
    peer1.stop_interval()
    peer2.stop_interval()
    sleep(11)
    print group.get_members()
    print group.get_members_name()

    shutdown()