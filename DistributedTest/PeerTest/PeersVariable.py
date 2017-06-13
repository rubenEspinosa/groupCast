from random import randint
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

    print "el sequencer que tienen asignado los peers al inicio del test es: "
    print sequencer.get_sequencer()
    for i in peers:
        print i.get_sequencer()

    print "se realizara un multicast..."
    rand = randint(1,5)
    for i in range(rand):
        peer=random.choice(peers)
        peer.multicast("mensaje"+str(i))

    sleep(2)

    print "mensajes recibidos despues del multicast:"
    for i in peers:
        print i.get_messages()

    #comprobar que funciona deteccion y eliminacion de peers caidos
    print "simularemos que el sequencer sale del grupo..."
    group.leave(sequencer)
    sleep(1)

    print "el nuevo sequencer asignado despues de la caida del sequencer es: "
    for i in peers:
        print i.get_sequencer()

    print "se realizara un nuevo multicast..."
    for i in range(rand, rand+randint(2,5)):
        peer = random.choice(peers)
        peer.multicast("mensaje" + str(i))

    sleep(2)

    print "mensajes recibidos despues del nuevo multicast"
    for i in peers:
        print i.get_messages()

    sleep(5)

    shutdown()