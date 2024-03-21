from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from tool_code import NmapTool


class NmapToolkit(BaseToolkit, ABC):
    name: str = "Nmap Toolkit"
    description: str = "Toolkit contains all tools related to network scanning and security auditing using Nmap."

    def get_tools(self) -> List[BaseTool]:
        return [NmapTool()]

