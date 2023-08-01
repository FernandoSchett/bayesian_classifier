import numpy as np
import pandas as pd

# Define the number of samples
num_samples = 100000

# Probabilities
prob_intruder_presence = [0.95, 0.05]
prob_sheep_presence = [0.70, 0.30]
prob_thunder = [0.90, 0.10]
prob_alarm = {
    (True, True, True): [0.05, 0.95],
    (True, True, False): [0.06, 0.94],
    (True, False, True): [0.07, 0.93],
    (True, False, False): [0.08, 0.92],
    (False, True, True): [0.20, 0.80],
    (False, True, False): [0.25, 0.75],
    (False, False, True): [0.40, 0.60],
    (False, False, False): [0.99, 0.01]
}
prob_farmer_wakeup = {
    True: [0.20, 0.80],
    False: [0.95, 0.05]
}
prob_orange_safety = {
    (False, True): [0.00, 1.00],
    (True, False): [1.00, 0.00],
    (True, True): [0.00, 1.00],
    (False, False): [0.00, 1.00]
}

# Generate samples
samples = {
    'IntruderPresence': np.random.choice([False, True], size=num_samples, p=prob_intruder_presence),
    'SheepPresence': np.random.choice([False, True], size=num_samples, p=prob_sheep_presence),
    'Thunder': np.random.choice([False, True], size=num_samples, p=prob_thunder)
}

samples['AlarmTriggered'] = [np.random.choice([False, True], p=prob_alarm[(samples['IntruderPresence'][i], samples['SheepPresence'][i], samples['Thunder'][i])]) for i in range(num_samples)]
samples['FarmerWakeUp'] = [np.random.choice([False, True], p=prob_farmer_wakeup[samples['AlarmTriggered'][i]]) for i in range(num_samples)]
samples['OrangeSafety'] = [np.random.choice([0, 1], p=prob_orange_safety[(samples['IntruderPresence'][i], samples['FarmerWakeUp'][i])]) for i in range(num_samples)]

# Convert to DataFrame
df = pd.DataFrame(samples)

# Save DataFrame to csv
df.to_csv('night_farm_dataset.csv', index=False)
