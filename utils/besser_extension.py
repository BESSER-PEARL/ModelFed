from besser.BUML.metamodel.structural import Element

# id (property)
def id(self):
    return self._id

def id_setter(self, id: str):
    self._id = id

# attributed_to (property)
def attributed_to(self) -> str:
    return self._attributed_to

def attributed_to_setter(self, value: str):
    self._attributed_to = value

# grants (property)
def grants(self):
    if not hasattr(self, '_grants'):
        self._grants = set()
    return self._grants

def grants_setter(self, grants):
    self._grants = grants

# Apply monkey patching in BESSER
setattr(Element, 'id', property(id, id_setter))
setattr(Element, 'attributed_to', property(attributed_to, attributed_to_setter))
setattr(Element, 'grants', property(grants, grants_setter))
