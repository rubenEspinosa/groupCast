from pyactor.context import set_context, create_host, shutdown
from Group import *
from Peer import *


if __name__ == "__main__":
    set_context()
    h = create_host('http://127.0.0.1:1111/')
    group = h.lookup_url('http://127.0.0.1:2220/group', 'Group', 'Group')
    peer1 = h.spawn("peer1", Sequencer)
    group = h.spawn('group', Group)

    print "se realizara el join en 10 segundos..."
    sleep(10)
    group.join(peer1)


    #comprobar que funciona el annnounce
    print "comprobacion announce"
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "peer0, peer1 y peer2 simularan que han caido:"
    peer1.stop_interval()
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    shutdown()