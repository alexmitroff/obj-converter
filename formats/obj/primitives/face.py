import numpy as np
from formats.obj.primitives.vertex import VertexDataIndexes


class Face:
    """Face class

    Attrs:
        `list_of_vertices` (list of string): 'vertex_index/t_coord_index/normal_index'

    Properties:
        `vertices` (numpy Array): array of VertexDataIndexes
        `as_vector` (numpy Array)

    Usage:
        ```
        from formats.obj.primitives.face import Face

        list_of_vertices = [ '1/5/6', '10/2/1', ... ]
        face = Face(list_of_vertices)

        print(face.vertices)
        print(face.as_vector)
        ```
    """

    __slots__ = 'vertices'

    def __init__(self, list_of_vertices):
        vertices = None
        for vertex_data in list_of_vertices:
            vertex_data = VertexDataIndexes(vertex_data.split('/')).as_vector
            if vertices is not None:
                np.vstack([vertices, vertex_data])
            vertices = vertex_data
        self.vertices = vertices

    @property
    def as_vector(self):
        return self.vertices
