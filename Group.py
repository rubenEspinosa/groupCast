import random
from pyactor.context import interval


class Group(object):
    _tell = ['join','init_start','update','leave','announce']
    _ask = ['get_members']

    def __init__(self):
        self.peerList = {}

    def join(self,peer_ref):
        self.peerList[peer_ref] = 10
        peer_ref.lookup().activarpeer
        #activar intervalo peer----------------------------------------------------------------

    def announce(self,peer_ref):
        if self.peerList.has_key(peer_ref):
            self.peerList[peer_ref] = 10

    def init_start(self):
        self.time = interval(self.host, 1, self.proxy, "update")

    def leave(self,torrent_hash,peer_ref):
        #parar intervalo peer------------------------------------------------------------------
        self.peerList.pop(peer_ref)

    def get_members(self,torrent_hash):
        return self.peerList.keys()

    def update(self):
        for i in self.peerList.keys():
            self.peerList[i] -= 1
            if self.peerList[i] <= 0:
                self.peerList.pop(i)

    #def setsequencer -> alforitmo de eleccion sequencer
    #def getSequencer
    #comprobar si sequencer falla con otro intervalo? en caso afirmativo volver a elegir sequencer
    #metodos sequencer
    #los peers llamaran a getseQuencer de la clase group antes de enviar mensaje
    #haran un lookup del sequencer obtenido
    #invocaran el metodo de obtener secuencia del secuencer (que hacen si sequencer peta?)


    #y si es el group el que hace de sequencer?? SE puede?