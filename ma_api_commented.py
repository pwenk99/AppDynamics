import psutil
import requests
import json
import time

# Replace with the Machine Agent address for AppDynamics
APPDYNAMICS_MACHINE_AGENT_HOST = 'http://localhost:8293'

# Function to get CPU usage percentages
def get_cpu_usage():
    time.sleep(5)  # Wait for 5 seconds to let the CPU accumulate usage stats
    cpu_percentages = psutil.cpu_percent(interval=None, percpu=True)
    return cpu_percentages

# Function to generate metrics from CPU percentages
def generate_metrics(cpu_percentages):
    metrics = []
    for i, percentage in enumerate(cpu_percentages):
        metric = {
            "metricName": f"Custom Metrics|Hardware Resources|CPU|Usage|Core {i + 1}",
            "aggregatorType": "AVERAGE",
            "value": percentage
        }
        metrics.append(metric)
    return metrics

# Function to send generated metrics to AppDynamics
def send_to_appdynamics(metrics):
    headers = {"Content-Type": "application/json"}
    response = requests.post(f'{APPDYNAMICS_MACHINE_AGENT_HOST}/api/v1/metrics',
                             headers=headers,
                             json=metrics)
    print(f'Status code: {response.status_code}')
    print(f'Content: {response.content}')

# Continuously monitor CPU usage and send metrics to AppDynamics
while True:
    cpu_percentages = get_cpu_usage()      # Get CPU usage percentages
    metrics = generate_metrics(cpu_percentages)  # Generate metrics from percentages
    send_to_appdynamics(metrics)            # Send metrics to AppDynamics
    print(metrics)  # Print the metrics for debugging or logging purposes