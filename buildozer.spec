[app]
title = Business App
package.name = businessapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,fpdf,openpyxl
orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
