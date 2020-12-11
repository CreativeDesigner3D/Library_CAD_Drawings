import bpy,os,inspect

from bpy.types import (Header, 
                       Menu, 
                       Panel, 
                       Operator,
                       PropertyGroup)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)
from . import cad_drawings_utils
from .pc_lib import pc_utils

class cad_drawings_OT_activate(Operator):
    bl_idname = "cad_drawings.activate"
    bl_label = "Activate Library"
    bl_options = {'UNDO'}
    
    library_name: StringProperty(name='Library Name')

    def execute(self, context):
        #Code to initalize library goes here
        #This can be left blank
        print('Activate Starter Library:',self.library_name)
        path = cad_drawings_utils.get_library_path()
        pc_utils.update_file_browser_path(context,path)
        return {'FINISHED'}

class cad_drawings_OT_drop(Operator):
    bl_idname = "cad_drawings.drop"
    bl_label = "Drop File"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        print('Drop File:',self.filepath)
        #This is called when a file is dropped with your library active
        return {'FINISHED'}

class cad_drawings_OT_generate_2d_drawings(Operator):
    bl_idname = "cad_drawings.generate_2d_drawings"
    bl_label = "Generate 2D Drawings"
    bl_options = {'UNDO'}
    
    #Generate Drawings from Walls, Assemblies
    def execute(self, context):
        props = cad_drawings_utils.get_scene_props(context.scene)
        dwg = props.drawings.add()
        dwg.name = "Drawing 1"
        return {'FINISHED'}

classes = (
    cad_drawings_OT_activate,
    cad_drawings_OT_drop,
    cad_drawings_OT_generate_2d_drawings,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
