from pyactor.context import interval
import queue

class Peer:
    _tell = ['attach_group','announce','stop_interval','init_gossip_cycle','receive','process_msg']
    _ask = ['get_messages','get_name']
    _ref = ['attach_group','announce']

    def __init__(self):
        self.orderedList = []           #conte la llista de chunks que te el peer
        self.orderingQueue = queue.Queue()
        self.ts = 0                      #timestamp

    def attach_group(self,group):
        self.group = group

    def get_messages(self):
        return self.orderedList

    def get_name(self):
        return self.id

    def announce(self):
        self.group.announce(self.proxy)

    def stop_interval(self):
        self.time.set()
        self.orderMessages.set()

    def init_gossip_cycle(self):
        self.time = interval(self.host, 5, self.proxy, "announce")
        self.orderMessages = interval(self.host, 1, self.proxy, "process_msg")

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


class Sequencer(Peer):
    _tell = Peer._tell + ['set_sequencer','multicast','sequencer_dictadure']
    _ask = Peer._ask + ['get_number']
    _ref = Peer._ref + ['set_sequencer']

    def __init__(self):
        Peer.__init__(self)
        self.timestamp = 0

    def get_number(self):
        self.timestamp += 1
        return self.timestamp-1

    def set_sequencer(self,sequencer):
        self.sequencer = sequencer

    def multicast(self, msg):
        try:
            timestamp = self.sequencer.get_number(timeout=2)
        except Exception:
            self.group.sequencer_dictadure(self.proxy)
        for i in self.group.get_members():
            i.receive(timestamp, msg)

    def sequencer_dictadure(self,dictator):
        for i in self.peerList.keys():
            i.set_sequencer(dictator)



