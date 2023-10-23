import numpy as np
import random

# Sim-Defining Editable Variables

planet_radius = 2439000  # m, Mercury
surface_gravity = 3.705  # m/s^2, Mercury
temp_in_light = 500  # K, can go back and make more complex later
rotational_speed = 3.026  # m/s, planetary rotation
radius_poles = 300000  # m, location of stable regions
num_particles = 1000
polar_deg = radius_poles/(np.pi*planet_radius)*180

# Setup (Pre-defined/Empty Variables, etc)

time_factor = 20
sun_time_factor = 40
angle_per_m = 360/(2*np.pi*planet_radius)
escape_vel = 4300
photo_loss = 10000  # s, photodestruction loss timescale


def random_polar_coords():
    """
    Generates uniformly distributed random polar coordinates on the surface of the sphere

    Returns:
        list: The random coordinate, in the form [radius, polar angle, azimuth angle]
    """
    rand_u = random.random()
    rand_v = random.random()
    phi = 360*rand_u
    # Unclusters the final distibution from around the poles
    # theta = np.arccos(2*rand_v - 1)
    theta = 180*rand_v
    return [planet_radius, theta, phi]


class System:

    def __init__(self):
        self.particles_active = []
        self.particles_caught = []
        self.particles_lost = []
        self.sun_pos = 0  # phi of the furthestmost clockwise edge of sunlight

    def update_model(self):
        for particle in self.particles_active:
            particle.move(self.sun_pos)
            if particle.is_caught():
                self.particles_caught.append(particle)
            if particle.lost:
                self.particles_lost.append(particle)
        self.particles_active = [
            particle for particle in self.particles_active if not particle.is_caught() and not particle.lost]
        self.sun_pos += rotational_speed*angle_per_m*time_factor*sun_time_factor
        self.sun_pos = self.sun_pos % 360

    def first_spawn(self):
        # spawn num_particles particles
        for _ in range(num_particles):
            self.particles_active.append(Particle())


class Particle:

    def __init__(self):
        self.coordinates = random_polar_coords()
        self.hop = None
        self.lost = False

    def move(self, sun_pos):
        # Continue current hop
        if self.hop != None:
            self.coordinates = self.hop.move()
        # Or start a new one!
        elif self.inside_sunlight(sun_pos):
            self.hop = Hop(self.coordinates)
            if self.hop.start_vel[0] > escape_vel:
                self.lost = True

        # VERY clunky way to deal with a particle landing on the surface
        if self.coordinates[0] < planet_radius:
            self.lost = self.photo_lost(
                self.hop.elapsed_time)  # Photodissociation
            self.coordinates[0] = planet_radius
            self.hop = None

    def is_caught(self):
        if self.coordinates[1] > 180-polar_deg or self.coordinates[1] < polar_deg:
            return True
        return False

    def inside_sunlight(self, sun_pos):
        # checks if coordinates are inside the current area of sunlight
        if sun_pos <= self.coordinates[2] <= sun_pos+180:
            return True
        if self.coordinates[2] < sun_pos-180:
            return True
        return False

    def photo_lost(self, time):
        P = 1 - np.exp(-1*time/photo_loss)
        if random.random() < P:
            return True
        return False


class Hop:

    def __init__(self, coords):
        self.elapsed_time = 0
        self.start_vel = self.init_velocity()
        self.current_pos = coords  # starting coords
        self.current_vel = self.start_vel
        self.current_accl = [-surface_gravity, 0, 0]

    def move(self):
        self.calculate_pos()
        self.calculate_vel()
        self.calculate_accl()
        self.elapsed_time += time_factor

        return self.current_pos

    def calculate_pos(self):
        self.current_pos = list(map(
            lambda a, b: a+b*time_factor, self.current_pos, self.current_vel))
        self.current_pos[2] = self.current_pos[2] % 360

    def calculate_vel(self):
        self.current_vel = list(map(
            lambda a, b: a+b*time_factor, self.current_vel, self.current_accl))

    def calculate_accl(self):
        current_grav = surface_gravity * \
            (planet_radius/(planet_radius + self.current_pos[0])) ** 2
        self.current_accl = [-current_grav, 0, 0]

    def init_velocity(self):
        launch_angle = random.random()*np.pi/2  # Ordinary Maxwell distribution
        launch_direction = random.random()*2*np.pi
        launch_polar = [np.sin(launch_angle),
                        np.cos(launch_angle)*np.cos(launch_direction),
                        np.cos(launch_angle)*np.sin(launch_direction)
                        ]
        mass_mole_h2o = .018
        ideal_gas_const = 8.3145
        velocity = (3*ideal_gas_const*temp_in_light /
                    mass_mole_h2o) ** .5  # m/sec
        m_sec_velocity = [velocity*polar_comp for polar_comp in launch_polar]
        return [
            m_sec_velocity[0], m_sec_velocity[1]*angle_per_m, m_sec_velocity[2]*angle_per_m]
