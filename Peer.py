from pyactor.exceptions import TimeoutError
import queue
from pyactor.context import interval
import time


class Peer:
    _tell = ['attach_group','announce','stop_interval','init_gossip_cycle','receive','process_msg']
    _ask = ['get_messages','get_name']
    _ref = ['attach_group','announce']

    def __init__(self):
        self.orderedList = []           #conte la llista de chunks que te el peer
        self.orderingQueue = queue.Queue()
        self.ts = -1                      #timestamp

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
    _ref = Peer._ref + ['set_sequencer','sequencer_dictadure']

    def __init__(self):
        Peer.__init__(self)
        self.timestamp = 0
        self.sequencer = Peer()

    def get_number(self):
        self.timestamp += 1
        return (self.timestamp-1,time.clock())

    def set_sequencer(self,sequencer):
        self.sequencer = sequencer

    def multicast(self, msg):
        if self.sequencer == self.proxy:
           timestamp= self.get_number()
        else:
            timestamp = self.sequencer.get_number()
        #en caso de morir el sequencer hace un golpe de estado
        #self.sequencer_dictadure()
        for i in self.group.get_members():
            i.receive((timestamp[0], msg,timestamp[1]))

    def sequencer_dictadure(self):
        for i in self.group.get_members():
            i.set_sequencer(self.proxy)



