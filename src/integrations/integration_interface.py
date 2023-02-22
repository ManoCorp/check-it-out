import io

class IntegrationInterface:
    @staticmethod
    def name() -> str:
        pass
    
    def save(self, data:io.BufferedReader):
        pass
    def __init__(self, dest:str, key:str="", sender="", topic="") -> None:
        pass
    def check(self):
        pass
    
