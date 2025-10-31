import pandas as pd
import numpy as np

    # Series and DataFrames
s = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print(f"Simple Series :\n{s}\n")
data = {
    'City' : ['Mumbai', 'Delhi', 'Chennai', 'Kolkata'],
    'Population' : [20, 19, 11, 15], 
    'Area_sq_km' :
    [603, 1484, 426, 185]
}
df = pd.DataFrame(data)
print(f"Data Frame created from a dictionary :\n{df}\n")

    # Multilevel index series
index_tuples = [
    ('Group A', 'Item 1'),('Group A', 'Item 2'),
    ('Group B', 'Item 1'),('Group B', 'Item 2')
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Group', 'Item'])
multilevel_s = pd.Series([100, 200, 300, 400], index = multi_index)
print(f"Multi-level Index Series :\n{multilevel_s}\n")
print("Accessing data for 'Group A' :")
print(multilevel_s.loc['Group A'])
print("-"*40)
