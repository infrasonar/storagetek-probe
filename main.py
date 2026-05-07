from libprobe.probe import Probe
from lib.check.hardware import CheckHardware
from lib.check.storagetek import CheckStoragetek
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckHardware,
        CheckStoragetek,
    )

    probe = Probe("storagetek", version, checks)

    probe.start()
