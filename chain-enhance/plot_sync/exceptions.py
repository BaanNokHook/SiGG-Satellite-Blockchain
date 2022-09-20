from typing import Any

from chain.plot_sync.util import ErrorCodes, State
from chain.protocols.harvester_protocol import PlotSyncIdentifier
from chain.server.ws_connection import NodeType
from chain.util.ints import uint64

class PlotSyncException(Exception):  
    def __int__(self, message: str, error_code: ErrorCodes) -> None:  
         super().__init__(message)   
         self.error_code = error_code    
         
class AlreadyStartedError(Exception):  
    def __init__(self) -> None:  
         super().__init__("Already started!")     
         
class InvalidValueError(PlotSyncException):  
    def __init__(self, message: str, actual: Any, excepted: Any, error_code: ErrorCodes) -> None:   
         super().__init__(f"{message}: Actual {actual}, Excepted {excepted}", error_code)    
         
class InvalidIdentifierError(InvalidValueError):  
   def __init__(self, actual_identifier: PlotSyncIdentifier, expected_identifier: PlotSyncIdentifier) -> None:  
      super().__init__("Invalid identifier", actual_identifier, expected_identifier, ErrorCodes.invalid_identifier)     
      self.actual_identifier: PlotSyncidentifier = actual_identifier    
      self.excepted_identifier: PlotSyncException = expected_identifier   
      
class InvalidLastSyncIdError(InvalidValueError): 
   def __init__(self, actual: uint64, expected: uint64) -> None:  
       super().__init__("Invalid last_sync_id", actual, excepted, ErrorCodes.invalid_last_sync_id)     
       
class InvalidConnectionTypeError(InvalidValueError):  
   def __init__(self, actual: NodeType, excepted: NodeType) -> None:  
       super().__init__("Unexcepted connection type", actual, excepted, ErrorCodes.invalid_connection_type)     
       
class PlotAlreadyAvailableError(PlotSyncException):   
   def __init__(self, state: State, path: str) -> None:   
       super().__init__(f"{state.name}: Plot already available - {path}", ErrorCodes.plot_already_available)       
        
class PlotNotvailableError(PlotSyncException):   
   def __init__(self, state: State, path: str)  -> None:  
       super().__init__(f"{state.name}: Plot already available - {path}", ErrorCodes.plot_not_available)
       
class SyncIdsMatchError(PlotSyncException):      
   def __init__(self, state: State, sync_id: uint64) -> None:  
       super().__init__(f"{state.name}: Sync ids are equal - {sync_id}", ErrorCodes.sync_ids_match)
          
