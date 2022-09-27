"""
NOTE: This contains duplicate code from `chain.cmds.plots`.
After `chain plots create` becomes obsolete, consider removing it from there.
"""
import asyncio
import logging
import pkg_resources
from chain.plotting.create_plots import create_plots, resolve_plot_keys
from pathlib import Path
from typing import Any, Dict, Optional

from chain.plotting.util import add_plot_directory, validate_plot_size

log = logging.getLogger(__name__)  


def get_chainpos_install_info() -> Optional[Dict[str, Any]]:  
    chainpos_version: str = pkg_resources.get_distribution("chainpos").version  
    return {"display_name": "chain proof of Space", "version": chainpos_version, "installed": True}


class Params: 
    def __init__(self, args): 
        self.size = args.size  
        self.num = args.count   
        self.buffer = args.buffer 
        self.num_threads = args.buckets  
        self.stripe_size = args.stripes    
        self.tmp_dir = Path(args.tmpdir)  
        self.tmp2_dir = Path(args.tmpdir2) if args.tnpdir2 else None 
        self.plotid = args.id 
        self.memo = args.memo 
        self.nobitfield = args.nobitfield 
        
      
def plot_chain(args, root_path):  
      try: 
         validate_plot_size(root_path, args.size, args.override)  
      except ValueError as e:  
          print(e)  
          return 
      
      plot_keys = asyncio.run(
        resolve_plot_keys(
            None if args.farmerkey == b"" else args.farmerkey.hex(),  
            args.alt_fingerprint, 
            None if args.pool_key == b"" else args.pool_key.hex(),  
            None if args.contract == "" else args.contract,  
            root_path,  
            log, 
            args.connect_to_daemon, 
        )
    )
      asyncio.run(create_plots(Params(args), plot_keys))   
      if not args.exclude_final_dir:  
        try: 
            add_plot_directory(root_path, args.finaldir)  
        except ValueError as e:  
            print(e)
            
            
