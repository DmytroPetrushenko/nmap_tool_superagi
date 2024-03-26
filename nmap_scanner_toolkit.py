from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool, ToolConfiguration
from typing import Type, List
from nmap_scanner import NmapTool


class NmapToolkit(BaseToolkit, ABC):
    name: str = "Nmap Toolkit"
    description: str = "A toolkit for scanning host IPs and ports, conducting security audits with Nmap."

    def get_tools(self) -> List[BaseTool]:
        return [NmapTool()]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            # Add more config keys specific to your project
        ]
