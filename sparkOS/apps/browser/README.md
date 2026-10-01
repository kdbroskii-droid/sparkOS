# SparkOS Browser

SparkOS Browser is the Chromium integration point. SparkOS should launch a packaged Chromium/ChromiumOS browser rather than implementing a second web-rendering engine. Chromium is already designed as a multi-process browser with separate browser and renderer processes, which fits the SparkOS security model. citeturn0search0

The final integration should provide the SparkOS theme, profile location, downloads location, keyboard shortcuts and window-manager integration.