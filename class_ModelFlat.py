from class_ModelIrregularRightPrism import ModelIrregularRightPrism
from class_ModelAbstractShape import ModelAbstractShape
import jsonpickle

"""ModelFlat class
"""


class ModelFlat(ModelIrregularRightPrism):

    def __init__(self, label="A flat", description="", *args, **kwargs):
        ModelIrregularRightPrism.__init__(self, label, description, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)






