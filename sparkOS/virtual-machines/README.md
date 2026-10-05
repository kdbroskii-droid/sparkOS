# SparkOS Second PC

SparkOS can create a second isolated virtual PC on the same physical machine.

## Design

Main PC: SparkOS desktop and normal apps.
Second PC: separate virtual CPU/RAM allocation, separate virtual disk, and a separate virtual network.

Both PCs can later use SparkLink for explicitly enabled file sharing, clipboard sharing, discovery, and remote display.

The second PC is a VM, so it has bounded resources instead of pretending one physical CPU/GPU is two independent computers.

## Commands

second-pc-manager.py create — create the VM disk.
second-pc-manager.py command — print the QEMU launch command.
second-pc-manager.py status — show the current configuration.

Future UI: Settings → System → Second PCs.