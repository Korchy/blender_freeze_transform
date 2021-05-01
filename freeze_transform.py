# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_freeze_transform/

class FreezeTransform:

    @staticmethod
    def freeze_transform(objects):
        # Save world transform matrix for objects
        if not isinstance(objects, list):
            objects = [objects]
        for obj in objects:
            obj.freeze_transform_matrix.matrix = obj.matrix_world.copy()
            obj.freeze_transform_flag = True

    @staticmethod
    def to_frozen(objects):
        # Return object to frozen transform
        if not isinstance(objects, list):
            objects = [objects]
        for obj in objects:
            if obj.freeze_transform_flag:
                obj.matrix_world = obj.freeze_transform_matrix.matrix

    @staticmethod
    def reset_transform(objects):
        # Reset world transform matrix for obj
        if not isinstance(objects, list):
            objects = [objects]
        for obj in objects:
            obj.matrix_world = (
                (1.0, 0.0, 0.0, 0.0),
                (0.0, 1.0, 0.0, 0.0),
                (0.0, 0.0, 1.0, 0.0),
                (0.0, 0.0, 0.0, 1.0)
            )
