import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Rename columns
df_renamed = df.rename(columns={'A': 'Alpha', 'B': 'Beta'})

print(df_renamed)
