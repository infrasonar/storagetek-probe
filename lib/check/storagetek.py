from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery


QUERIES = (
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibrary'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibVersion'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibLocation'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibDate'],
)


async def check_storagetek(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    return state
