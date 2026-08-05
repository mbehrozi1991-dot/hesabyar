[app]

title = Hesabyar

package.name = hesabyar

package.domain = org.hesabyar

source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,ttf,db,json

version = 0.1

requirements = python3,kivy==2.3.1,kivymd,arabic-reshaper,python-bidi

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[app:android]

android.api = 35

android.minapi = 24

android.ndk = 27c

android.archs = arm64-v8a

android.accept_sdk_license = True
