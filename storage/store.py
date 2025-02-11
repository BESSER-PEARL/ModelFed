user_inbox = {}
user_outbox = {}
objects = {}
grants = {}

def save_object(id_, obj):
    objects[str(id_)] = obj

def get_object(id_, raise_error=True):
    obj = objects.get(str(id_))
    if obj is None and raise_error:
        raise ValueError(f"Object with id '{id_}' does not exist")
    return obj

def delete_object(id_):
    if objects.pop(str(id_), None) is None:
        raise ValueError(f"Object with id '{id_}' does not exist")
    return True

def save_grant(id_, grant):
    grants[str(id_)] = grant

def get_grant(id_):
    grant = grants.get(str(id_))
    if grant is None:
        raise ValueError(f"Object with id '{id_}' does not exist")
    return grant

def get_grants(obj_id):
    matching_grants = [grant for grant in grants.values() if str(grant.modelElement) == str(obj_id)]
    return matching_grants

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