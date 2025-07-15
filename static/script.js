document.getElementById("startBtn").addEventListener("click", function () {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "Running test... ⏳";

    fetch("/speedtest")
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                resultsDiv.innerHTML = `❌ Error: ${data.error}`;
            } else {
                resultsDiv.innerHTML = `
                    <p><strong>Download:</strong> ${data.download} Mbps</p>
                    <p><strong>Upload:</strong> ${data.upload} Mbps</p>
                    <p><strong>Ping:</strong> ${data.ping} ms</p>
                    <p><strong>Jitter:</strong> ${data.jitter} ms</p>
                    <p><strong>Packet Loss:</strong> ${data.packet_loss} %</p>
                    <p><strong>Server:</strong> ${data.best_server.location} (${data.best_server.sponsor})</p>
                `;
            }
        })
        .catch((error) => {
            resultsDiv.innerHTML = `❌ Error running test.`;
            console.error("Error:", error);
        });
});
