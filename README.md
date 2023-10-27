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

### Run

This project contains three main python files, and the one that should be run in order to view the simulation is **controller.py**. After being run, a pygame window should pop up on your machine, and the model will be run. After the model is complete, a message is sent to the terminal about the percentage of water molucules that were caught in the cold traps at the end of the simulation.

If you would want to change any of the starting conditions of the simulation, such as number of particles simulated or the time dilation factor, they are easily accessible at the top of the **model.py** file.

## Simulation

### Premise

This simulation is intended to represent the modeling of cold traps on Mercury, and the movement of H2O molecules across its surface, specifically with reference to how those molecules either:
- Get photodissociated by the sun or atmospheric conditions
- Become trapped in the polar regions at the north and south poles (cold traps) of the planet, where the temperature is not sufficient to provoke jumping

This simulation is primarily based on the '93 paper by Bryan J. Butler and Duane O. Muhleman called "Mercury: Full-Disk Radar Images and the Detection and Stability of Ice at the North Pole". Their work on this particular topic can be seen in their paper under the heading "Migration". I also incorporated some work from the follow-up '97 paper by Butler, "“The migration of volatiles on the surfaces of Mercury and the Moon.” 

My model uses the sunlight and temperature components of the '93 paper, but the random angle and height-based gravity components of the '97 paper. 

### Implementation

Upon being run, this code creates a window with the visualization for my model, with three different colors of molecule:
- Green molecules are active, and change size depending on how high off of the surface of the planet they are during their hop
- Blue molecules are caught, specifically in the cold traps at the north and south poles of the planet
- Orange molecules are lost, most commonly dissociated by the sun, but occasionally are lost because their initial launch led to their escaping the atmosphere of the planet.

![Screenshot from 2023-10-26 23-50-50](https://github.com/olincollege/scicomp-p2-water-you-up-to/assets/95325894/6e9a2e8c-3076-49cc-97ec-af52ef565626)

The yellow area on the visualization represents the current area of the planet that is facing the sun and so is enabled to hop by the temperature of the surface.

#### Weaknesses

This model abstracts away the idea that the velocities of the molecules would be randomly generated, and instead assumes constant initial velocity. This is partly due to the temperature of sunlit surface being abstracted to a flat 500K, which is very oversimplified.

### Results

The '93 and '97 papers found that the percentage of molecules that wound up trapped in in the polar cold traps hovers around 10-13%, which seems to be the ratio observed by data collection. 

The grand reveal: This is exactly the ratio I have found my model to return! 
