[app]

title = Hesabyar

package.name = hesabyar

package.domain = org.hesabyar

source.dir = .

source.include_exts = py,kv,png,jpg,json,db

version = 1.0

requirements = python3,kivy==2.1.0,kivymd==1.1.1,arabic-reshaper,python-bidi==0.4.2

orientation = portrait

fullscreen = 0



# Android

android.api = 35

android.minapi = 24

android.ndk = 27c

android.ndk_api = 24

android.archs = arm64-v8a

android.accept_sdk_license = True


[buildozer]

log_level = 2

warn_on_root = 1

