# EdgeX Snaps Nightly Build

Canonical publishes the several EdgeX snaps to the Snap Store.

The snaps are built nightly from the [upstream](https://www.github.com/edgexfoundry) repos and published to the store under `latest/edge` channel.

The builds are triggered using the Github Action [nightly-build workflow](https://github.com/canonical/edgex-sync/tree/main/.github/workflows/nightly.yml) which uses [edgex-launchpad-build-action](https://github.com/canonical/edgex-launchpad-build-action). The action take various input including three secrets which are stored as [secrets in this project](https://github.com/canonical/edgex-sync/settings/secrets/actions).

Once triggered, the builds run on [Launchpad build farm](https://launchpad.net/builders). The status of the builds can be monitored [here](https://launchpad.net/~canonical-edgex/+snaps).
