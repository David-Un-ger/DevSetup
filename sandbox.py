# %%

import numpy as np
import toml#lib 
from box import Box
import torch
import pathlib

path = pathlib.Path("config.toml")
config = pathlib.Path.read_text(path)
config = Box(toml.loads(config))
# %%
print("Cuda available: ", torch.cuda.is_available())