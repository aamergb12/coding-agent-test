"""
Main entry point for the customer behavior analysis project.
This module orchestrates the data loading, processing, and analysis pipeline.
"""
import pandas as pd
from data_processor import DataProcessor
from behavior_analyzer import CustomerBehaviorAnalyzer
from visualization import CustomerVisualizer

def main():
    # Initialize components
    data_processor = DataProcessor()
    analyzer = CustomerBehaviorAnalyzer()
    visualizer = CustomerVisualizer()
    
    # Load and process data
    raw_data = data_processor.load_data('customer_data.csv')
    processed_data = data_processor.preprocess_data(raw_data)
    
    # Perform analysis
    purchase_patterns = analyzer.analyze_purchase_patterns(processed_data)
    customer_segments = analyzer.perform_customer_segmentation(processed_data)
    loyalty_scores = analyzer.calculate_loyalty_scores(processed_data)
    
    # Create visualizations
    visualizer.plot_purchase_patterns(purchase_patterns)
    visualizer.plot_customer_segments(customer_segments)
    visualizer.plot_loyalty_distribution(loyalty_scores)
    
if __name__ == "__main__":
    main()