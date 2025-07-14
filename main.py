import speedtest
import socket
import time
import statistics

def calculate_jitter(ping_times):
    """Calculate jitter (variation in ping times)"""
    return statistics.stdev(ping_times) if len(ping_times) > 1 else 0

def measure_packet_loss(host="8.8.8.8", count=10, timeout=1):
    """Ping a host and calculate packet loss"""
    lost_packets = 0
    for _ in range(count):
        try:
            start = time.time()
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 80))
            s.close()
            end = time.time()
        except socket.error:
            lost_packets += 1
        time.sleep(0.2)  # slight delay between pings
    loss_percentage = (lost_packets / count) * 100
    return loss_percentage

def perform_speed_test():
    print(" Initializing Speed Test...")
    try:
        st = speedtest.Speedtest()
        st.get_servers()
        best_server = st.get_best_server()
        
        print(f"\n Best server found:")
        print(f"   Host: {best_server['host']}")
        print(f"   Location: {best_server['name']}, {best_server['country']}")
        print(f"   Sponsor: {best_server['sponsor']}")
        print(f"   Latency: {best_server['latency']:.2f} ms\n")
        
        # Measure ping times for jitter calculation
        ping_times = []
        print(" Measuring ping and jitter...")
        for _ in range(10):
            st.get_best_server()
            ping_times.append(st.results.ping)
            time.sleep(0.1)
        avg_ping = sum(ping_times) / len(ping_times)
        jitter = calculate_jitter(ping_times)
        
        # Measure packet loss
        print(" Measuring packet loss...")
        packet_loss = measure_packet_loss()
        
        # Measure download and upload
        print(" Measuring download speed...")
        download_speed = st.download()
        print(" Measuring upload speed...")
        upload_speed = st.upload()
        
        # Convert speeds from bits/sec to Mbps
        download_mbps = download_speed / 1_000_000
        upload_mbps = upload_speed / 1_000_000
        
        # Display results
        print("\n Speed Test Results:")
        print(f"   Download Speed: {download_mbps:.2f} Mbps")
        print(f"   Upload Speed:   {upload_mbps:.2f} Mbps")
        print(f"   Ping:           {avg_ping:.2f} ms")
        print(f"   Jitter:         {jitter:.2f} ms")
        print(f"   Packet Loss:    {packet_loss:.2f} %\n")
    
    except Exception as e:
        print(" Error during speed test:", e)

if __name__ == "__main__":
    perform_speed_test()
