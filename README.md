# 📡 Network Speed Test App

A simple Python application to measure your network’s download speed, upload speed, and ping latency using the `speedtest` module. This CLI-based tool selects the best available test server and returns accurate results in Mbps and milliseconds.

---

## 🚀 Features
- Automatically selects the best test server based on latency.
- Measures:
  - **Download Speed** (Mbps)
  - **Upload Speed** (Mbps)
  - **Ping** (ms)
- Clean and minimal command-line interface.

---

## 🛠 How It Works
- Uses the **Speedtest.net API** to perform speed tests.
- Downloads and uploads random data chunks to/from the closest server.
- Calculates speeds in Megabits per second (Mbps).

---



## 🔮 Future Enhancements (in progress)
- [x] Display test server details (city, country, sponsor) for more transparency.  
- [x] Add jitter and packet loss measurements to improve network diagnostics.  
- [ ] Implement robust error handling with automatic retries on failure.  
- [ ] Include real-time progress indicators for download and upload operations.  
- [ ] Develop GUI versions:  
  - [ ] PyQt for a professional desktop interface.  
  - [ ] Kivy for cross-platform mobile support (Android/iOS).  
- [ ] Build a REST API backend using Flask or FastAPI to expose the speed test as a service.  
- [ ] Integrate a logging system to save test results locally and in JSON format for analytics.  
- [ ] Visualize speed fluctuations with interactive graphs and charts.  
- [ ] Add multi-threaded test execution to simulate real-world conditions more effectively.  
- [ ] Create a modern Text-based UI (TUI) using Rich or Textual for terminal users.  

---

## 📖 Requirements
- Python 3.7+
- `speedtest` Python module

---

---
## ⚠️ Disclaimer

This project is intended for educational and personal use only. The speed test results are approximate and may vary depending on network conditions and server availability. The author is not responsible for any issues, damages, or inaccuracies arising from the use of this application. Use at your own discretion.

