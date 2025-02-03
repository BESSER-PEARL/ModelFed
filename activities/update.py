from models import Activity
from besser.BUML.metamodel.structural import *

def update_class(new_class: dict, class_obj: Class):
    print("class name: " + class_obj.name)
    print("new class name: " + new_class["name"])
    if new_class["name"] != class_obj.name:
        class_obj.name = new_class["name"]
    print("class name: " + class_obj.name)
    return