import bpy
import os
from bpy.types import (
        Operator,
        Panel,
        PropertyGroup,
        UIList,
        )
from bpy.props import (
        BoolProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        CollectionProperty,
        EnumProperty,
        )

def update_drawing_index(self,context):
    pass
    #Set Active Scene

class Drawing(bpy.types.PropertyGroup):
    drawing_type: EnumProperty(name="Drawing type", 
                                 description="This is the collection of drawings",
                                 items=[('PLAN',"Plan","Top Down view of a drawing"),
                                        ('ELEVATION',"Elevation","Front view of a drawing"),
                                        ('ASSEMBLY',"Assemby","Assembly Drawing")],
                                 default='ASSEMBLY')

    scene: PointerProperty(name="Scene",type=bpy.types.Scene)


class CAD_Drawings_Scene_Props(PropertyGroup):
    drawings: CollectionProperty(type=Drawing, name="Drawings")
    drawing_index: IntProperty(name="Drawing Index",update=update_drawing_index)

    library_enum: EnumProperty(name="Library Tabs",
                               items=[('OPTION1',"Option 1","Example Enum"),
                                      ('OPTION2',"Option 2","Example Enum"),
                                      ('OPTION3',"Option 3","Example Enum")],
                               default='OPTION1')

    library_bool: BoolProperty(name="Bool")
    library_float: FloatProperty(name="Float")
    library_string: StringProperty(name="String")
    library_int: IntProperty(name="Int")

    @classmethod
    def register(cls):
        bpy.types.Scene.cad_drawings = PointerProperty(
            name="CAD Drawings Props",
            description="CAD Drawings Props",
            type=cls,
        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.cad_drawings

classes = (
    Drawing,
    CAD_Drawings_Scene_Props,
)

register, unregister = bpy.utils.register_classes_factory(classes)        