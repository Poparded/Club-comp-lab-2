import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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
def plot_task_cost(df, task_name):
    # Transform the DataFrame
    df_plot = df.melt(id_vars=['Task'], value_vars=['Cost on VM1 ($)', 'Cost on VM2 ($)'],
                      var_name='VM', value_name='Cost')
    df_plot['VM'] = df_plot['VM'].str.replace('Cost on ', '')
    #print(df_plot)

    # Plotting
    plt.figure(figsize=(6, 4))
    sns.barplot(x='VM', y='Cost', data=df_plot)
    plt.title(f'Cost of {task_name} on Different VMs')
    plt.ylabel('Cost in $')
    plt.xlabel('VM')
    plt.show()

# Assuming you have DataFrames: results_df_task1, results_df_task2, results_df_task3

# Plot for Task 1
plot_task_cost(results_df_task1, 'Task 1')

# Plot for Task 2
plot_task_cost(results_df_task2, 'Task 2')

# Plot for Task 3
plot_task_cost(results_df_task3, 'Task 3')



cost_vm1_task1 = results_df_task1['Cost on VM1 ($)'].iloc[0]
cost_vm1_task2 = results_df_task2['Cost on Vm1 ($)'].iloc[0]
cost_vm1_task3 = results_df_task3['Cost on VM1 ($)'].iloc[0]
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


cost_vm2_task1 = results_df_task1['Cost on VM2 ($)'].iloc[0]
cost_vm2_task2 = results_df_task2['Cost on VM2 ($)'].iloc[0]
cost_vm2_task3 = results_df_task3['Cost on VM2 ($)'].iloc[0]
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