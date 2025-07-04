import bpy
import pytest
from .. import animutils  # Import aus deinem Plugin-Root

class TestAnimUtils:
    """Testet die animutils.py-Funktionen."""

    def setup_method(self):
        """Vor jedem Test: Frische Szene erstellen."""
        bpy.ops.wm.read_factory_settings(use_empty=True)
        self.armature = bpy.data.armatures.new("TestArmature")
        self.obj = bpy.data.objects.new("TestArmatureObj", self.armature)
        bpy.context.scene.collection.objects.link(self.obj)

    def test_bone_creation(self):
        """Prüft, ob Bones korrekt erstellt werden."""
        bone_name = "TestBone"
        animutils.create_bone(self.obj, bone_name, head=(0, 0, 0), tail=(0, 1, 0))
        assert bone_name in self.obj.data.bones

    def test_keyframe_insertion(self):
        """Testet das Keyframe-Setting."""
        animutils.insert_keyframe(self.obj, "location", frame=1)
        assert self.obj.animation_data.action.fcurves[0].keyframe_points[0].co.x == 1

    def test_animation_copy(self):
        """Prüft das Kopieren von Animationen."""
        target_obj = bpy.data.objects.new("Target", None)
        bpy.context.scene.collection.objects.link(target_obj)
        
        animutils.copy_animation(self.obj, target_obj)
        assert target_obj.animation_data is not None

    def test_constraint_creation(self):
        """Testet Constraint-Hinzufügung."""
        animutils.add_constraint(self.obj, "COPY_LOCATION")
        assert "COPY_LOCATION" in self.obj.constraints