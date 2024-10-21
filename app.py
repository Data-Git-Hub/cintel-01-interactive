import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Define a unique ID for the slider and set the required label, min, max, and initial values
with ui.slidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19542312)
    # Generate random data
    x = 100 + 15 * np.random.randn(437)

    # Get the number of bins from the slider input
    number_of_bins = input.selected_number_of_bins()

    # Check if number_of_bins is 0 to avoid a 0/0 error, and set to 1 if it's 0
    if number_of_bins == 0:
        plt.text(0.5, 0.5, 'No bins selected, please choose a value greater than 0.', 
                 horizontalalignment='center', verticalalignment='center', 
                 transform=plt.gca().transAxes)
    else:
        # Create a histogram using the number of bins and normalize it
        plt.hist(x, bins=number_of_bins, density=True)
    
    # Display the chart
    plt.show()
