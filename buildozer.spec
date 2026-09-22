[app]

# (str) Title of your application
title = Calculadora Depósitos

# (str) Package name
package.name = calculadoradepositos

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ejemplo

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,xlsx

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (str) Android build-tools version to use
android.build_tools_version = 33.0.2

# (android.api) API number to target
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then accept all SDK licenses automatically
android.accept_sdk_licenses = True

# (bool) Allow cleartext network traffic (necesario para la conexión del WebView)
android.uses_cleartext_traffic = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = warning)
warn_on_root = 1