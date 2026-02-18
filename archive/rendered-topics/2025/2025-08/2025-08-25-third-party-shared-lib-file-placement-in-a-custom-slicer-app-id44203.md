# Third party shared LIB file placement in a custom Slicer application

**Topic ID**: 44203
**Date**: 2025-08-25
**URL**: https://discourse.slicer.org/t/third-party-shared-lib-file-placement-in-a-custom-slicer-application/44203

---

## Post #1 by @ejm-revvity (2025-08-25 21:16 UTC)

<p>I’m adding in license management functionality to our custom Slicer application. We’re using Revanera FlexNet which provides a sort of SDK in the form of include (.h) files, .lib files and runtime .dll files.</p>
<p>I can successfully build/link/run the application IFF I place all source, includes, LIB files in the top-level project directory and make minor changes to CMakeLists.txt to add all the relevant source files to APPLIB_SRCS.</p>
<p>However, when I create a logical directory structure and place all the required files in their respective places, along with creating the associated CMakeLists.txt files, I can successfully build the application, but the linker reports a series of unresolved symbols. I have verified that the symbols exist in the relevant .lib files (and of course they do since I can link successfully in the ‘single directory’ case), so the conclusion I must draw is that the build system is not finding the required .lib files.</p>
<p>Where should they be placed?</p>
<p>Here is the folder structure and relevant part of the top-level CMakeLists.txt file:</p>
<pre data-code-wrap="plaintext"><code class="lang-plaintext">XXXApp/ 
├── CMakeLists.txt  # Top-level; single executable output
├── LicenseManager/ # LicenseManagerXXX source and includes; no lib input or output
│   └── CMakeLists.txt
│   └── FlexNet/ # FlexNetXXX source and includes; no lib input or output 
│       └── CMakeLists.txt 
│       └── Flc/ # Flc includes for third party library 
│           └── CMakeLists.txt 
│       └── Lib/ # Flc imported library .lib and .dll files 
│           └── CMakeLists.txt (not necessary because not building from source)
</code></pre>
<pre data-code-wrap="bash"><code class="lang-bash">if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxClientXT.lib")
  file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxClientXT.lib" DESTINATION ${CMAKE_BINARY_DIR})
endif()

if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxCommonXT.lib")
  file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxCommonXT.lib" DESTINATION ${CMAKE_BINARY_DIR})
endif()

set(APPLIB_NAME ${APPLIB_NAME} CACHE INTERNAL "Main application library")

add_library(FlxClientXT SHARED IMPORTED)
set_target_properties(FlxClientXT PROPERTIES
  IMPORTED_IMPLIB "${CMAKE_BINARY_DIR}/FlxClientXT.lib"
  IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxCore64.dll"
)

add_library(FlxCommonXT SHARED IMPORTED)
set_target_properties(FlxCommonXT PROPERTIES
  IMPORTED_IMPLIB "${CMAKE_BINARY_DIR}/FlxCommonXT.lib"
  IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/LicenseManager/FlexNet/Lib/FlxComm64.dll"
)

add_subdirectory(LicenseManager)
add_subdirectory(LicenseManager/FlexNet)
add_subdirectory(LicenseManager/FlexNet/Flc)

target_include_directories(${APP_TARGET_NAME}
    PRIVATE
        LicenseManager/FlexNet
        LicenseManager/FlexNet/Flc
)

target_link_libraries(${APP_TARGET_NAME}
    ${APPLIB_NAME}
        FlxClientXT
        FlxCommonXT
        legacy_stdio_definitions
)
</code></pre>

---
