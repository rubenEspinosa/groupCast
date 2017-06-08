from pyactor.context import set_context, create_host, shutdown , sleep
from Group import *
from Peer import *


if __name__ == "__main__":
    set_context()
    h = create_host()

    group=h.spawn('tracker1',Group)

    peer0 = h.spawn("peer0", Peer)
    peer1 = h.spawn("peer1", Peer)
    peer2 = h.spawn("peer2", Peer)
    peer3 = h.spawn("peer3", Peer)
    peer4 = h.spawn("peer4", Peer)
    peer5 = h.spawn("peer5", Peer)
    peer6 = h.spawn("peer6", Peer)
    peer7 = h.spawn("peer7", Peer)
    peer8 = h.spawn("peer8", Peer)
    peer9 = h.spawn("peer9", Peer)

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

    sleep(11)

    print group.get_members()

    shutdown()