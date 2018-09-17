import jsonpickle

"""ModelMapObject class.

Mainly for decoration purposes.
"""


class ModelMapObject(object):

    def __init__(self, label="Object", description="", *args, **kwargs):
        print("ModelMapObject constructor")
        self.label = label
        self.description = description

    def __repr__(self):
        return jsonpickle.encode(self)

