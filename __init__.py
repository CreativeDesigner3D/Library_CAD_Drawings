import bpy
from .pc_lib import pc_utils
from . import cad_drawings_ops
from . import cad_drawings_props
from . import cad_drawings_ui
from bpy.app.handlers import persistent

#Standard bl_info for Blender Add-ons
bl_info = {
    "name": "CAD Drawings",
    "author": "Andrew Peel",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Asset Library",
    "description": "This is library that helps create CAD style drawings",
    "warning": "",
    "wiki_url": "",
    "category": "Asset Library",
}

@persistent
def load_library_on_file_load(scene=None):
    pc_utils.register_library(name="CAD Drawings",
                              activate_id='cad_drawings.activate',
                              drop_id='cad_drawings.drop',
                              icon='FILE_HIDDEN')

#Standard register/unregister Function for Blender Add-ons
def register():
    cad_drawings_ops.register()
    cad_drawings_props.register()
    cad_drawings_ui.register()
    load_library_on_file_load()
    bpy.app.handlers.load_post.append(load_library_on_file_load)

def unregister():
    cad_drawings_ops.unregister()
    cad_drawings_props.unregister()
    cad_drawings_ui.unregister()

    bpy.app.handlers.load_post.remove(load_library_on_file_load)  

    pc_utils.unregister_library("CAD Drawings")

