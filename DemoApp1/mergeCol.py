import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 5]})

# Creating the second dataframe
df2 = pd.DataFrame({'C': [8, 0], 'D': [9, 0]})

# Merging the two dataframes
merged_df = pd.concat([df1, df2], axis=1)

print("merged_df ","\n", merged_df)
# Grouping by the "C" column and keeping the other columns
grouped_df = merged_df.groupby('C', as_index=False).agg(lambda x: x.tolist())

# Displaying the grouped dataframe
print(grouped_df)
