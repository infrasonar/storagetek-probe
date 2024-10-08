from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery


QUERIES = (
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slPhysHardware'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slHostInterfaceEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slTempSensorEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slFanEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slPowerSupplyEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slRobotEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slElevatorEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slControllerEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slPtpEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slDriveEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slCapEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slTurntableEntry'],
    MIB_INDEX['STREAMLINE-TAPE-LIBRARY-MIB']['slMVDriveEntry'],
)


async def check_hardware(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    return state
