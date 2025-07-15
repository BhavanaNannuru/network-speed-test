from flask import Flask, jsonify, render_template
from flask_cors import CORS
import speedtest
import time
import statistics

try:
    from ping3 import ping
    ICMP_AVAILABLE = True
except ImportError:
    ICMP_AVAILABLE = False

import requests

app = Flask(__name__)
CORS(app)  # Allow frontend JS to call API


def calculate_jitter(ping_times):
    """Calculate jitter (variation in ping times)"""
    return statistics.stdev(ping_times) if len(ping_times) > 1 else 0


def measure_packet_loss_icmp(host="8.8.8.8", count=10, timeout=1):
    """Ping a host using ICMP and calculate packet loss"""
    lost_packets = 0
    for _ in range(count):
        response = ping(host, timeout=timeout)
        if response is None:
            lost_packets += 1
        time.sleep(0.2)
    loss_percentage = (lost_packets / count) * 100
    return loss_percentage


def measure_packet_loss_http(url="https://www.google.com", count=10, timeout=2):
    """Send HTTP requests and calculate packet loss"""
    lost_packets = 0
    for _ in range(count):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code != 200:
                lost_packets += 1
        except requests.RequestException:
            lost_packets += 1
        time.sleep(0.2)
    loss_percentage = (lost_packets / count) * 100
    return loss_percentage


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/speedtest')
def perform_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_servers()
        best_server = st.get_best_server()

        # Measure ping times for jitter calculation
        ping_times = []
        for _ in range(5):  # Reduced ping count for speed
            ping_times.append(st.results.ping)
            time.sleep(0.1)
        avg_ping = sum(ping_times) / len(ping_times)
        jitter = calculate_jitter(ping_times)

        # Measure packet loss
        print("Measuring packet loss...")
        if ICMP_AVAILABLE:
            packet_loss = measure_packet_loss_icmp()
        else:
            packet_loss = measure_packet_loss_http()

        # Measure download and upload
        print("Measuring download speed...")
        download_speed = st.download()
        print("Measuring upload speed...")
        upload_speed = st.upload()

        # Convert speeds from bits/sec to Mbps
        download_mbps = download_speed / 1_000_000
        upload_mbps = upload_speed / 1_000_000

        return jsonify({
            "best_server": {
                "host": best_server['host'],
                "location": f"{best_server['name']}, {best_server['country']}",
                "sponsor": best_server['sponsor'],
                "latency": round(best_server['latency'], 2)
            },
            "download": round(download_mbps, 2),
            "upload": round(upload_mbps, 2),
            "ping": round(avg_ping, 2),
            "jitter": round(jitter, 2),
            "packet_loss": round(packet_loss, 2),
            "method": "ICMP" if ICMP_AVAILABLE else "HTTP fallback"
        })

    except Exception as e:
        print("Error during speed test:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
