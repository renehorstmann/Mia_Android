cmake_minimum_required(VERSION 3.6)
project(Mia)


#
# Example user settings to be changed
#
set(MIA_USE_APP_HELLO ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_APP_EX ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_APP_EX_MAIN OFF CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_APP_EX_MAIN_TEA OFF CACHE BOOL "ANDROID" FORCE)

# change this to rerun cmake, cause AndroidStudio has no button for that :D
set(MIA_ANDROID_CMAKE_REBUILD ON CACHE BOOL "ANDROID" FORCE)

#
# Settings needed for the android port:
#

set(MIA_PROJECT "main" CACHE STRING "ANDROID" FORCE)
set(MIA_USE_VENDOR_SDL ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_VENDOR_SDL_IMAGE ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_VENDOR_SDL_NET ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_VENDOR_SDL_TTF ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_FETCH ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_SOCKET ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_TTF ON CACHE BOOL "ANDROID" FORCE)
set(MIA_USE_BUILT_AS_LIBRARY ON CACHE BOOL "ANDROID" FORCE)

# java package name, must match to allow jni
add_definitions(-DMIA_ANDROID_PACKAGE=@@@package_underscored@@@)

# Tell the linker to allow flexible page sizes
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,-z,max-page-size=0x4000")

# In this directory should Mia be cloned "Mia/" ("app/jni/Mia")
add_subdirectory(Mia)
