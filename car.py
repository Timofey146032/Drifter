class Description():
    accelerationFriction = 0.75
    rollingFrictionOnTrack = 0.1
    rotationFriction = 1.0
    power = 5000.0
    mass = 1500.0
    restitution = 0.05
    dragLinear = 1.0
    dragQuadratic = 5.0


class Car(pygame.sprite.Sprite, Description):
    def __init__ (self, size, health, *group):
        super().__init__(*group)
        size = self.size
