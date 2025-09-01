#!/usr/bin/env python3
from time import time
from rich.console import Console

console=Console()
def send_Msg(msg):
     if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
     else:
       print(msg)
class BaseMsg:
    def __init__(self,data:str):
        self._data=data
        
    @property
    def style (self):
        return'' #BaseMsg-specific
    
    @property
    def data (self):
        return self._data
    
    def __str__(self):
        return self._data  #BaseMsg-specific
    
    def __len__(self):
       return len(self._data)
    
    def __eq__(self,other):
        if isinstance(other ,BaseMsg):
            return self._data == other._data
        return False
    
    
    def __add__(self,other):
        if isinstance(other, BaseMsg):
            return BaseMsg(self._data + other._data)
        return BaseMsg(self._data + str (other))
    
class LogMsg(BaseMsg):
    def __init__(self,data):
        super().__init__(data)
        self._timestamps:int= 
        
class WarnMsg(LogMsg):
    #jhj



if __name__=="__main__":
  m1=BaseMsg('normal massage')
  m2 = LogMsg('Log')
  m3= WarnMsg('Warnning')
  send_Msg(m1)
  send_Msg(m2)
  send_Msg(m3)     
    
