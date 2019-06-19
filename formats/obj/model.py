from formats.obj.processor import ObjProcessor
from formats.obj.settings import *


class Model:
    __slots__ = SLOTS

    def __init__(self):
        for slot in self.__slots__:
            setattr(self, slot, None)

    def read_obj(self, obj_file):
        for line in obj_file:
            line = line.rstrip()
            data_list = line.split(' ')
            primitive_name = data_list.pop(0)

            if hasattr(self, primitive_name):
                storage = getattr(self, primitive_name)
                new_storage = ObjProcessor.process_promitive(primitive_name, data_list, storage)
                setattr(self, primitive_name, new_storage)

        # TEST
        print(f'Vertices number: {self.v.shape[0]}')
        print(f'Texture coordinates number: {self.vt.shape[0]}')
        print(f'Normals number: {self.vn.shape[0]}')
        print(f'Faces number: {self.f.shape[0]}')
