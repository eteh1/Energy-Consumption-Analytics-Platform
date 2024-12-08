# Energy Consumption Monitoring System

This project monitors energy consumption across different regions and devices, simulating data collection, processing it, storing it in a database, and performing analysis with visualization.

## Features
1. **Data Ingestion**: Simulates data collection from energy-consuming devices.
2. **Data Processing**: Cleans and filters the data for validity.
3. **Data Storage**: Stores the processed data in an SQLite database.
4. **Data Analysis**: Provides insights into energy consumption trends with visualizations.
5. **Scheduling**: Automates data ingestion and analysis to run hourly.

## Technologies Used
- **Python**: Core programming language.
- **SQLite**: Database for storing energy data.
- **Pandas**: Data analysis and manipulation.
- **Matplotlib**: Visualization of energy usage trends.
- **Schedule**: For job orchestration.

## Prerequisites
- Python 3.7 or higher installed.
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `schedule`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
