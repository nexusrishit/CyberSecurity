from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to analyze and display packet information
def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet Captured: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        # Check if it's a TCP, UDP, or ICMP packet
        if packet.haslayer(TCP):
            print("Protocol: TCP")
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
            print(f"Type: {packet[ICMP].type}")
        
        # Payload data (if present)
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload)
            if payload:
                print(f"Payload Data: {payload}")
            else:
                print("No payload data.")
    else:
        print("Non-IP packet captured, ignoring...")

# Function to start sniffing packets
def start_sniffer(interface):
    print(f"[*] Starting packet sniffer on {interface}...")
    sniff(iface=interface, prn=analyze_packet, store=False)

# Main program
if __name__ == "__main__":
    interface = input("Enter the network interface to sniff (e.g., eth0 or wlan0): ")
    start_sniffer(interface)
