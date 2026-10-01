# SparkOS wireless layer

SparkOS uses the Linux wireless stack instead of device-specific drivers. Modern 802.11 hardware is exposed through cfg80211/nl80211 and managed in userspace by NetworkManager. Bluetooth is handled by BlueZ.

Wi-Fi supports status, scanning, connection, disconnection and radio power. Bluetooth supports discovery, pairing, trusting, connection and radio power.

Hardware compatibility depends on the Chromebook's Linux kernel driver and firmware. SparkOS reports unsupported hardware instead of pretending it works.

Wi-Fi passwords must never be written into logs. A production GUI should use NetworkManager's secure connection APIs.
