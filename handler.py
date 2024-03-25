import plotly.graph_objects as go
import pandas as pd


class handler:
    def __init__(self, data: pd.DataFrame):
        self.data_frame = data

    def make_plot_vs_front_rear_rideheight(self, z: str):
        print(z)
        fig = go.Figure(
            data =
            go.Contour(
                z=self.data_frame.get(z),
                x=self.data_frame.get('Front Rideheight'),
                y=self.data_frame.get('Rear Rideheight'),
                colorscale="balance",
                colorbar=dict(
                    title=f"{z}",
                    titlefont=dict(size=20),
                    titleside='right'
                )
            ),
        )
        fig.update_layout(
            title=dict(
                text=f"Ride Height (Front & Rear) vs {z}",
                font=dict(size=24), 
                x=0.5
            )
        )
        
        fig.update_xaxes(
            title_text="Front Ride Height (in)"
        )
        
        fig.update_yaxes(
            title_text="Rear Ride Height (in)"
        )

        return fig