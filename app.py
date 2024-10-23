import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# (1.0) Add page options for the overall app.
ui.page_opts(title="PyShiny App with plot", fillable=True)

# (2.0) Add a slider for specifying the number of bins in the histogram.
# (2.1) A string id ("selected_number_of_bins") that uniquely identifies this input value.
# (2.2) A string label (e.g., "Number of Bins") to be displayed alongside the slider.
# (2.3) An integer representing the minimum number of bins (e.g., 0).
# (2.4) An integer representing the maximum number of bins (e.g., 1000).
# (2.5) An integer representing the initial value of the slider at the halfway point (e.g., 500).
# (3.0) Added variable names.

min_num = 0
max_num = 1000
halfway_point = (min_num + max_num) / 2

with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins", "Number of Bins", min_num, max_num, halfway_point
    )


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
