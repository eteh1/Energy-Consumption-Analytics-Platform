import sqlite3
import random
import pandas as pd
import matplotlib.pyplot as plt
import schedule
import time
from datetime import datetime, timedelta

# 1. Data Ingestion (Simulated)
def collect_energy_data():
    # Simulate data collection from various devices/sensors
    regions = ['North', 'South', 'East', 'West']
    devices = ['AC', 'Heater', 'Lights', 'Washing Machine']
    data = []
    
    for region in regions:
        for device in devices:
            energy_usage = random.randint(50, 500)  # Random usage in kWh
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data.append((timestamp, region, device, energy_usage))
    
    return data

# 2. Data Processing (Cleaning and Transformation)
def process_data(data):
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'region', 'device', 'energy_usage'])
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Filter out invalid readings (e.g., energy_usage < 0)
    df = df[df['energy_usage'] > 0]
    
    return df

# 3. Data Storage (SQLite Database)
def store_data(df):
    conn = sqlite3.connect('energy_consumption.db')
    df.to_sql('energy_data', conn, if_exists='append', index=False)
    conn.close()
    print(f"Stored {len(df)} rows of data to database.")

# 4. Data Analysis (Consumption Metrics)
def analyze_data():
    conn = sqlite3.connect('energy_consumption.db')
    df = pd.read_sql('SELECT * FROM energy_data', conn)
    
    # Aggregating energy usage by region and device
    analysis = df.groupby(['region', 'device'])['energy_usage'].agg(['sum', 'mean', 'max', 'min']).reset_index()
    
    print("Energy Consumption Analysis:")
    print(analysis)
    
    # Plotting the total energy consumption by region
    region_consumption = df.groupby('region')['energy_usage'].sum()
    region_consumption.plot(kind='bar', title="Total Energy Consumption by Region", ylabel="Energy Usage (kWh)")
    plt.show()
    
    conn.close()

# 5. Orchestration and Monitoring
def job():
    print(f"Job started at {datetime.now()}")
    
    # Step 1: Collect energy data
    data = collect_energy_data()
    
    # Step 2: Process data
    processed_data = process_data(data)
    
    # Step 3: Store data
    store_data(processed_data)
    
    # Step 4: Analyze data
    analyze_data()
    
    print(f"Job completed at {datetime.now()}")

# Scheduling the pipeline to run every hour
schedule.every(1).hour.do(job)

# Run the orchestration indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
