# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_freeze_transform/

from . import freeze_transform_ops
from . import freeze_transform_ui
from . import freeze_transform_props
from .addon import Addon


bl_info = {
    'name': 'Freeze Transform',
    'category': 'Object',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 83, 0),
    'location': '3D Viewport',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-freeze-transform/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-freeze-transform/',
    'description': 'Save and restore object world transformation'
}


def register():
    if not Addon.dev_mode():
        freeze_transform_props.register()
        freeze_transform_ops.register()
        freeze_transform_ui.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        freeze_transform_ui.unregister()
        freeze_transform_ops.unregister()
        freeze_transform_props.unregister()


if __name__ == '__main__':
    register()
