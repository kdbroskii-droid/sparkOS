# SparkOS Package Manager

One native package service will provide a common interface for EXK, APK and EXE packages.

## Source adapters
- APK adapter: Aurora Store. Aurora Store retrieves app data from Google Play rather than hosting the applications itself.
- EXE/software adapter: UniGetUI-compatible package managers. UniGetUI provides a GUI over package managers and supports discovery, installation, updating and removal.

## Installation flow
1. Get package metadata from the selected source adapter.
2. Download into an isolated temporary directory.
3. Verify publisher, signature and checksum where available.
4. Ask for user confirmation.
5. Install into the correct runtime.
6. Register the application with SparkOS.
7. Remove temporary files.

The App Store UI never embeds the source websites.