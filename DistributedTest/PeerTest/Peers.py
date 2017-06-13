from Group import *
from pyactor.context import set_context, create_host, shutdown
from Peer import *

if __name__ == "__main__":
    set_context()

    h = create_host('http://127.0.0.1:1111/')

    group = h.lookup_url('http://127.0.0.1:2220/group', 'Group', 'Group')

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

    group.set_sequencer(peer0)

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

    peer0.multicast("mensaje1")
    peer6.multicast("mensaje2")
    peer1.multicast("mensaje3")
    peer2.multicast("mensaje4")
    peer5.multicast("mensaje5")
    peer7.multicast("mensaje6")

    sleep(3)

    print "los mensajes guardados son:"
    print peer0.get_messages()
    print peer1.get_messages()
    print peer3.get_messages()
    print peer4.get_messages()
    print peer5.get_messages()
    print peer6.get_messages()
    print peer7.get_messages()
    print peer8.get_messages()
    print peer9.get_messages()

    #simularemos que el sequencer actual (peer0) ha salido del grupo.
    #Esto generara dictadura para elegir el nuevo sequencer
    group.leave(peer0)
    sleep(5)

    print "El nuevo lider elegido despues del leave de sequencer0 es:"
    print peer1.get_sequencer()
    print peer2.get_sequencer()
    print peer3.get_sequencer()
    print peer4.get_sequencer()
    print peer5.get_sequencer()
    print peer6.get_sequencer()
    print peer7.get_sequencer()
    print peer8.get_sequencer()
    print peer9.get_sequencer()

    print "enviamos mas mensajes para ver que el timestamp sigue siendo correcto:"
    peer6.multicast("mensaje7")
    peer1.multicast("mensaje8")
    peer2.multicast("mensaje9")

    sleep(5)

    print "los mensajes guardados son:"
    print peer1.get_messages()
    print peer3.get_messages()
    print peer4.get_messages()
    print peer5.get_messages()
    print peer6.get_messages()
    print peer7.get_messages()
    print peer8.get_messages()
    print peer9.get_messages()

    sleep(5)



    shutdown()
