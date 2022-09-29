import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("chain_ROOT", "~/.chain/mainnet"))).resolve()
STANDALONE_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("chain_STANDALONE_WALLET_ROOT", "~/.chain/standalone_wallet"))
).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("chain_KEYS_ROOT", "~/.chain_keys"))).resolve()
