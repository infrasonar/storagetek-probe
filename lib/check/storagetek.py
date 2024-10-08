from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery


QUERIES = (
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibrary'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibVersion'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibLSMConfigEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibLSMStateEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibLocation'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibNetworkEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibStatistics'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibMediaEventEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibDate'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibCleaning'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibCleanWarnEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibCleanCartEntry'],
)


async def check_storagetek(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    return state
