# Mia_Android

Android Port for the [Mia](https://github.com/renehorstmann/Mia) engine.

## Install

Install [Android Studio](https://developer.android.com/studio) and the latest sdk tools.
Install path must not contain a whitespace or other special symbols.

Create the Android project with the template generator:
```sh
# Use your own package name like:
python3 template.py de horsimann tea
```
The project will be generated in the out dir.
> The generated project path must not include a whitespace or other special symbols!

Next clone Mia (and the sdl vendored submodules):
```sh
cd out/tea/app/jni
git clone --recursive git@github.com:renehorstmann/Mia.git
```

Now open the project in Android Studio and have fun!

> See `app/jni/CMakeLists.txt` for cmake configs

> See `app/src/main/AndroidManifest.xml` for android projects, like enabling mic or cam

> Compiling may need an additional attempt, 
> cause `res`ources and the logo are cloned by the cmake script and may miss on first build try.

## Author
René Horstmann *aka* Horsimann
