# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_freeze_transform/

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class FREEZE_TRANSFORM_PT_panel(Panel):
    bl_idname = 'FREEZE_TRANSFORM_PT_panel'
    bl_label = 'Freeze Transform'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Freeze Transform'

    def draw(self, context):
        layout = self.layout
        layout.operator('freeze_transform.freeze', icon='FREEZE')
        row = layout.row()
        row.operator('freeze_transform.freeze', icon='RECOVER_LAST')
        row.operator('freeze_transform.freeze', icon='EMPTY_DATA')


def register():
    register_class(FREEZE_TRANSFORM_PT_panel)


def unregister():
    unregister_class(FREEZE_TRANSFORM_PT_panel)
