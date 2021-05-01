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
    bl_description = 'Save selected objects world transformation'
    bl_options = {'REGISTER'}

    def execute(self, context):
        FreezeTransform.freeze_transform(
           objects=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects


class FREEZE_TRANSFORM_OT_to_fozen(Operator):
    bl_idname = 'freeze_transform.to_frozen'
    bl_label = 'To Frozen'
    bl_description = 'Move current object to frozen point'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        FreezeTransform.to_frozen(
           objects=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects


class FREEZE_TRANSFORM_OT_reset_transform(Operator):
    bl_idname = 'freeze_transform.reset_transform'
    bl_label = 'Reset Transform'
    bl_description = 'Reset world transform'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        FreezeTransform.reset_transform(
           objects=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects


def register():
    register_class(FREEZE_TRANSFORM_OT_freeze)
    register_class(FREEZE_TRANSFORM_OT_to_fozen)
    register_class(FREEZE_TRANSFORM_OT_reset_transform)


def unregister():
    unregister_class(FREEZE_TRANSFORM_OT_reset_transform)
    unregister_class(FREEZE_TRANSFORM_OT_to_fozen)
    unregister_class(FREEZE_TRANSFORM_OT_freeze)
