import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset():
    dataset_df1 = pd.read_csv(r"./Premonsoon/ground_water_quality_2018_pre.csv")
    dataset_df2 = pd.read_csv(r"./Premonsoon/ground_water_quality_2019_pre.csv")
    dataset_df3 = pd.read_csv(r"./Premonsoon/ground_water_quality_2020_pre .csv")
    dataset_df4 = pd.read_csv(r"./Premonsoon/ground_water_quality_2021_pre.csv")
    dataset_df5 = pd.read_csv(r"./Premonsoon/ground_water_quality_2022_pre.csv")
    dataset_df6 = pd.read_csv(r"./postmonsoon/ground_water_quality_2018_post.csv")
    dataset_df7 = pd.read_csv(r"./postmonsoon/ground_water_quality_2019_post.csv")
    dataset_df8 = pd.read_csv(r"./postmonsoon/ground_water_quality_2020_post.csv")
    dataset_df9 = pd.read_csv(r"./postmonsoon/ground_water_quality_2021_post.csv")
    dataset_df = pd.concat([dataset_df1,dataset_df2,dataset_df3,dataset_df4,dataset_df5,dataset_df6,dataset_df7,dataset_df8,dataset_df9],join='outer',ignore_index=True)
    dataset_df.drop(columns=['long_gis','lat_gis','sno','RL_GIS','sno','village','mandal','district','gwl','Classification.1','season'],inplace=True)

    dataset_df['pH'] = pd.to_numeric(dataset_df['pH'], errors='coerce')

    # Now convert to float
    dataset_df['pH'] = dataset_df['pH'].astype(float)
    dataset_df['RSC  meq  / L'] = pd.to_numeric(dataset_df['RSC  meq  / L'], errors='coerce')

    # Now convert to float
    dataset_df['RSC  meq  / L'] = dataset_df['RSC  meq  / L'].astype(float)

    temp = dataset_df['Classification'].copy()
    dataset_df['Classification'] = dataset_df['RSC  meq  / L']
    dataset_df['RSC  meq  / L'] = temp
    dataset_df = dataset_df.rename(columns={'Classification': 'RSC  meq  / L', 'RSC  meq  / L': 'Classification'})

    null_threshold = len(dataset_df) * 0.25
    for column in dataset_df.columns:
        null_count = dataset_df[column].isnull().sum()
        if null_count > null_threshold:
            dataset_df.drop(column, axis=1, inplace=True)
        elif null_count > 0:
            dataset_df.dropna(subset=[column], inplace=True)
    dataset_df.reset_index(drop=True, inplace=True)

    Classification_labels = []

    unique_labels = dataset_df['Classification'].unique()
    print(unique_labels)

    # Convert unique_labels to a set to remove duplicates and then back to a list
    Classification_labels = list(set(unique_labels))

    # Items to remove from the list
    items_to_remove = ['OG', 'BELOW THE GRAPH', 'O.G', 'OUT OF SAR GRAPH', 'BG']

    # Create a new list without the items to remove
    Classification_labels = [label for label in Classification_labels if label not in items_to_remove]

    # Filter dataset_df based on the updated Classification_labels
    dataset_df = dataset_df[dataset_df['Classification'].isin(Classification_labels)]

    dataset_df = dataset_df.reset_index(drop=True)
    print(dataset_df['Classification'].unique())
    print(dataset_df.info())
    return dataset_df