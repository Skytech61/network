class Packet:
    
    _sn = 0
    
    def __init__(self, size=320, content=None):
        self.size = size
        self.content = content
        self._sn = Packet._sn
        Packet._sn += 1
    
    def __repr__(self):
        if self.content != None:
            return f'Packet(sn={self._sn}, size={self.size}B, content={self.content})'
        else:
            return f'Packet(sn={self._sn}, size={self.size}B)'