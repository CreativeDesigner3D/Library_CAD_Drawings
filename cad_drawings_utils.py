import bpy
import os

def get_library_path():
    return os.path.join(os.path.dirname(__file__),"library")

def get_scene_props(scene):
    return scene.cad_drawings