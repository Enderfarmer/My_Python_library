from typing import Iterable, Sequence
class gooddict(dict):
    """
    A version of a Python dictionary but with more methods
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs) if kwargs else super().__init__()
    def items_from_seq(self, keys, values):
        shorter = len(keys) if len(keys) < len(values) else len(values)
        try:
            if issubclass(keys.__class__, Sequence) and issubclass(values.__class__, Sequence):
                
                    for i in range(shorter):
                       self.__setitem__(keys[i], values[i])
        except:
            raise SyntaxError('Invalid method syntax.')
    def setitem(self, key, val):
        self.__setitem__(key, val)
    
