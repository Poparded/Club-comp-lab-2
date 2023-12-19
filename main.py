import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from Task_1 import task1
from Task_2 import task2
from Task_3 import task3
#task1()
task3()
task2()


df_task1 = pd.read_csv('cleaned_data_task1.csv')
df_task2 = pd.read_csv('cleaned_data_task2.csv')

df_task3 = pd.read_csv('cleaned_data_task3.csv')

#print(df_task1)

print(df_task2)

#print(df_task3)

#Small - 2 cores, 4GB RAM
cost_per_hour_vm1 = 0.20
#DS lab - 8 cores, 32GB RAM
cost_per_hour_vm2 = 0.84
#Formula for small vm
#total_cost_vm1 = (execution_time_vm1 / 3600) * cost_per_hour_vm1
#Formula for large vm
#total_cost_vm2 = (execution_time_vm2 / 3600) * cost_per_hour_vm2
