# EdgeX Snaps Nightly Build

Canonical publishes the following [EdgeX](https://www.edgexfoundry.org/) Snaps to the Snap Store:
- [edgexfoundry](https://snapcraft.io/edgexfoundry)
- [edgex-cli](https://snapcraft.io/edgex-cli)
- [edgex-ui](https://snapcraft.io/edgex-ui)
- [edgex-app-service-configurable](https://snapcraft.io/edgex-app-service-configurable)
- [edgex-app-rfid-llrp-inventory](https://snapcraft.io/edgex-app-rfid-llrp-inventory)
- [edgex-device-camera](https://snapcraft.io/edgex-devic)
- [edgex-device-gpio](https://snapcraft.io/edgex-device-gpio)
- [edgex-device-modbus](https://snapcraft.io/edgex-device-modbus)
- [edgex-device-mqtt](https://snapcraft.io/edgex-device-mqtt)
- [edgex-device-rest](https://snapcraft.io/edgex-device-rest)
- [edgex-device-rfid-llrp](https://snapcraft.io/edgex-device-rfid-llrp)
- [edgex-device-snmp](https://snapcraft.io/edgex-device-snmp)
- [edgex-device-usb-camera](https://snapcraft.io/edgex-device-usb-camera)
- [edgex-device-virtual](https://snapcraft.io/edgex-device-virtual)

The snaps are built nightly from the [upstream](https://www.github.com/edgexfoundry) repos and published to the store under `latest/edge` channel.

The builds are triggered using the Github Action [nightly-build workflow](https://github.com/canonical/edgex-sync/tree/main/.github/workflows/nightly-build.yml) which uses [edgex-launchpad-build-action](https://github.com/canonical/edgex-launchpad-build-action). The action take various input including three secrets which are stored as [secrets in this project](https://github.com/canonical/edgex-sync/settings/secrets/actions).

Once triggered, the builds run on [Launchpad build farm](https://launchpad.net/builders). The status of the builds can be monitored [here](https://launchpad.net/~canonical-edgex/+snaps).
