import random
from pyactor.context import interval

class Peer(object):
    _tell = ['attach_group','add_message','announce','stop_interval','init_gossip_cycle']
    _ask = ['get_messages']
    _ref = ['attach_group']

    def __init__(self):
        self.messageList = {}    #conte la llista de chunks que te el peer

    def attach_group(self,group):
        self.group = group

    def add_message(self,message_id,message_data):
        self.messageList[message_id] = message_data

    def get_messages(self):
        return self.messageList

    def announce(self):
        self.group.announce(self.id)

    def stop_interval(self):
        self.time.set()

    def init_gossip_cycle(self):
        self.time = interval(self.host, 5, self.proxy, "announce")

