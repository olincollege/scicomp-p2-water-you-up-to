# Project 2 for Scientific Computing: Fall 2023


## Running the Code
### Install

This project uses two external python libraries:

1. `numpy`
2. `pygame`

Install them via `pip`:

    ```bash
    pip install numpy pygame

Then clone this repo:

    ```bash
    git clone git@github.com:olincollege/scicomp-p2-water-hoppn.git

### Simulation

This project contains three main python files, and the one that should be run in order to view the simulation is **controller.py**. After being run, a pygame window should pop up on your machine, and the model will be run

If you would want to change any of the starting conditions of the simulation, such as number of particles simulated or the time dilation factor, they are easily accessible at the top of the **model.py** file.

## Premise

This simulation is intended to represent the modeling of cold traps on Mercury, and the movement of H2O molecules across its surface, specifically with reference to how those molecules either:
- Get photodissociated by the sun or atmospheric conditions
- Become trapped in the polar regions at the north and south poles (cold traps) of the planet, where the temperature is not sufficient to provoke jumping

This simulation is primarily based on the '93 paper by Bryan J. Butler and Duane O. Muhleman called "Mercury: Full-Disk Radar Images and the Detection and Stability of Ice at the North Pole". Their work on this particular topic can be seen in their paper under the heading "Migration". I also incorporated some work from the follow-up '97 paper by Butler, "“The migration of volatiles on the surfaces of Mercury and the Moon.” 

My model uses the sunlight and temperature components of the '93 paper, but the random angle and height-based gravity components of the '97 paper. 

## Results



