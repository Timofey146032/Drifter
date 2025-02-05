from enum import Enum
from pygame.math import Vector2


class Description(Enum):
    accelerationFriction = 0.75
    rollingFrictionOnTrack = 0.1
    rotationFriction = 1.0
    power = 5000.0
    mass = 1500.0
    restitution = 0.05
    dragLinear = 1.0
    dragQuadratic = 5.0


class Car(pygame.sprite.Sprite, Description):
    def __init__(self, desk, surface, index, isHuman, *group):
        super().__init__(*group)
        self.size = size
        self.desc = desc
        self.onTrackFriction = MFrictionGenerator(desc.rollingFrictionOnTrack, 0)
        ...

    def createTires(self):
        offTrackFrictionFactor = 0.8
        frontFriction = 0.85
        leftFrontTire = Tire(self, frontFriction, frontFriction * offTrackFrictionFactor)
