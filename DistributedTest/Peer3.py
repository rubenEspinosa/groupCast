from pyactor.context import set_context, create_host, shutdown , sleep
from Group import *
from Peer import *


if __name__ == "__main__":
    set_context()
    h = create_host('http://127.0.0.1:1113/')
    group = h.lookup_url('http://127.0.0.1:2220/group', 'Group', 'Group')
    group = h.spawn('group1', Group)
    peer3 = h.spawn("peer3", Sequencer)

    print "se realizara el join en 6 segundos..."
    sleep(6)
    group.join(peer3)


    #comprobar que funciona el annnounce
    print "comprobacion announce"
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "peer0, peer1 y peer3 simularan que han caido:"
    peer3.stop_interval()
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    shutdown()