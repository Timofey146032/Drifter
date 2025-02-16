import car.hpp
import carparticleeffectmanager.hpp
import carphysicscomponent.hpp
import carsoundeffectmanager.hpp
import game.hpp
import gearbox.hpp
import graphicsfactory.hpp
import layers.hpp
import renderer.hpp
import tire.hpp
import MCAssetManager
import MCDragForceGenerator
import MCForceRegistry
import MCFrictionGenerator
import MCPhysicsComponent
import MCWorld
import math
import string


class Description():
    accelerationFriction = 0.75
    rollingFrictionOnTrack = 0.1
    rotationFriction = 1.0
    power = 5000.0
    mass = 1500.0
    restitution = 0.05
    dragLinear = 1.0
    dragQuadratic = 5.0


class Car(Description, surface, size_t, isHuman):
    def __init__(self):
        self.m_desc = desc
        self.onTrackFriction = MC_friction_generator
        self.leftSideOffTrack = False
        self.rightSideOffTrack = False
        self.skidding = False
        self.steer = Steer
        self.index = index
        self.tireAngle = 0
        self.initDamageCapacity = 100
        self.damageCapacity = init_damage_capacity
        self.initTireWearOutCapacity = 100
        self.tireWearOutCapacity = m_initTireWearOutCapacity
        self.frontTire = front_tire
        self.brakeGlow = brake_glow
        self.speedInKmh = 0
        self.absSpeed = 0
        self.dx = 0
        self.dy = 0
        self.isHuman = is_human
        self.particleEffectManager = Car_particle_effect_manager(self)
        self.numberPos = (-5, 0, 0)
        self.leftFrontTirePos = (14, 9, 0)
        self.rightFrontTirePos = (14, -9, 0)
        self.leftRearTirePos = (-14, 9, 0)
        self.rightRearTirePos = (-14, -9, 0)
        self.leftBrakeGlowPos = (-21, 8, 0)
        self.rightBrakeGlowPos = (-21, -8, 0)
        self.hadHardCrash = False
        self.gearbox = Gearbox()
