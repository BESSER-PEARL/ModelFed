from models import Activity
from storage import get_grants

def check_permission(activity: Activity) -> bool:
    """Checks if the actor has permission to perform the activity on the target."""
    grants = get_grants(activity.target)
    if activity.type == "Create":
        for grant in grants:
            if str(grant.user) == str(activity.actor) and (grant.role in {"admin", "write"}):
                return True
    elif activity.type == "Update":
        for grant in grants:
            if str(grant.user) == str(activity.actor) and grant.role in {"admin", "write"}:
                return True
    elif activity.type == "Delete":
        for grant in grants:
            if str(grant.user) == str(activity.actor) and grant.role == "admin":
                return True
    return False
