import numpy as np

from formats.obj.primitives.face import Face
from formats.obj.primitives.normal import Normal
from formats.obj.primitives.texture_coordinate import TextureCoordinate
from formats.obj.primitives.vertex import Vertex
from formats.obj.settings import *


class ObjProcessor:
    primitives = {
        VERTEX: Vertex,
        TEXTURE_COORDINATE: TextureCoordinate,
        NORMAL: Normal,
        FACE: Face
    }

    @classmethod
    def process_promitive(cls, primitive_name, coord_list, storage=None):
        vector = cls.primitives[primitive_name](coord_list).as_vector
        if storage is not None:
            return np.vstack([storage, vector])
        return vector
