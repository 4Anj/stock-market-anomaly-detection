from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_ml_anomaly(df):
    features = df[["daily_return", "volatility_20", "volume_change"]].dropna()

    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    iso = IsolationForest(contamination=0.01, random_state=42)
    preds = iso.fit_predict(scaled)

    # Create full column with default False
    df["iforest_anomaly"] = False

    # Assign ML anomalies only to the rows used
    df.loc[features.index, "iforest_anomaly"] = preds == -1

    return df
