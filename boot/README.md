# SparkOS Boot Animation

The first SparkOS boot animation prototype is intentionally small and silent.

Design goals:

- ChromeOS-inspired simplicity
- Dark neutral background
- Small white SparkOS mark
- Short scale/fade animation
- No sound
- No network access
- Suitable as the visual source for the eventual early-boot theme

## Next step

The SVG is the design prototype. The final boot integration will be converted into a native early-boot theme (such as Plymouth or the equivalent boot stack selected for SparkOS) so the animation can appear before the desktop starts.
