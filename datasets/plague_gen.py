import pandas as pd
import numpy as np
import random

# Set a random seed for reproducibility
np.random.seed(50)

# Number of data samples in the dataset
num_samples = 10000

# Generate the data for each variable
data = {
    'Symptoms': np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5]),
    'Pesticides': np.random.choice([0, 1], size=num_samples, p=[0.5, 0.5]),
    'Rainfall': np.random.uniform(0, 200, num_samples),
    'Soil Moisture': np.random.uniform(0, 100, num_samples),
    'Temperature': np.random.uniform(10, 40, num_samples),
    'Management Practices': np.random.choice(['Conventional', 'Organic'], size=num_samples, p=[0.5, 0.5])
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Create 'Infestation' column
# Let's say that infestation is more likely when there are Symptoms,
# when Pesticides are not used, when Rainfall and Soil Moisture are high,
# when Temperature is in the range 20-30, and when Management Practices are 'Organic'.
df['Infestation'] = (
    df['Symptoms'] 
    & (~df['Pesticides']) 
    & (df['Rainfall'] > df['Rainfall'].median())
    & (df['Soil Moisture'] > df['Soil Moisture'].median()) 
    & ((df['Temperature'] > 20) & (df['Temperature'] < 30))
    & (df['Management Practices'] == 'Organic')
).astype(int)

# Save the dataset to a CSV file
df.to_csv('plague_farm_dataset.csv', index=False)
