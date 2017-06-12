from pyactor.context import set_context, create_host, shutdown , sleep
from Group import *
from Peer import *


if __name__ == "__main__":
    set_context()
    h = create_host('http://127.0.0.1:1114/')
    group = h.lookup_url('http://127.0.0.1:2220/group', 'Group', 'Group')
    group = h.spawn('group', Group)
    peer4 = h.spawn("peer4", Sequencer)

    print "se realizara el join en 4 segundos..."
    sleep(10)
    group.join(peer4)


    #comprobar que funciona el annnounce
    print "comprobacion announce"
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "peer0, peer1 y peer4 simularan que han caido:"
    peer4.stop_interval()
    sleep(20)
    print group.get_members()
    print group.get_members_name()

    shutdown()