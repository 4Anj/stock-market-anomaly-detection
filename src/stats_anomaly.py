def detect_statistical_anomaly(df, threshold=3):
    df["stat_anomaly"] = (df["daily_return"].abs() > threshold * df["volatility_20"])
    return df
