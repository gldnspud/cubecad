"""Schema for CubeCAD."""

from schevo.schema import *
schevo.schema.prep(locals())


class SchevoIcon(E.Entity):
    """Stores icons for Schevo database and application objects."""

    _hidden = True

    name = f.string()
    data = f.image()

    _key(name)
