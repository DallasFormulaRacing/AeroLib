import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib
from typing import Final

class plot_functions:
        def __init__(self, file_path1: str) -> None:
                self.HEAVE_MIN: Final = -1.0
                self.HEAVE_MAX: Final = 1.0
                self.file_path1 = file_path1

                self.CHASSIS_ANGLE_MIN: Final = -1.8131 # having these hardcoded seems counterintuitive but I digress 
                self.CHASSIS_ANGLE_MAX: Final = 0.8076
                self.folder = "2024V3\\"
                self.num_angles = 36
                self.num_heaves = 36
                self.aeromap_df = pd.DataFrame(pd.read_csv(self.file_path1, delimiter=','))

        
        def clean_data(self) -> pd.DataFrame:
                threshold = 2
                df = pd.read_csv(self.file_path1) #converting a file into a dataframe

                for column in df.columns:
                        df.loc[df[column] == 0, column] = pd.NA

                df.dropna(inplace=True)

                return df
        
              
        def calculate_ride_height_combinations(self, j) -> float:
                heave_increment = (self.HEAVE_MAX + abs(self.HEAVE_MIN)) / (self.num_heaves - 1)
                angle_increment = (self.CHASSIS_ANGLE_MAX + abs(self.CHASSIS_ANGLE_MIN)) / (self.num_angles - 1)
        
                chassis_heave = np.round(-0.1429, 5)
                chassis_angle = np.round(self.CHASSIS_ANGLE_MIN + (j * angle_increment), 5)
                front_ride_height = 4.88 + (chassis_heave - 49.50) * np.sin(chassis_angle * (np.pi / 180))
                rear_ride_height = 5.55 + (chassis_heave + 46.04) * np.sin(chassis_angle * (np.pi / 180))

                return chassis_heave, chassis_angle, front_ride_height, rear_ride_height
        

        def calculate_min_max_mean(self) -> pd.DataFrame:
                df = self.aeromap_df
                selected_columns = df[['ClA', 'Raw Downforce']]
                
                # Calculate the minimum, maximum, and mean values using NumPy
                min_values = np.min(selected_columns, axis=0)
                max_values = np.max(selected_columns, axis=0)
                mean_values = np.mean(selected_columns, axis=0)

                raw_stats = pd.DataFrame({
                        'Minimum': min_values,
                        'Maximum': max_values,
                        'Mean': mean_values
                })

                raw_stats.to_csv("data/mean_max_min.csv", index=False)

                return raw_stats
        
        
        def compare_min_max_mean(self) -> dict:
                df = self.calculate_min_max_mean()
                minComp = df.loc['Raw Downforce', 'Minimum'] - df.loc['ClA', 'Minimum']
                meanComp = df.loc['Raw Downforce', 'Maximum'] - df.loc['ClA', 'Maximum']
                maxComp = df.loc['Raw Downforce', 'Mean'] - df.loc['ClA', 'Mean']
                compared = {
                        'Minimum': minComp,
                        'Maximum': maxComp,
                        'Mean': meanComp
                }
                return compared
        
        
        def plot_yaw_angle_vs_downforce(self) -> None:
                yaw_angle_vs_downforce = pd.DataFrame(columns=["Yaw Angle", "Downforce"])
                yaw_angle_increment = 5
                iteration = 0
                for i in range(0, 1):
                        for j in range(0, 65):
                                yaw_angle = np.round(j * yaw_angle_increment, 5)
                                yaw_angle_vs_downforce.loc[iteration, "Yaw Angle"] = yaw_angle
                                yaw_angle_vs_downforce.loc[iteration, "Downforce"] = self.aeromap_df.loc[j, "Raw Downforce"]
                                iteration += 1
                
                fig = px.scatter(yaw_angle_vs_downforce, x="Yaw Angle", y="Downforce")
                fig.show()
                yaw_angle_vs_downforce.to_csv("data/Yaw_Angle_vs_Downforce.csv", index=False)


        def plot_yaw_angle_vs_overturning_moment(self) -> None:
                yaw_angle_vs_downforce = pd.DataFrame(columns=["Yaw Angle", "Overturning Moment"])
                yaw_angle_increment = 5
                iteration = 0
                for i in range(0, 1):
                        for j in range(0, 1):
                                yaw_angle = np.round(j * yaw_angle_increment, 5)
                                yaw_angle_vs_downforce.loc[iteration, "Yaw Angle"] = yaw_angle
                                yaw_angle_vs_downforce.loc[iteration, "Overturning Moment"] = self.aeromap2_df.loc[j, "Overturning Moment"]
                                iteration += 1
                
                fig = px.scatter(yaw_angle_vs_downforce, x="Yaw Angle", y="Overturning Moment")
                fig.show()
                yaw_angle_vs_downforce.to_csv("data/Yaw_Angle_vs_Downforce.csv", index=False)
        

        def display_plot(self, data_path: str, x: list, y: str, to_file: bool = False) -> None:
                df = pd.DataFrame(pd.read_csv(data_path))
                fig = make_subplots()
                file_name = "data/"
                for i in x:
                        t = go.Scatter(
                                x=df[i],
                                y=df[y],
                                name=i + " vs " + y,
                                mode='markers'
                        )
                        fig.add_trace(t)
                        file_name = file_name + i + "_"
                fig.show()
                file_name = file_name.replace(" ", "_") + "vs_" + y + ".csv"
                if to_file:
                        df.to_csv(file_name, index=False)