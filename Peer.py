from random import randint

from pyactor.exceptions import TimeoutError
import queue
from pyactor.context import interval, sleep
import time


class Peer(object):
    _tell = ['attach_group','announce','stop_interval','init_gossip_cycle','receive','process_msg']
    _ask = ['get_messages','get_name']
    _ref = ['attach_group']

    def __init__(self):
        self.orderedList = []           #conte la llista de chunks que te el peer
        self.orderingQueue = queue.Queue()
        self.queue_processed = -1                      #timestamp

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
            while self.queue_processed is not (message[0] - 1):
                self.orderingQueue.put(message)
                message = self.orderingQueue.get()
                if message[0] == first:
                    self.orderingQueue.put(message)
                    return
            self.orderedList.append(message)
            self.queue_processed += 1

    def receive(self,msg):
        self.orderingQueue.put(msg)
        self.timestamp += 1


class Sequencer(Peer):
    _tell = Peer._tell + ['set_sequencer','multicast','sequencer_dictadure']
    _ask = Peer._ask + ['get_number','get_timestamp','get_sequencer']
    _ref = Peer._ref + ['set_sequencer','sequencer_dictadure','get_sequencer']

    def __init__(self):
        Peer.__init__(self)
        self.timestamp = 0
        self.sequencer = Peer()

    def get_number(self):
        self.timestamp += 1
        return (self.timestamp-1,time.clock())

    def get_sequencer(self):
        return self.sequencer

    def set_sequencer(self,sequencer):
        self.sequencer = sequencer

    def get_timestamp(self):
        return self.timestamp

    def multicast(self, msg):
        try:
            #si es el sequencer no enviara mensaje
            if self.sequencer == self.proxy:
                return
            else:
                timestamp = self.sequencer.get_number()
            for i in self.group.get_members():
                i.receive((timestamp[0], msg, timestamp[1]))
        except TimeoutError:
            if not self.group.get_dictadure_state():
                self.group.set_dictadure_state()
                self.sequencer_dictadure()
            #else:
                #self.multicast(msg)

    def sequencer_dictadure(self):
        members = self.group.get_members()
        try:
            members.remove(self.sequencer)
        except:
            pass
        finally:
            best = (self.proxy,self.timestamp)
            for i in members:
                if not i == self.proxy:
                    timestamp = i.get_timestamp()
                    if timestamp > best[1]:
                        best = (i,timestamp)
            for i in members:
                if not i == self.proxy:
                    i.set_sequencer(best[0])
                else:
                    self.sequencer = best[0]
            self.group.set_dictadure_state()
            self.group.set_sequencer(best[0])





