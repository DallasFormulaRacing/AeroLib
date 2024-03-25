import plotly.graph_objects as go
import pandas as pd
import handler as hd

aeromap_df = pd.DataFrame(pd.read_csv('./data/aerodata.csv', delimiter=','))

plot_funcs = hd.handler(aeromap_df)

z_vals = ['ClA', 'CdA', 'Raw Downforce Mean', 'Raw Drag Mean']

for val in z_vals:
    plot_funcs.make_plot_vs_front_rear_rideheight(val).show()