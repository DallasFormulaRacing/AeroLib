from handler import plot_functions

plotFunc = plot_functions(file_path1="data/aerodata.csv")

plotFunc.display_plot("data/aerodata.csv", ["Rear Rideheight", "Front Rideheight"], "ClA")