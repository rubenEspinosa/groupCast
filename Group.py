from Peer import *
import random


class Group(object):
    _tell = ['init_start','update','leave','announce','set_sequencer']
    _ask = ['join','get_members','get_members_name','get_dictadure_state','set_dictadure_state','get_sequencer']
    _ref = ['join','announce','leave','get_members','set_sequencer','get_sequencer']

    def __init__(self):
        self.peerList = {}
        self.sequencer = Peer()
        self.dictadure_state = False

    def join(self,peer_ref):
        self.peerList[peer_ref] = 10
        peer_ref.attach_group(self.proxy)
        peer_ref.set_sequencer(self.sequencer)
        peer_ref.init_gossip_cycle()

    def announce(self,peer_ref):
        if self.peerList.has_key(peer_ref):
            self.peerList[peer_ref] = 10

    def init_start(self):
        self.time = interval(self.host, 1, self.proxy, "update")

    def set_sequencer(self,sequencer):
        self.sequencer = sequencer

    def get_sequencer(self):
        return self.sequencer

    def get_dictadure_state(self):
        if not self.dictadure_state:
            self.dictadure_state = True
            return False
        return self.dictadure_state

    def set_dictadure_state(self):
        self.dictadure_state = False

    def leave(self,peer_ref):
        peer_ref.stop_interval()
        self.peerList.pop(peer_ref)
        if peer_ref == self.sequencer:
            dictator = random.choice(self.peerList.keys())
            dictator.sequencer_dictadure()

    def get_members(self):
        return self.peerList.keys()

    def get_members_name(self):
        members = []
        for i in self.peerList.keys():
            members.append(i.get_name())
        return members

    def update(self):
        for i in self.peerList.keys():
            self.peerList[i] -= 1
            if self.peerList[i] <= 0:
                self.peerList.pop(i)



