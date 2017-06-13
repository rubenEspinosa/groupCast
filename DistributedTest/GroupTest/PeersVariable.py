from Group import *
from pyactor.context import set_context, create_host, shutdown
from Peer import *

if __name__ == "__main__":
    peers = []

    set_context()

    h = create_host('http://127.0.0.1:1111/')

    group = h.lookup_url('http://127.0.0.1:2220/group', 'Group', 'Group')

    print "selecciona el numero de peers: "
    numero = int(input())

    sequencer = h.spawn("peer0", Sequencer)
    group.set_sequencer(sequencer)
    group.join(sequencer)

    for i in range(1,numero):
        peer_name = "peer" + str(i)
        p = h.spawn(peer_name, Sequencer)
        peers.append(p)

    for i in peers:
        group.join(i)

    #comprobar que funciona el annnounce
    print "comprobacion announce"
    sleep(15)
    print group.get_members()
    print group.get_members_name()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "simularemos que todos los peers menos peer0 salen del grupo:"
    for i in peers:
        i.stop_interval()

    sleep(15)
    print group.get_members()
    print group.get_members_name()

    shutdown()