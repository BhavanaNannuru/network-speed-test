import speedtest as st

server = st.Speedtest()
server.get_best_server()

down = server.download() / 1000000
print(f"Download speed: {down:.2f} Mbps")

up = server.upload() / 1000000
print(f"Upload speed: {up:.2f} Mbps")

ping = server.results.ping
print(f"Ping: {ping:.2f} ms")