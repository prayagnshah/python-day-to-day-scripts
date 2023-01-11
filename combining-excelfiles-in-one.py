import os 
import pandas as pd

# Absolute path name where all the excel files are stored 
folder_path_name = r'D:\bats\test'

# Empty list 
df = []

# Reading the contents of the directory and iterating them and reading excel files using the pandas function 
for file in os.listdir(folder_path_name):
    if file.endswith('.csv'):
        print("Loading files {0}".format(file))
        df.append(pd.read_csv(os.path.join(folder_path_name, file)))

# merging all the excel files into the final result
df_final_result = pd.concat(df)
df_final_result.to_csv('combined-files.csv', index= False)

##Files will be saved in the directory where you run this program    

        