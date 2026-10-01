# Chromebook hardware controls

SparkOS uses the Linux input stack for Chromebook keyboard/media keys. Brightness uses the kernel backlight interface when the board exposes one. Power-button and lid events belong to the system power manager, not the browser UI.

ChromeOS documents dedicated brightness controls and hardware power-button behavior; exact behavior varies by device. citeturn0search2turn0search10

Chromebook embedded-controller behavior remains board-specific, so SparkOS uses the kernel's Chromebook/EC drivers instead of directly accessing EC registers.
