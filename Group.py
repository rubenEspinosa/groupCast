from pyactor.context import interval


class Group(object):
    _tell = ['join','init_start','update','leave','announce']
    _ask = ['get_members','get_members_name']
    _ref = ['join','announce','leave','get_members']

    def __init__(self):
        self.peerList = {}
        self.number_peers= 0

    def join(self,peer_ref):
        self.peerList[peer_ref] = 10
        peer_ref.attach_group(self.proxy)
        peer_ref.init_gossip_cycle()
        self.number_peers += 1
        peer_ref.set_peer_number(self.number_peers)

    def announce(self,peer_ref):
        if self.peerList.has_key(peer_ref):
            self.peerList[peer_ref] = 10

    def init_start(self):
        self.time = interval(self.host, 1, self.proxy, "update")

    def leave(self,peer_ref):
        peer_ref.stop_interval()
        self.peerList.pop(peer_ref)

    def get_members(self):
        return self.peerList.keys()

    def get_members_name(self):
        for i in self.get_members():
            print i.get_name()

    def update(self):
        for i in self.peerList.keys():
            self.peerList[i] -= 1
            if self.peerList[i] <= 0:
                self.peerList.pop(i)

    def sequencer_election(self):
        #bully
        print "miau"

    def get_sequencer(self):
        return self.sequencer

    #comprobar si sequencer falla con otro intervalo? en caso afirmativo volver a elegir sequencer
    #metodos sequencer
    #los peers llamaran a getseQuencer de la clase group antes de enviar mensaje
    #invocaran el metodo de obtener secuencia del secuencer (que hacen si sequencer peta?)


    #y si es el group el que hace de sequencer?? SE puede?
