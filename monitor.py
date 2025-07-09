#!/usr/bin/env python3
import time
from system_metrics import SystemMetricsCollector
from alert_manager import AlertManager
from config import load_config

def main():
    # Load configuration
    config = load_config()
    
    # Initialize components
    metrics_collector = SystemMetricsCollector()
    alert_manager = AlertManager(
        smtp_host=config['smtp_host'],
        smtp_port=config['smtp_port'],
        smtp_username=config['smtp_username'],
        smtp_password=config['smtp_password']
    )
    
    print("Server monitoring system started...")
    
    while True:
        try:
            # Collect current metrics
            metrics = metrics_collector.collect_metrics()
            
            # Check thresholds and send alerts if needed
            if metrics['cpu_percent'] > config['cpu_threshold']:
                alert_manager.send_alert(
                    f"High CPU Usage Alert: {metrics['cpu_percent']}%"
                )
            
            if metrics['memory_percent'] > config['memory_threshold']:
                alert_manager.send_alert(
                    f"High Memory Usage Alert: {metrics['memory_percent']}%"
                )
            
            if metrics['disk_percent'] > config['disk_threshold']:
                alert_manager.send_alert(
                    f"High Disk Usage Alert: {metrics['disk_percent']}%"
                )
            
            # Wait for next check interval
            time.sleep(config['check_interval'])
            
        except Exception as e:
            print(f"Error in monitoring loop: {e}")
            time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    main()