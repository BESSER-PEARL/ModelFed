user_inbox = {}
user_outbox = {}
objects = {}

def save_object(obj):
    objects[obj.id] = obj

def get_object(id_, raise_error=True):
    obj = objects.get(id_)
    if obj is None and raise_error:
        raise ValueError(f"Object with id '{id_}' does not exist")
    return obj

def delete_object(id_):
    if objects.pop(id_, None) is None:
        raise ValueError(f"Object with id '{id_}' does not exist")
    return True

def save_inbox_activity(username, activity):
    if username in user_inbox:
        user_inbox[username].append(activity)
    else:
        user_inbox[username] = [activity]

def get_inbox(username):
    return user_inbox.get(username, {})

def save_outbox_activity(username, activity):
    if username in user_outbox:
        user_outbox[username].append(activity)
    else:
        user_outbox[username] = [activity]

def get_outbox(username):
    return user_outbox.get(username, {})