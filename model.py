
import numpy as np

# Sim-Defining Editable Variables

#planetary radius
#surface gravity
#surface temp stuff
#rate of sunlight rotation?
#location of stable regions (radius of poles?)
#number of molecules

# Setup (Pre-defined/Empty Variables, etc)

#escape velocity
#particles_active list
#particles_caught list
#time spent during hop
#photodissociation time scale

class Particle:

    def __init__(self):
        #polar coordinates: random

    def jump(self):
        #generate random direction
        #for now, fixed distance based on vars

    def is_caught(self):
        # return T/F depending on if in polar region


def first_spawn():
    #spawn num_particles particles


def projection(coordinate):
    #turn spherical coordinates into equidistant 2d projection
    #(maybe mercator projection eventually?? something funky with maps)


def update_model():
    #for particle in particles_active
        #particle.jump()
        #if particle.is_caught()
            #particles_caught.append(particle)
    #particles_active = all not is_caught

def main():
    #this will be in another file - going to animate with pygame :)


main()