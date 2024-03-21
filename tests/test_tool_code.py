# Using the class
from tool_code import NmapScanner

if __name__ == "__main__":
    host = '63.251.228.0/24'
    port = '0-125'
    arguments = '-p -A -T4'
    scanner = NmapScanner(host, port, arguments)
    scanner.scan_and_save('scan_results.csv')  # The results will be saved to a file
