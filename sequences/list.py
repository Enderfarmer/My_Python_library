class goodlist(list):
    def __init__(self, arg=None):
        super().__init__(arg) if arg else super().__init__()
    def to_string(self) -> str:
        return ''.join(self)

