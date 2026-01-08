async function detectAnomalies() {
    const ticker = document.getElementById("ticker").value;

    document.getElementById("result").innerHTML = "Loading...";

    const response = await fetch("http://127.0.0.1:8000/anomaly/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            ticker: ticker.toUpperCase(),
            start: "2022-01-01",
            end: "2024-12-31"
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Results for ${ticker}</h3>
        <p>Statistical anomalies: ${data.statistical_anomalies.length}</p>
        <p>ML anomalies: ${data.ml_anomalies.length}</p>
    `;

    drawDashboardCharts(data);
}

async function plotChart(statAnom, mlAnom, ticker) {
    const priceData = await fetch(`https://api.polygon.io/v2/aggs/ticker/${ticker}/range/1/day/2022-01-01/2024-12-31?apiKey=YOUR_API_KEY`);
    const raw = await priceData.json();

    const dates = raw.results.map(item => new Date(item.t));
    const close = raw.results.map(item => item.c);

    // Plot
    const trace1 = {
        x: dates,
        y: close,
        type: "scatter",
        name: "Close Price"
    };

    const trace2 = {
        x: statAnom,
        y: statAnom.map(() => close[dates.indexOf(statAnom)]),
        mode: "markers",
        marker: { color: "red", size: 10 },
        name: "Statistical Anomaly"
    };

    const layout = {
        title: `Price Chart for ${ticker}`,
        showlegend: true
    };

    Plotly.newPlot("chart", [trace1], layout);
}

function drawDashboardCharts(data) {

    // --- PRICE LINE TRACE ---
    const priceTrace = {
        x: data.dates,
        y: data.close,
        type: "scatter",
        mode: "lines",
        name: "Close Price",
        line: { color: "blue" }
    };

    // --- SAFE STAT ANOMALY Y VALUES ---
    const statY = data.statistical_anomalies.map(d => {
        const idx = data.dates.indexOf(d);
        return idx !== -1 ? data.close[idx] : null;
    });

    const statAnomTrace = {
        x: data.statistical_anomalies,
        y: statY,
        mode: "markers",
        marker: { color: "red", size: 8 },
        name: "Statistical Anomaly"
    };

    // --- SAFE ML ANOMALY Y VALUES ---
    const mlY = data.ml_anomalies.map(d => {
        const idx = data.dates.indexOf(d);
        return idx !== -1 ? data.close[idx] : null;
    });

    const mlAnomTrace = {
        x: data.ml_anomalies,
        y: mlY,
        mode: "markers",
        marker: { color: "orange", size: 8 },
        name: "ML Anomaly"
    };

    // --- PLOT PRICE CHART ---
    Plotly.newPlot("priceChart", [priceTrace, statAnomTrace, mlAnomTrace], {
        title: "MSFT Price with Anomalies"
    });


    // --- VOLATILITY CHART ---
    Plotly.newPlot("volatilityChart", [{
        x: data.dates,
        y: data.volatility,
        type: "scatter",
        mode: "lines",
        name: "Volatility",
        line: { color: "purple" }
    }], {
        title: "20-Day Rolling Volatility"
    });


    // --- DAILY RETURNS HISTOGRAM ---
    Plotly.newPlot("returnsChart", [{
        x: data.daily_return,
        type: "histogram",
        name: "Daily Returns",
        marker: { color: "blue" }
    }], {
        title: "Distribution of Daily Returns",
        bargap: 0.05
    });
}