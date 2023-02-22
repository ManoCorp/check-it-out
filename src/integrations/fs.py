from .integration_interface import IntegrationInterface
from jinja2.environment import TemplateStream 
import io
import logging
import os 

class File(IntegrationInterface):
    @staticmethod
    def name() -> str:
        return "file"
    
    def __init__(self,  dest:str, key:str="", sender="", topic="") -> None:
        self.dest = dest
        self.key = key
        self.sender = sender
        self.topic = topic
        self.check()
    
    def check(self) -> bool:
        dir_path = os.path.dirname(os.path.realpath(self.dest))
        if os.path.exists(dir_path): # and os.access(self.dest, os.W_OK):
            return True
        raise PermissionError(f"Directory {dir_path} cannot be written to. Please check the path and permissions.")
    