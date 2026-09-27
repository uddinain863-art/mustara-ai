[app]
title = Mustara AI
package.name = mustaraai
package.domain = org.mustara
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,urllib3
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
