from fastapi import APIRouter
from pydantic import BaseModel
import yfinance as yf
import pandas as pd
from src.feature_eng import (
    compute_daily_return,
    compute_volatility,
    compute_volume_change,
    create_feature_matrix
)
from src.stats_anomaly import detect_statistical_anomaly
from src.ml_anomaly import detect_ml_anomaly

router = APIRouter(
    prefix="/anomaly",
    tags=["anomaly"]
)

class AnomalyRequest(BaseModel):
    ticker: str
    start: str
    end: str

@router.post("/")
def detect_anomalies(req: AnomalyRequest):
    # Load data
    df = yf.download(req.ticker, start="2022-01-01", end="2025-12-31")

    # flatten MultiIndex columns if needed
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # compute features BEFORE converting index
    df["daily_return"] = df["Close"].pct_change()

    # rolling volatility
    df["volatility_20"] = df["daily_return"].rolling(window=20).std()

    # volume change
    df["volume_change"] = df["Volume"].pct_change()

    # run statistical anomaly detection
    df = detect_statistical_anomaly(df)

    # run ML anomaly detection
    df = detect_ml_anomaly(df)

    # drop initial NaN rows safely
    df = df.dropna(subset=["daily_return", "volatility_20", "volume_change"], how="any")

    # extract anomaly dates BEFORE converting index
    statistical_dates = df[df["anomaly"] == True].index.strftime("%Y-%m-%d").tolist()
    ml_dates = df[df["iforest_anomaly"] == True].index.strftime("%Y-%m-%d").tolist()

    # convert index to string AFTER all calculations
    df.index = df.index.strftime("%Y-%m-%d")


    # --- RETURN RESPONSE PAYLOAD ---
    return {
    "dates": df.index.tolist(),
    "close": df["Close"].tolist(),
    "daily_return": df["daily_return"].tolist(),
    "volatility": df["volatility_20"].tolist(),
    "statistical_anomalies": statistical_dates,
    "ml_anomalies": ml_dates,
}

