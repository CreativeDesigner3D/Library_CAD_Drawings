import bpy
import os
from .pc_lib import pc_utils
from . import cad_drawings_utils

class FILEBROWSER_PT_cad_drawings_headers(bpy.types.Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'UI'
    bl_label = "Library"
    bl_category = "Attributes"
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        #Only display when active and File Browser is not open as separate window
        if len(context.area.spaces) > 1:
            pyclone = pc_utils.get_scene_props(context.scene)
            if pyclone.active_library_name == 'CAD Drawings':
                return True   
        return False

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="CAD Drawings")
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Library")        


class VIEW3D_PT_cad_drawings(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CAD Drawings"
    bl_label = "CAD Drawings"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        props = cad_drawings_utils.get_scene_props(context.scene)
        layout.operator('cad_drawings.generate_2d_drawings',icon='FILE_HIDDEN')
        col = layout.column(align=True)
        col.template_list("CD_UL_drawings"," ", props, "drawings", props, "drawing_index",rows=5)


class CD_UL_drawings(bpy.types.UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name)        


classes = (
    FILEBROWSER_PT_cad_drawings_headers,
    VIEW3D_PT_cad_drawings,
    CD_UL_drawings
)

register, unregister = bpy.utils.register_classes_factory(classes)                