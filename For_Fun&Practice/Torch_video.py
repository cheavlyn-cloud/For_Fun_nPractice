import torch
import numpy as np

class Screen:
    def __init__(self, resolution=(1920, 1080)):
        self.resolution = resolution
    def __repr__(self):
        return f"Screen {self.resolution}"

class Keyboard:
    def __init__(self, layout="QWERTY"):
        self.layout = layout
    def __repr__(self):
        return f"Keyboard layout: {self.layout}"

class CPU:
    def __init__(self, cores=4):
        self.cores = cores
    def compute(self, data):
        return np.mean(data)  # simple computation
    def __repr__(self):
        return f"CPU with {self.cores} cores"

class Laptop:
    def __init__(self, screen, keyboard, cpu):
        self.screen = screen
        self.keyboard = keyboard
        self.cpu = cpu
    def run_model(self):
        # Example Torch computation
        x = torch.tensor([1.0, 2.0, 3.0])
        return torch.nn.functional.softmax(x, dim=0)
    def __repr__(self):
        return f"Laptop({self.screen}, {self.keyboard}, {self.cpu})"

# "Build" the laptop
screen = Screen()
keyboard = Keyboard()
cpu = CPU(cores=8)
my_laptop = Laptop(screen, keyboard, cpu)

print(my_laptop)
print("CPU test:", cpu.compute([1, 2, 3, 4, 5]))
print("Torch model output:", my_laptop.run_model())