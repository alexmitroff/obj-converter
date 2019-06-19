"""OBJ format name convention:
```
mtllib suzanne.mtl
o Suzanne
v 0.437500 0.164062 0.765625
...
vt 0.890955 0.590063
...
vn 0.6650 -0.2008 0.7194
...
usemtl None
s off
f 47/1/1 1/2/1 3/3/1 45/4/1

```
Also slots for Model class
"""

VERTEX = 'v'
TEXTURE_COORDINATE = 'vt'
NORMAL = 'vn'
FACE = 'f'

OBJECT_NAME = 'o'
SMOOTH_GROUP = 's'
MATERIAL_NAME = 'usemtl'
MATERIAL_FILE = 'mtllib'

SLOTS = (
    VERTEX,
    TEXTURE_COORDINATE,
    NORMAL,
    FACE,
)