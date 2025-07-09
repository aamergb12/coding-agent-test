import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_customer_data(file_path):
    """
    Load customer data from various file formats (CSV, Excel, etc.)
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def clean_customer_data(df):
    """
    Clean customer dataset by handling missing values, outliers, and data type conversions
    """
    # Handle missing values
    df = df.fillna({
        'age': df['age'].median(),
        'income': df['income'].median(),
        'purchase_amount': 0,
    })
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert categorical variables
    le = LabelEncoder()
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = le.fit_transform(df[col])
    
    return df

def feature_engineering(df):
    """
    Create new features from existing customer data
    """
    # Calculate customer lifetime value
    df['customer_lifetime_value'] = df['purchase_amount'] * df['purchase_frequency']
    
    # Create customer segments based on recency, frequency, monetary value
    df['recency_score'] = pd.qcut(df['days_since_last_purchase'], q=5, labels=[1, 2, 3, 4, 5])
    df['frequency_score'] = pd.qcut(df['purchase_frequency'], q=5, labels=[1, 2, 3, 4, 5])
    df['monetary_score'] = pd.qcut(df['purchase_amount'], q=5, labels=[1, 2, 3, 4, 5])
    
    # Normalize numerical features
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    return df