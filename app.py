import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# (1.0) Add page options for the overall app.
ui.page_opts(title="PyShiny App with plot", fillable=True)

# (2.0) Add a slider for specifying the number of bins in the histogram.
# (2.1) A string id ("selected_number_of_bins") that uniquely identifies this input value.

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
