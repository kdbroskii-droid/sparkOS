# SparkOS first-party apps

The initial app IDs are `files`, `chrome`, `settings`, and `terminal`. Their display metadata is in `config/apps.toml`.

These IDs and manifests are app-manager contracts, not proof that executable apps exist. Each app needs a native implementation and a compatible runtime before it can launch on a booted SparkOS.

- Files: native file browser, initially read-only where filesystem safety is uncertain.
- Chrome: launch official Google Chrome only when a compatible supported runtime/package is available; do not silently substitute Chromium.
- Settings: implement the categories in `config/settings-sections.toml`.
- Terminal: start a restricted command/session interface only after process and permission boundaries exist.