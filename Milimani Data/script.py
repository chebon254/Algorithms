import pandas as pd

# Load the data from the excel sheet into a pandas DataFrame
df = pd.read_excel("KUZA Registration Data.xlsx")

# Remove duplicates based on columns A, B, and C
df = df.drop_duplicates(subset=["2. Phone Number", "3. Are you born again?", "4. Do you prefer a physical or online meeting", "5. Which day do you prefer", "6. What time do you prefer?"])

# print(df.columns)

# Sort the data based on columns F, E, and G
df = df.sort_values(by=["5. Which day do you prefer", "4. Do you prefer a physical or online meeting", "6. What time do you prefer?"])

# Write the arranged data back to the excel sheet
df.to_excel("KUZA Registration Data(Ordered).xlsx", index=False)
