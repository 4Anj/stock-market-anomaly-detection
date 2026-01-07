from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_ml_anomaly(features, df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    iso = IsolationForest(
        contamination=0.01,
        random_state=42
    )
    preds = iso.fit_predict(scaled)

    preds_series = pd.Series(preds, index=features.index)
    df["ml_anomaly"] = False
    df.loc[features.index, "ml_anomaly"] = preds_series == -1

    return df
