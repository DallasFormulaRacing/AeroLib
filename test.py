from handler import plot_functions
import pandas as pd

plotFunc = plot_functions(file_path1="data/aerodata.csv")

plotFunc.display_plot("data/aerodata.csv", ["Rear Rideheight", "Front Rideheight"], "ClA",)