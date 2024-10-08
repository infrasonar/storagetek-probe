from libprobe.probe import Probe
from lib.check.storagetek import check_storagetek
from lib.check.hardware import check_hardware
from lib.check.storage import check_storage
from lib.check.inventory import check_inventory
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'hardware': check_hardware,
        'inventory': check_inventory,
        'storage': check_storage,
        'storagetek': check_storagetek,

    }

    probe = Probe("storagetek", version, checks)

    probe.start()
