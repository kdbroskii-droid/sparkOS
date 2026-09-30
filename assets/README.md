# SparkOS Visual Assets

This directory contains the reusable visual system for SparkOS.

## Design
- Dark neutral boot background
- White SparkOS mark
- Subtle blue accent for the desktop
- Rounded, simple ChromeOS-inspired shapes
- Windows-like centered taskbar geometry
- No boot sound

## Asset groups
- brand: logos and marks
- boot: boot animation source and frame specification
- recovery: recovery state specifications
- ui: desktop/taskbar/window assets
- icons: system icon specifications

Vector assets are preferred so the final image size can be selected at build time without shipping many duplicate raster files.
