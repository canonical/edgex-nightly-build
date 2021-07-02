# Github Actions workflow for building daily builds of EdgeX snaps

This repository contains the Github Actions workflow used to build EdgeX snaps. It uses a couple of custom Github Actions.
There is one workflow file per snap and they all perform the following steps:

1. build-snap: Builds the snap - to check that it can build. If that step suceeds, then proceed to
2. build-launchpad: Kick off a build on Launchpad, which creates the official latest/edge snap
