from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.anomaly import router as anomaly_router

app = FastAPI(
    title="Stock Market Anomaly Detection API",
    description="Detect anomalies in stock price movements using statistical and ML methods.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anomaly_router)

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs for Swagger UI."}
