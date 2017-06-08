from pyactor.context import set_context, create_host, shutdown , sleep
from Group import *


if __name__ == "__main__":
    set_context()
    h = create_host()

    tracker=h.spawn('tracker1',Group)

    tracker.join('peer1')
    tracker.join('peer2')
    tracker.join('peer5')
    tracker.join('peer6')
    tracker.join('peer3')
    tracker.join('peer4')
    tracker.join('peer7')
    tracker.join('peer8')
    tracker.join('peer9')
    tracker.join('peer10')
    tracker.join('peer11')
    tracker.join('peer12')
    tracker.join('peer13')
    tracker.join('peer14')
    tracker.join('peer15')
    tracker.join('peer16')
    tracker.join('peer17')
    tracker.join('peer18')
    tracker.join('peer19')
    tracker.join('peer20')
    tracker.join('peer3')



    tracker.init_start()

    sleep(11)

    print tracker.get_members('peli1')

    shutdown()