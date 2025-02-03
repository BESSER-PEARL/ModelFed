from besser.BUML.metamodel.structural import Element

# Define a backing variables
private_id = "_id"
_private_attributed_to = "_attributed_to"
_private_users = "_users"

# id
@property
def id(self):
    return getattr(self, private_id, None)

@id.setter
def id(self, id: str):
    setattr(self, private_id, id)

# attributed_to
@property
def attributed_to(self) -> str:
    return getattr(self, _private_attributed_to, None)

@attributed_to.setter
def attributed_to(self, value: str):
    setattr(self, _private_attributed_to, value)

# users
@property
def users(self) -> [str]:
    return getattr(self, _private_users, [])

@users.setter
def users(self, value: [str]):
    setattr(self, _private_users, value)

# Apply monkey patching: Add the property to the Element class
Element.id = id
Element.attributed_to = attributed_to
Element.users = users