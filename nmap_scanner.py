import nmap
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class NmapScanner:
    def __init__(self, host, ports, arguments):
        self.host: str = host
        self.ports: str = ports if ports != "" else None
        self.arguments: str = arguments if arguments != "" else None
        self.scanner = nmap.PortScanner()

    def scan_and_save(self, filename):
        # Launch scanning
        try:
            if self.arguments is not None and '-p' in self.arguments:
                self.arguments = self.arguments.replace('-p', '')

            if self.ports is None and self.arguments is None:
                self.scanner.scan(hosts=self.host)
            elif self.ports is None:
                self.scanner.scan(hosts=self.host, arguments=self.arguments)
            elif self.arguments is None:
                self.scanner.scan(hosts=self.host, ports=self.ports)
            else:
                self.scanner.scan(hosts=self.host, ports=self.ports, arguments=self.arguments)

            # Get the result in CSV format
            scan_results = self.scanner.csv()
            # Save the result to a file
            with open(filename, 'w') as file:
                file.write(scan_results)
            print(f"Results saved to {filename}")
            return True
        except Exception as e:
            print(f"Scan failed: {e}")
            return False


class NmapInput(BaseModel):
    hosts: str = Field(..., description="IP addresses or domain names to be scanned")
    port: str = Field(..., description="Port or range of ports to be scanned")
    arguments: str = Field(..., description="Additional nmap command-line arguments for scanning, such as port "
                                            "ranges, scan techniques, and script usage")


class NmapTool(BaseTool):
    """
    Nmap Tool
    """
    name: str = "Nmap Tool"
    args_schema: Type[BaseModel] = NmapInput
    description: str = "Utilizes Nmap for network scanning and security auditing."

    def _execute(self, args: dict, filename='scan_results.csv'):
        hosts = args['hosts']
        port = args['port']
        arguments = args['arguments']

        nmap_scanner = NmapScanner(hosts, port, arguments)

        if nmap_scanner.scan_and_save(filename):
            return f"Scan finished. Results are saved in {filename}."
        else:
            return "Scan failed. Check the logs for errors."
