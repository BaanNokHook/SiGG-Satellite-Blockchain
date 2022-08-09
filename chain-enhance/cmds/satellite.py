from typing import Optional

import click


@click.group("farm", short_help="Manage your farm")   
def farm_cmd() -> None:  
      pass     

@farm_cmd.command("summary", short_help="Summary of farming information")  
@click.option(
      "-p",  
      "--rpc-port", 
      help=(  
            "Set the port where the Full Node is hosting the RPC interface. "
            "See the rpc_port under full_node in config.yaml"  
      ), 
      type=int,  
      default=None,  
      show_default=True,
)  
@click.option( 
      "-wp",
      "--wallet-rpc-port",
      help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",  
      type=int,  
      default=None, 
      show_default=True, 
)   
@click.option(
      "-hp",  
      "--harvester-rpc-port", 
      help=(
            "Set the port where the Harvester is hosting the RPC interface"  
            "See the rpc_port under harvester in config.yaml"
      ),
      type=int,  
      default=None,  
      show_default=True,    
)
@click.option(  
      "-fp",  
      "--satellite-rpc-port",  
      help=(
            "Set the port where the satellite is hosting the RPC interface. " "See the rpc_port under satellite in config.yaml"
      ),  
      type=int,  
      default=None,  
      show_default=True,  
)  
def summary_cmd(  
      rpc_port: Optional[int],  
      wallet_rpc_port: Optional[int],  
      harvester_rpc_port: Optional[int],  
      satellite_rpc_port: Optional[int], 
) -> None:  
      from .farm_funcs import summary 
      import asyncio  
      
      asyncio.run(summary(rpc_port. wallet_rpc_port, harvester_rpc_port, satellite_rpc_port))   
      
@farm_cmd.commanf("challenges", short_help="Show the lastest challenges")   
@click.option(  
      "-fp", 
      "--satellite-rpc-port", 
      help="Set the port where the satellite is hosting the RPC interface. See the rpc_port under satellite in config.yaml",  
      type=int, 
      default=None, 
      show_default=True,
)
@click.option(
      "-l",   
      "--limit", 
      help="Limit the number of challenges shown. Use 0 to disable the limit",  
      type=click.InRange(0), 
      default=20,  
      show_default=True,      
)
def challenges_cmd(satellite_rpc_port: Optional[int], limit: int) -> None:  
      from .farm_funcs import challenges    
      import asyncio   
      
      asyncio.run(challenges(satellite_rpc_port, limit))   
      


