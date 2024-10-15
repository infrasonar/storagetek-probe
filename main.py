from libprobe.probe import Probe
from lib.check.storagetek import check_storagetek
from lib.check.hardware import check_hardware
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'hardware': check_hardware,
        'storagetek': check_storagetek,

    }

    probe = Probe("storagetek", version, checks)

    probe.start()
