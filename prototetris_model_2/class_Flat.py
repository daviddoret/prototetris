from prototetris_model_2.class_IrregularRightPrism import IrregularRightPrism
import jsonpickle

"""Flat class
"""


class Flat(IrregularRightPrism):

    def __init__(self, label="A flat", description="", *args, **kwargs):
        IrregularRightPrism.__init__(self, label, description, *args, **kwargs)

    def __repr__(self):
        return jsonpickle.encode(self)






