# Using the class
from nmap_scanner import NmapScanner, NmapTool

# if __name__ == "__main__":
#     host = '63.251.228.0/24'
#     port = '0-125'
#     arguments = '-p -A -T4'
#     scanner = NmapScanner(host, port, arguments)
#     scanner.scan_and_save('scan_results.csv')  # The results will be saved to a file

# 🛠️
# Tool Nmap Tool returned: Error1: NmapTool._execute() got an unexpected keyword argument 'hosts',
# TypeError, args: {'hosts': '63.251.228.0/24', 'port': '', 'arguments': ''}

args = "{'hosts': '127.0.0.1', 'port': '', 'arguments': ''}"
NmapTool()._execute(args)
