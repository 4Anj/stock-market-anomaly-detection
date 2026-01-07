import pandas as pd

def compute_daily_return(df):
    df["daily_return"] = df["Close"].pct_change()
    return df

def compute_volatility(df, window=20):
    df["volatility_20"] = df["daily_return"].rolling(window).std()
    return df

def compute_volume_change(df):
    df["volume_change"] = df["Volume"].pct_change()
    return df

def create_feature_matrix(df):
    features = df[["daily_return", "volatility_20", "volume_change"]].dropna()
    return features

