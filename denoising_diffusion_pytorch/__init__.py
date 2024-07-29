from denoising_diffusion_pytorch.denoising_diffusion_pytorch import GaussianDiffusion, Unet, Trainer

from denoising_diffusion_pytorch.learned_gaussian_diffusion import LearnedGaussianDiffusion
from denoising_diffusion_pytorch.continuous_time_gaussian_diffusion import ContinuousTimeGaussianDiffusion
from denoising_diffusion_pytorch.weighted_objective_gaussian_diffusion import WeightedObjectiveGaussianDiffusion
from denoising_diffusion_pytorch.elucidated_diffusion import ElucidatedDiffusion
from denoising_diffusion_pytorch.v_param_continuous_time_gaussian_diffusion import VParamContinuousTimeGaussianDiffusion

from denoising_diffusion_pytorch.denoising_diffusion_pytorch_1d import GaussianDiffusion1D, Unet1D, Trainer1D, Dataset1D

from denoising_diffusion_pytorch.karras_unet import (
    KarrasUnet,
    InvSqrtDecayLRSched
)

from denoising_diffusion_pytorch.karras_unet_1d import KarrasUnet1D
from denoising_diffusion_pytorch.karras_unet_3d import KarrasUnet3D


###### note:
### Question:
# if a function is imported in the __init__.py, how should an exterior main function to call them?
### Answer:
# Let's assume the following project structure:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── main.py
# * my_package/__init__.py: Imports functions from module1.py.
# * my_package/module1.py: Contains the functions.
# * main.py: The external script that calls functions from my_package.
# Importing and Calling Functions
# Here's how to import and call functions from module1.py through __init__.py in your main.py script:
# Python
# # my_package/__init__.py
# from .module1 import function1, function2

# # my_package/module1.py
# def function1(arg1, arg2):
#     # Function logic
#     pass

# def function2(arg3):
#     # Function logic
#     pass

# # main.py
# import my_package

# def main():
#     result1 = my_package.function1(value1, value2)
#     result2 = my_package.function2(value3)

