from abc import ABC
from typing import Optional, List
import weakref

class MCObject:

    def __init__(self, mass):
        self.mass = mass
        self.forces = []

    def apply_force(self, force):
        self.forces.append(force)

    def get_mass(self):
        return self.mass

    def clear_forces(self):
        self.forces.clear()

    def get_forces(self):
        return self.forces


class MCForceGenerator(ABC):

    def __init__(self):
        self._enabled = True

    def update_force(self, obj: MCObject):
        pass

    def enable(self, status: bool):
        self._enabled = status

    def enabled(self) -> bool:
        return self._enabled


class MCGravityForce(MCForceGenerator):
    def __init__(self, gravity_magnitude: float):
        super().__init__()
        self.gravity_magnitude = gravity_magnitude

    def update_force(self, obj: MCObject):
        if self.enabled():
            mass = obj.get_mass()
            force = (0, -self.gravity_magnitude * mass, 0)
            obj.apply_force(force)


class ForceManager:
    def __init__(self):
        self._force_generators: List[weakref.ref[MCForceGenerator]] = []

    def add_force_generator(self, force_generator: MCForceGenerator):
        self._force_generators.append(weakref.ref(force_generator))

    def apply_forces(self, obj: MCObject):
        obj.clear_forces()
        for ref in self._force_generators:
            force_generator = ref()
            if force_generator:
                force_generator.update_force(obj)


if __name__ == "__main__":
    my_object = MCObject(mass=10.0)
    gravity = MCGravityForce(gravity_magnitude=9.81)
    force_manager = ForceManager()
    force_manager.add_force_generator(gravity)
    force_manager.apply_forces(my_object)
    gravity.enable(False)
    force_manager.apply_forces(my_object)
