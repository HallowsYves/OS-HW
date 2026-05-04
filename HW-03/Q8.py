import socket

def perform_dns_lookup():
    """Simulates a Domain Name System (DNS) lookup."""
    domain = input("Enter domain name: ")
    
    try:
        ip_address = socket.gethostbyname(domain)
        
        print("\n--- Lookup Results ---")
        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")
        
    except socket.gaierror:
        print("\n--- Lookup Results ---")
        print(f"Error: Unable to resolve IP address for '{domain}'. Invalid or unreachable domain.")

if __name__ == "__main__":
    perform_dns_lookup()