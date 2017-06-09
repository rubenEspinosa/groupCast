from pyactor.context import interval
import Queue

class Peer(object):
    _tell = ['attach_group','add_message','announce','stop_interval','init_gossip_cycle','multicast','receive']
    _ask = ['get_messages','get_name','multicast']
    _ref = ['attach_group','announce','multicast']

    def __init__(self):
        self.orderedList = []           #conte la llista de chunks que te el peer
        self.orderingQueue = Queue()
        self.ts = 0                      #timestamp

    def attach_group(self,group):
        self.group = group

    def add_message(self,message_id,message_data):
        self.orderedList[message_id] = message_data

    def get_messages(self):
        return self.orderedList

    def get_name(self):
        return self.id

    def announce(self):
        self.group.announce(self.proxy)

    def stop_interval(self):
        self.time.set()
        self.readMessages.set()

    def init_gossip_cycle(self):
        self.time = interval(self.host, 5, self.proxy, "announce")
        self.order = interval(self.host, 1, self.proxy, "process_msg")

    def process_msg(self):
        while not self.orderingQueue.empty():
            message = self.orderingQueue.get()
            first = message[0]
            while self.ts is not (message[0] - 1):
                self.orderingQueue.put(message)
                message = self.orderingQueue.get()
                if message[0] == first:
                    self.orderingQueue.put(message)
                    return
            self.orderedList.append(message)
            self.ts += 1

    def receive(self,msg):
        self.orderingQueue.put(msg)

    def multicast(self, msg):
        timestamp=
        for i in self.group.get_members():
            i.receive(msg)

class Sequencer(Peer):
    _tell = Peer._tell + []
    _ask = Peer._ask+ []
    _ref = Peer.ref + []
