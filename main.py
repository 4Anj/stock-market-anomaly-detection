from src.data_loader import load_stock_data
from src.feature_engineering import *
from src.statistical_anomaly import detect_statistical_anomaly
from src.ml_anomaly import detect_ml_anomaly

df = load_stock_data("MSFT", "2021-01-01", "2024-12-31")

df = compute_daily_return(df)
df = compute_volatility(df)
df = compute_volume_change(df)

features = create_feature_matrix(df)

df = detect_statistical_anomaly(df)
df = detect_ml_anomaly(features, df)

df.to_csv("data/processed/MSFT_anomaly_output.csv")

