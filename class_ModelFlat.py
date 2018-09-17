from class_ModelBaseShape import ModelBaseShape
from class_ModelMapObject import ModelMapObject
import jsonpickle

"""ModelFlat class
"""


class ModelFlat(ModelMapObject, ModelBaseShape):

    def __init__(self, label="A flat", description="", *args, **kwargs):
        print("ModelFlat constructor")
        ModelMapObject.__init__(self, label, description, *args, **kwargs)
        ModelBaseShape.__init__(self, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)






