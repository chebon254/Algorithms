import pandas as pd

# read xls sheet into pandas dataframe
df = pd.read_excel('invoice2.xlsx')

# identify and print out the repeating row data
duplicate_rows = df[df.duplicated(subset=['Article Document', 'Article Link'], keep=False)]
print("Repeating rows:\n", duplicate_rows)

# drop duplicates based on both columns "Document Article" and "Article Link"
df.drop_duplicates(subset=['Article Document', 'Article Link'], keep='first', inplace=True)

# save updated dataframe to a new xlsx sheet using openpyxl engine
df.to_excel('new_file.xlsx', engine='openpyxl', index=False)
