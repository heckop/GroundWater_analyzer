import pandas as pd
import numpy as np


dataset_df = pd.read_csv(r"./ground_water_quality_2018_post.csv")

dataset = dataset_df.values

print(dataset[373][2])