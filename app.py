import matplotlib.pyplot as plt
import numpy as np
import panda as pd
from shiny.express import ui, input, render

with ui.slidebar():
  ui.input_slider("n", "N", 1, 100, 20)

@render.plot(alt="A histogram")
def histogram():
  np.random.seed(19542312)
  x = 100 + 15 * np.random.randn(437)
  plt.hist(x, input.n(), density=True)
  
