import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from Task_1 import task1
from Task_2 import task2
from Task_3 import task3
task1()
task3()
task2()
# Define your functions

def calculate_cost(execution_time, cost_per_hour):
    return (execution_time / 3600) * cost_per_hour

def create_results_df(task_name, execution_time, cost_per_hour_vm1, cost_per_hour_vm2):
    total_cost_vm = calculate_cost(execution_time, cost_per_hour_vm1)
    return pd.DataFrame({
        'Task': [task_name],
        'Execution Time (s)': [execution_time],
        'Cost on VM ($)': [total_cost_vm]
    })

# Execution and reading data
task1_execution_time = pd.read_csv('cleaned_data_task1.csv').loc[0, 'Total Time']
task2_execution_time = pd.read_csv('cleaned_data_task2.csv').loc[0, 'Total Time']
task3_execution_time = pd.read_csv('cleaned_data_task3.csv').loc[0, 'Total Time']

# Cost calculation
cost_per_hour_vm1 = 0.20  # Small - 2 cores, 4GB RAM
cost_per_hour_vm2 = 0.84  # DS lab - 8 cores, 32GB RAM

results_df_task1 = create_results_df('Task 1', task1_execution_time, cost_per_hour_vm1, cost_per_hour_vm2)
results_df_task2 = create_results_df('Task 2', task2_execution_time, cost_per_hour_vm1, cost_per_hour_vm2)
results_df_task3 = create_results_df('Task 3', task3_execution_time, cost_per_hour_vm1, cost_per_hour_vm2)
#print(results_df_task1)
#print(results_df_task2)
#print(results_df_task3)

# Combine DataFrames
combined_results_df = pd.concat([results_df_task1, results_df_task2, results_df_task3])

# Melting DataFrame for plotting
melted_df = combined_results_df.melt(id_vars=['Task'], var_name='VM', value_name='Cost')

# Function to transform and plot each task's DataFrame


# Assuming you have DataFrames: results_df_task1, results_df_task2, results_df_task3




cost_vm1_task1 = results_df_task1['Cost on VM ($)'].iloc[0]
cost_vm1_task2 = results_df_task2['Cost on VM ($)'].iloc[0]
cost_vm1_task3 = results_df_task3['Cost on VM ($)'].iloc[0]
print(cost_vm1_task3)
combined_vm1_costs_df = pd.DataFrame({
    'Task': ['Task 1', 'Task 2', 'Task 3'],
    'Cost on VM1 ($)': [cost_vm1_task1, cost_vm1_task2, cost_vm1_task3]
})
melted_df_vm1 = combined_vm1_costs_df.melt(id_vars=['Task'], var_name='Cost on VM1 ($)', value_name='Cost')
print(melted_df_vm1)

plt.figure(figsize=(6, 4))
sns.barplot(x='Task', y='Cost', data=melted_df_vm1)
plt.title(f'Cost of vm1 on Different VMs')
plt.ylabel('Cost in $')
plt.xlabel('vm1')
plt.show()


cost_vm2_task1 = results_df_task1['Cost on VM ($)'].iloc[0]
cost_vm2_task2 = results_df_task2['Cost on VM ($)'].iloc[0]
cost_vm2_task3 = results_df_task3['Cost on VM ($)'].iloc[0]
print(cost_vm1_task3)
combined_vm2_costs_df = pd.DataFrame({
    'Task': ['Task 1', 'Task 2', 'Task 3'],
    'Cost on VM2 ($)': [cost_vm2_task1, cost_vm2_task2, cost_vm2_task3]
})
melted_df_vm2 = combined_vm2_costs_df.melt(id_vars=['Task'], var_name='Cost on VM2 ($)', value_name='Cost')
print(melted_df_vm2)

plt.figure(figsize=(6, 4))
sns.barplot(x='Task', y='Cost', data=melted_df_vm2)
plt.title(f'Cost of vm2 on Different VMs')
plt.ylabel('Cost in $')
plt.xlabel('vm2')
plt.show()

print(results_df_task1)


# Time for vm1
time_vm1_task1 = results_df_task1['Execution Time (s)'].iloc[0]
time_vm1_task2 = results_df_task2['Execution Time (s)'].iloc[0]
time_vm1_task3 = results_df_task3['Execution Time (s)'].iloc[0]

# Creating a DataFrame for the combined times
combined_vm1_time_df = pd.DataFrame({
    'Task': ['Task 1', 'Task 2', 'Task 3'],
    'Total Time (s)': [time_vm1_task1, time_vm1_task2, time_vm1_task3]
})

# Printing the DataFrame for verification
print(combined_vm1_time_df)

# Creating the bar plot
plt.figure(figsize=(6, 4))
sns.barplot(x='Task', y='Total Time (s)', data=combined_vm1_time_df)
plt.title('Execution Time of Tasks on VM1')
plt.ylabel('Time (seconds)')
plt.xlabel('Task')
plt.show()
