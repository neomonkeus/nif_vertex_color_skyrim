#--- ### Header
bl_info = {
           "name": "Niftools - Utilities",
           "description": "Utilities for nif related ",
           "author": "Neomonkeus",
           "version": (1, 0, 0),
           "blender:": (2, 6, 1),
           "api": 35622,
           "location": "Scene Properties Tab -> Niftools Utilities Panel",
           "warning": "not functional, porting from 2.49 series still in progress",
           "wiki_url": (
                        "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/"\
                        "Import-Export/Nif"),
           "tracker_url": (
                           "http://sourceforge.net/tracker/?group_id=149157&atid=776343"),
           "support": "COMMUNITY",
           "category": "Mesh"}

import bpy
import bpy.props
from . import ui
from . import operators

class PathProperties(bpy.types.PropertyGroup):
       
    #---operator parameters
    fileinput = bpy.props.StringProperty(name='Input', subtype='FILE_PATH', default="")   #, update=updatepath          
    fileoutput = bpy.props.StringProperty(name='Output', subtype='FILE_PATH', default="")
    hexwidget = bpy.props.FloatVectorProperty(name='Hex Value', subtype='COLOR', default=[0.0,0.0,0.0])

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.vertexcolor = bpy.props.PointerProperty(type=PathProperties)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.vertexcolor
    
if __name__ == "__main__":
    register()