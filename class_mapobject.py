import jsonpickle

"""MapObject class.

Mainly for decoration purposes.
"""


class MapObject(object):

    def __init__(self, label="Object", description="", *args, **kwargs):
        print("MapObject constructor")
        self.label = label
        self.description = description

    def __repr__(self):
        return jsonpickle.encode(self)

