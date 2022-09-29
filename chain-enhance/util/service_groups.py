from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "chain_harvester chain_timelord_launcher chain_timelord chain_farmer chain_full_node chain_wallet".split(),
    "node": "chain_full_node".split(),
    "harvester": "chain_harvester".split(),
    "farmer": "chain_harvester chain_farmer chain_full_node chain_wallet".split(),
    "farmer-no-wallet": "chain_harvester chain_farmer chain_full_node".split(),
    "farmer-only": "chain_farmer".split(),
    "timelord": "chain_timelord_launcher chain_timelord chain_full_node".split(),
    "timelord-only": "chain_timelord".split(),
    "timelord-launcher-only": "chain_timelord_launcher".split(),
    "wallet": "chain_wallet".split(),
    "introducer": "chain_introducer".split(),
    "simulator": "chain_full_node_simulator".split(),
    "crawler": "chain_crawler".split(),
    "seeder": "chain_crawler chain_seeder".split(),
    "seeder-only": "chain_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
