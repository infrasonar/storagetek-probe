from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery


QUERIES = (
    (MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibrary'], False),
    (MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibVersion'], False),
    (MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibLocation'], False),
    (MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slLibDate'], False),
)


class CheckStoragetek(Check):
    key = 'storagetek'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)
        return state
