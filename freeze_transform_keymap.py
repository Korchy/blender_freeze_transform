# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_freeze_transform/

import bpy


class FreezeTransform_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
            # add keys
            keymap_item = keymap.keymap_items.new('freeze_transform.freeze', 'F', 'PRESS', ctrl=True, shift=True)
            cls._keymaps.append((keymap, keymap_item))
            keymap_item = keymap.keymap_items.new('freeze_transform.to_frozen', 'F', 'PRESS', ctrl=True, alt=True)
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        # clear keys
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    FreezeTransform_KeyMap.register(context=bpy.context)


def unregister():
    FreezeTransform_KeyMap.unregister()
