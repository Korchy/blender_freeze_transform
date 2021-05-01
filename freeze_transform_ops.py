# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_freeze_transform/

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .freeze_transform import FreezeTransform


class FREEZE_TRANSFORM_OT_freeze(Operator):
    bl_idname = 'freeze_transform.freeze'
    bl_label = 'Freeze Transform'
    bl_description = 'Save current object world transformation'
    bl_options = {'REGISTER'}

    def execute(self, context):
        FreezeTransform.freeze_transform(
           context=context
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.object


def register():
    register_class(FREEZE_TRANSFORM_OT_freeze)


def unregister():
    unregister_class(FREEZE_TRANSFORM_OT_freeze)
