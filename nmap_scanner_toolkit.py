from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool, ToolConfiguration
from typing import Type, List
from nmap_scanner import NmapTool


class NmapToolkit(BaseToolkit, ABC):
    name: str = "Nmap Toolkit"
    description: str = "Toolkit contains all tools related to network scanning and security auditing using Nmap."

    def get_tools(self) -> List[BaseTool]:
        return [NmapTool()]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            # Add more config keys specific to your project
        ]
