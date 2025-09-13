

import pandas as pd

# Creating DataFrames from dictionaries

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'Salary': [50000, 60000, 70000]
# }

# data = [
#     {'Name': 'Alice', 'Age': 25, 'Salary': 50000},
#     {'Name': 'Bob', 'Age': 30, 'Salary': 60000},
#     {'Name': 'Charlie', 'Age': 35, 'Salary': 70000}
# ]
# df = pd.DataFrame(data)


df = pd.read_csv('people-100.csv')


# df_list = pd.read_html(
#     'https://planet4589.org/space/con/star/stats.html'
# )
# print(df_list[1])


# Data Exploration and Selection

# print(df.head(3))
# print(df.tail(3))
# print(df.describe())
# print(df.shape)
# print(df.columns)


# Label-based indexing with .loc
# print(df.loc[2, 'First Name'])
# print(df.loc[0:2, 'First Name':'Phone'])
# print(df.loc[
#     df['Index'] > 25, 'First Name'
# ])


# Position-based indexing with .iloc
# print(df.iloc[0, 2])
# print(df.iloc[:3, 1:3])

# Boolean indexing
# mask = (df['Index'] > 25) & (df['Index'] < 50)
# filtered_df = df[mask]
# print(filtered_df)
# print(df[(df['Index'] > 25) & (df['Index'] < 50)])


# Query method for complex filtering
# filtered_df = df.query('Index > 25 and Index < 50')
# print(filtered_df)
# print(df.query('Index > 25 and Index < 50'))


# Column Operations
df['Salary'] = 50000
df['Salary'] = df['Salary'] * 1.05
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

# Chanages are made in another copy of df
# df = df.drop(columns=['First Name', 'Last Name'])

# Changes are made in the same df
# df.drop(columns=['First Name', 'Last Name'], inplace=True)


# Sorting
# df_sorted = df.sort_values('Index', ascending=False)  # Single column

# Multiple columns
df_sorted = df.sort_values(
    ['First Name', 'Last Name'],
    ascending=[True, True]
)
# df_sorted = df_sorted.sort_index()


# URL: https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes
# print(df['Email'].dtype)
# df['Email'] = df['Email'].astype('string')
# print(df['Email'].dtype)


# df['Rolling_Mean'] = df['Index'].rolling(window=3).mean()
# df['Rolling_Median'] = df['Index'].rolling(window=3).median()
# print(df)


# Basic grouping
# print(df.groupby('Sex')['Salary'].mean())
# print(df.groupby(['Sex', 'Job Title'])['Salary'].mean())

# Concatenating DataFrames
# concatenated = pd.concat([df1, df2], ignore_index=True) # Vertically
# side_by_side = pd.concat([df1, df2], axis=1) # Horizontally


# print(df['Date of birth'].dtype)
df['Date of birth'] = pd.to_datetime(df['Date of birth'])
# print(df['Date of birth'].dtype)

# df['Date of birth'] = pd.to_datetime(df['Date of birth'], utc=True)


# https://en.wikipedia.org/wiki/ISO_8601
df['Date of birth'] = pd.to_datetime(df['Date of birth'], format='ISO8601')
# df['date'] = df['Date of birth'].dt.year

# print(df)

# Write
df.to_csv('out.csv', index=False)
