from enum import Enum
import numpy as np
from update_functions import *

initial_max_water_fascility_capacity = 0
initial_water = 0
initial_food = 0
initial_people = 0
initial_uranium = 0
initial_tharium = 0
initial_materials = 0

class ReqactorState(Enum):
    working = 0
    paused = 1
    on_hold = 3
    not_constructed = 4

class WaterFacility:
    def __init__(self):
        self.maxWater = initial_max_water_fascility_capacity
        self.water = initial_water

    def update(self):
        next_facility = WaterFacility
        next_facility.maxWater = self.maxWater
        next_facility.water = update_water()
        return next_facility


class Food:
    def __init__(self):
        self.food = initial_food

    def update(self):
        next_food = Food
        next_food.food = update_food()
        return next_food

class Population:
    def __init__(self):
        self.people = initial_people
    
    def update(self):
        next_population = Population
        next_population.people = update_people()
        return next_population

class Fuel:
    def __init__(self):
        self.uranium = initial_uranium
        self.tharium = initial_tharium
    
    def update(self):
        next_fuel = Fuel
        next_fuel.uranium = update_uranium()
        next_fuel.tharium = update_tharium
        return next_fuel

class ConstructionMaterials:
    def __init__(self):
        self.materials = initial_materials

    def update(self):
        next_materials = ConstructionMaterials
        next_materials.materials = update_materials()
        return next_materials

class Reactor:
    def __init__(self, number, state,  years_left):
        self.number = number
        self.state = state
        self.worker_years_left = years_left

    def construct(workers):
        worker_years_left -= workers

class PowerPlant:
    reactors = np.concatenate([Reactor(0, ReqactorState.working, None), Reactor(1, ReqactorState.working, None), Reactor(3, ReqactorState.on_hold, 3),
     Reactor(4, ReqactorState.on_hold, 4)], [Reactor(i, ReqactorState.working, None) for i in range(5, 13) ])



class State:    
    def __init__(self):
        self.water_facility = WaterFacility

