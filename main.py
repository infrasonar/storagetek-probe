from libprobe.probe import Probe
from lib.check.storagetek import check_storagetek
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'storagetek': check_storagetek
    }

    probe = Probe("storagetek", version, checks)

    probe.start()
