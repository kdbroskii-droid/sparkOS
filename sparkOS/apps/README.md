# SparkOS native applications

The production apps are native programs/services. The HTML files under `html/` are only visual prototypes.

| App | Native source | Package |
|---|---|---|
| Files | `files/main.py` | `files.exk` |
| Terminal | `terminal/main.py` | `terminal.exk` |
| Settings | `settings/main.py` | `settings.exk` |
| App Store | `app-store/main.py` | `app-store.exk` |
| Browser | Chromium integration | `browser.exk` |

These Python implementations are development-stage native service prototypes. The final SparkOS image can replace them with compiled binaries without changing the EXK package manifests.