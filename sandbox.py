# %%

import numpy as np
import tomllib 
from box import Box

with open("config.toml", "rb") as f:
    config = Box(tomllib.load(f))
# %%
config
# %%
config.title
