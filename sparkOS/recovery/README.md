# SparkOS Recovery

Recovery is a separate minimal boot environment intended to survive a normal factory reset.

States:
- GREEN: recovery is healthy and installation/recovery is available.
- RED: recovery integrity verification failed and recovery actions are blocked.
- BLACK + WHITE BAR: factory reset is running and the bar represents real progress.

Menu:
1. Get OS from USB
2. Get OS from Storage
3. Get OS from Web
4. Repair boot
5. Verify system
6. Factory reset
7. Restart

The recovery partition should be read-only during normal operation. Production images should be signed and verified. Normal factory reset must not erase recovery.

A UEFI boot manager can expose a separate recovery entry, and boot assessment can support rollback after repeated failed boots.
