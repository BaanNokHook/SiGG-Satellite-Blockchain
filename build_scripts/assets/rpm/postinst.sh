#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /usr/lib/chain-blockchain/resources/app.asar.unpacked/daemon/chain /usr/bin/chain || true
ln -s /usr/lib/chain-blockchain/resources/app.asar.unpacked/daemon /opt/chain || true
