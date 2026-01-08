def detect_statistical_anomaly(df):
    threshold = 3 * df["daily_return"].std()

    df["anomaly"] = abs(df["daily_return"]) > threshold

    return df
