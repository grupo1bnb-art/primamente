window.addEventListener("load", () => {
    new TradingView.widget({
        "width": "100%",
        "height": "100%",
        "symbol": "FX:EURUSD",
        "interval": "1",
        "theme": "dark",
        "container_id": "tradingview_chart"
    });
});

function openTrade(type){
    const amount = document.getElementById("amount").value;
    const now = new Date().toLocaleTimeString();

    const row = `
        <tr>
            <td>${now}</td>
            <td>EUR/USD</td>
            <td>$${amount}</td>
            <td style="color:orange;">En curso...</td>
        </tr>
    `;

    document.getElementById("history-body").innerHTML += row;
}
