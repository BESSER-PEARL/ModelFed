domain_models = {}
user_inbox = {}
user_outbox = {}

def save_model(id, domain_model):
    """Save the domain model in a dictionary."""
    domain_models[id] = domain_model

def get_model(id):
    """Get the domain model."""
    return domain_models.get(id)

def get_domain_models():
    """Get the dictionary of domain models."""
    return domain_models

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