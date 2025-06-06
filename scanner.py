import socket
import ipaddress
import argparse

# Common ports to scan (you can expand this list)
COMMON_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP",
    21: "FTP",
    25: "SMTP"
}

def scan_host(ip):
    open_ports = []
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((str(ip), port))
            if result == 0:
                open_ports.append(port)
        except Exception as e:
            pass
        finally:
            sock.close()
    return open_ports

def main(network):
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        print(f"Invalid network: {e}")
        return
    
    print(f"Scanning network: {network}")
    for ip in net.hosts():
        open_ports = scan_host(ip)
        if open_ports:
            print(f"[!] {ip} has open ports:")
            for port in open_ports:
                print(f"    - Port {port} ({COMMON_PORTS[port]})")
    print("Scan complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Network Vulnerability Scanner")
    parser.add_argument('--target', type=str, required=True, help="Target network (e.g., 192.168.1.0/24)")
    args = parser.parse_args()
    main(args.target)