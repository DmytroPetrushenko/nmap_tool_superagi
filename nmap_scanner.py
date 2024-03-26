import nmap
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class NmapScanner:
    def __init__(self, host, ports, arguments):
        self.host: str = host
        self.ports: str = ports
        self.arguments: str = arguments
        self.scanner = nmap.PortScanner()

    def __scan(self):
        # If the arguments contain '-p', remove it (assuming '-p' should not be port-unspecified)
        args = self.arguments.replace('-p', '') if self.arguments and '-p' in self.arguments else self.arguments

        # Performing a scan
        self.scanner.scan(hosts=self.host, ports=self.ports if self.ports else None, arguments=args if args else "-sV")

    def scan_and_save(self, filename):
        try:
            self.__scan()

            # Saving the scan results to a file
            with open(filename, 'w') as file:
                file.write(self.scanner.csv())

            print(f"Results saved to {filename}")
            return True
        except Exception as e:
            print(f"Scan failed: {e}")
            return False

    def get_scan_results_as_csv(self):
        self.__scan()
        return self.scanner.csv()



class NmapInput(BaseModel):
    args: dict = Field(..., description="A dictionary containing keys 'hosts', 'port', and 'arguments' for configuring "
                                        "an Nmap scan. 'hosts' should contain IP addresses or domain names to be "
                                        "scanned. 'port' specifies a single port or a range of ports to be scanned. "
                                        "'arguments' allows for additional Nmap command-line arguments to customize "
                                        "the scan, such as specific port ranges, scan techniques, and the usage of "
                                        "scripts. This flexible structure enables a wide range of scanning scenarios, "
                                        "from simple host discovery to more complex service and vulnerability "
                                        "detection."
                       )


class NmapTool(BaseTool):
    """
    Nmap Tool
    """
    name: str = "Nmap Tool"
    args_schema: Type[BaseModel] = NmapInput
    description: str = "Utilizes Nmap for network scanning and security auditing."

    def _execute(self, args: dict):
        hosts = args['hosts']
        port = args['port']
        arguments = args['arguments']

        try:
            nmap_scanner = NmapScanner(hosts, port, arguments)
            result_csv = nmap_scanner.get_scan_results_as_csv()
            return result_csv
        except Exception as e:
            # Log the exception and consider returning a custom error message
            # depending on the nature of the exception for better user feedback
            return f"Error during scanning: {str(e)}"

