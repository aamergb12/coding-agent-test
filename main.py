"""
Main entry point for the data science project.
Orchestrates the data analysis and visualization pipeline.
"""
import pandas as pd
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer
from utils import load_data, preprocess_data

def main():
    # Load and preprocess data
    raw_data = load_data('data/sample_data.csv')
    processed_data = preprocess_data(raw_data)
    
    # Initialize analyzer and visualizer
    analyzer = DataAnalyzer(processed_data)
    visualizer = DataVisualizer(processed_data)
    
    # Perform analysis
    summary_stats = analyzer.get_summary_statistics()
    correlations = analyzer.calculate_correlations()
    outliers = analyzer.detect_outliers()
    
    # Create visualizations
    visualizer.plot_distribution()
    visualizer.plot_correlation_heatmap(correlations)
    visualizer.plot_outliers(outliers)
    
    # Print analysis results
    print("Data Analysis Results:")
    print("=====================")
    print("\nSummary Statistics:")
    print(summary_stats)
    print("\nCorrelation Analysis:")
    print(correlations)
    print("\nOutliers detected:", len(outliers))

if __name__ == "__main__":
    main()