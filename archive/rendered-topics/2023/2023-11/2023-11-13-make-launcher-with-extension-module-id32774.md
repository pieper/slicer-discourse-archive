---
topic_id: 32774
title: "Make Launcher With Extension Module"
date: 2023-11-13
url: https://discourse.slicer.org/t/32774
---

# Make launcher with extension module

**Topic ID**: 32774
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/make-launcher-with-extension-module/32774

---

## Post #1 by @park (2023-11-13 09:54 UTC)

<p>Hi all</p>
<p>I am trying to create an application launcher with custom and built extionsion modules.<br>
I would like the modules loaded in slicer already when the custom application is installed by launcher.</p>
<p>I found a similar topic [<a href="https://discourse.slicer.org/t/customized-application-launchers/564">Customized application launchers</a>] and there is an option for custom installers that can be built without modifying anything in Slicer source code, just by tuning CMake options.</p>
<p>As I understood :</p>
<ol>
<li>the base slicer and all modules should be built already in the released version separately.</li>
<li>a .cmake file should be created or modified when building <code>PACKAGE</code> project in the CMakePredefinedTargets folder.</li>
</ol>
<p>Could you let me know which .cmake file should be modified and can I get any examples of it?</p>
<p>This is my file list for cmake build .<br>
The S dir is slicer source code and the left dirs are modules</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7337576781024bd2147b76f2f50d70f0e398a4fc.png" alt="image" data-base62-sha1="grftBIrfWGbMgLoZFdtkQueOU2g" width="228" height="464"></p>

---

## Post #2 by @jcfr (2023-11-13 13:41 UTC)

<p>If you have not done already, looking at this project may be helpful to understand the process:</p>
<ul>
<li><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a></li>
</ul>
<p>… as well as these two companion posts published on the Kitware blog:</p>
<ul>
<li><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">SlicerCAT: Creating custom applications based on 3D Slicer</a></li>
<li><a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/">SlicerCAT and Python: Creating Custom Slicer Applications with Qt Stylesheets</a></li>
</ul>

---

## Post #3 by @park (2023-11-27 11:37 UTC)

<p>Thank you for your reply</p>
<p>If I modify the CMakeLists.txt of the SlicerCat or make changes to qCustomAppNameAppMainWindow.cxx, do I need to rebuild the entire project? If so, are there any ways to reduce the build time? Building once takes a considerable amount of time.</p>

---

## Post #4 by @pieper (2023-11-27 12:20 UTC)

<p>Yes, project-wide changes like the top level CMakeLists.txt can trigger a long rebuild.  However since the default is shared libraries, once you have the structure set up changes to the implementation go more quickly since you can just rebuild the inner targets.</p>

---

## Post #5 by @park (2023-11-27 12:28 UTC)

<p>Hi pieper</p>
<p>Can you recommend an alternative method for creating a package, other than using Slicer Cat? The project has already progressed significantly, and it seems challenging to reconfigure it using Slicer Cat. Despite the challenges, is it still more efficient to use Slicer Cat and start over from the beginning? The functionality is already complete, but creating a package turns out to be more challenging than anticipated.</p>

---

## Post #6 by @pieper (2023-11-27 12:34 UTC)

<p>Building custom C++ packages that will run reliably on other computers is a big challenge and there are many things that can go wrong.  SlicerCat leverages a lot of debugging that allows Slicer packages to build and run cross-platform.  The only reliable options I know of to simplify the process are to narrow the target (e.g. only support one OS, but this only helps a bit) or write only in Python so you can use pre-build binaries.</p>

---

## Post #7 by @park (2023-11-27 12:48 UTC)

<p>Thank you Steve</p>
<p>jcfr&amp;Steve could you check there is any thing worng my CmakeList.txt ?<br>
The build was completed without error but I cannot find extension module like IGT, OpendIGTLink ,</p>
<p>Moreover, how could I use the modified Slicer source file that I worked on instead of the Slicer file obtained from Git?</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.16.3)

set(Qt5_DIR "C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5")
set(Navigation_SOURCE_DIR "C:/D4/snm/Modules/navigation")


# Enable C++14
if(NOT DEFINED CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set (EP_GIT_PROTOCOL "https")

# Slicer sources
include(FetchContent)
if(NOT DEFINED slicersources_SOURCE_DIR)
  # Download Slicer sources and set variables slicersources_SOURCE_DIR and slicersources_BINARY_DIR
  FetchContent_Populate(slicersources
    GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/Slicer
    GIT_TAG        98a2cba1dc328e6872c848c9dc20e78205718cc1
    GIT_PROGRESS   1
    )
else()
  set(slicersources_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/slicersources-subbuild)
endif()

# macOS initialization
set(CMAKE_MODULE_PATH ${slicersources_SOURCE_DIR}/CMake ${CMAKE_MODULE_PATH})
include(SlicerInitializeOSXVariables)

project(snm)

# Configure Application
set(Slicer_APPLICATIONS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Applications)
set(Slicer_MAIN_PROJECT "snmApp")

# Set organization
set(Slicer_ORGANIZATION_DOMAIN "snm_co")
set(Slicer_ORGANIZATION_NAME   "snm_co")

# Default home and favorite modules
set(Slicer_DEFAULT_HOME_MODULE "Home")
set(Slicer_DEFAULT_FAVORITE_MODULES "Data, Volumes, Models, Transforms, Markups, SegmentEditor")

# Configure SuperBuild
set(SUPERBUILD_TOPLEVEL_PROJECT Slicer)
set(EXTERNAL_PROJECT_ADDITIONAL_DIR "${CMAKE_CURRENT_SOURCE_DIR}/SuperBuild")
include(ExternalProjectDependency)

# Additional Slicer dependencies looked up in EXTERNAL_PROJECT_ADDITIONAL_DIR
set(Slicer_ADDITIONAL_DEPENDENCIES
  )

#  Enable listed remote modules from ITK
set(Slicer_ITK_ADDITIONAL_MODULES
  )

if(NOT CMAKE_CONFIGURATION_TYPES)
  set(Slicer_DEFAULT_BUILD_TYPE "Release")
endif()
include(SlicerInitializeBuildType)
include(SlicerInitializeReleaseType)

# Set application bundle identifier for macOS
if(APPLE)
  set(Slicer_MACOSX_BUNDLE_GUI_IDENTIFIER "snm")
endif()

# Installation folder and admin account requirement for Windows
if(WIN32)
  # Note: To avoid escaping issue, make sure to use forward slash when setting
  #       "Slicer_CPACK_NSIS_INSTALL_ROOT". It is replaced by "\\\\" in SlicerCPack.
  set(Slicer_CPACK_NSIS_INSTALL_REQUIRES_ADMIN_ACCOUNT ON)
  if(Slicer_CPACK_NSIS_INSTALL_REQUIRES_ADMIN_ACCOUNT)
    # User has administrative privileges, therefore we can install to shared folder
    # "C:\Program Files" or "C:\Program Files (x86)".
    if(CMAKE_CL_64)
      set(Slicer_CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES64")
    else()
      set(Slicer_CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
    endif()
  else()
    # We do not require administrative privileges, therefore we install to user folder
    # "C:\Users\&lt;username&gt;\AppData\Local".
    set(Slicer_CPACK_NSIS_INSTALL_ROOT "$LOCALAPPDATA/${Slicer_ORGANIZATION_NAME}")
  endif()
endif()

# Slicer options
option(BUILD_TESTING                            "Build application test suite"                        ON)
option(Slicer_BUILD_APPLICATIONUPDATE_SUPPORT   "Build application update support"                    ON)
option(Slicer_BUILD_DOCUMENTATION               "Build documentation (Doxygen, sphinx, ...)"          ON)
if(WIN32)
  option(Slicer_BUILD_WIN32_CONSOLE_LAUNCHER    "Build ${PROJECT_NAME} launcher executable as a console app on windows (displays console at application start)" OFF)
  option(Slicer_BUILD_WIN32_CONSOLE             "Build application executable as a console app (allows capturing and piping console output)" ON)
endif()

option(Slicer_BUILD_DICOM_SUPPORT               "Build application with DICOM support"                ON)
option(Slicer_BUILD_DIFFUSION_SUPPORT           "Build application with Diffusion support"            ON)
option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT    "Build application with ExtensionManager support"     ON)
option(Slicer_BUILD_APPLICATIONUPDATE_SUPPORT   "Build Slicer with application update support"        ON)
option(Slicer_BUILD_MULTIVOLUME_SUPPORT         "Build application with MultiVolume support"          ON)
option(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT "Build application with parameter serializer support" ON)
option(Slicer_USE_PYTHONQT                      "Build application with Python support"               ON)
option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            ON)
option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            ON)

option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           ON)
option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             ON)
option(Slicer_BUILD_CompareVolumes              "Build application with ChangeTrackerPy module"       ON)
option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  ON)
option(Slicer_BUILD_SurfaceToolbox              "Build application with SurfaceToolbox module"        ON)

# Enable Slicer built-in modules
set(Slicer_CLIMODULES_ENABLED
  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume
  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume
  )
set(Slicer_QTLOADABLEMODULES_ENABLED
  )
set(Slicer_QTSCRIPTEDMODULES_ENABLED
  )

# Disable Slicer built-in modules
set(Slicer_CLIMODULES_DISABLED
  )
set(Slicer_QTLOADABLEMODULES_DISABLED
  SceneViews
  SlicerWelcome
  ViewControllers
  )
set(Slicer_QTSCRIPTEDMODULES_DISABLED
  DataProbe
  DMRIInstall
  Endoscopy
  LabelStatistics
  PerformanceTests
  SampleData
  VectorToScalarVolume
  )

# Enable/Disable Slicer custom modules: To create a new module, use the SlicerExtensionWizard.
set(Slicer_EXTENSION_SOURCE_DIRS
  ${snm_SOURCE_DIR}/Modules/CLI/MyCLIModule
  ${snm_SOURCE_DIR}/Modules/Loadable/MyLoadableModule
  ${snm_SOURCE_DIR}/Modules/Scripted/Home
  )

# Add remote extension source directories


# SlicerCustomAppUtilities
set(extension_name "SlicerCustomAppUtilities")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/KitwareMedical/SlicerCustomAppUtilities.git
  GIT_TAG        1d984a2c9143e2617ff1ffa9d86c51e07dc6321e
  GIT_PROGRESS   1
  QUIET
  )
message(STATUS "Remote - ${extension_name} [OK]")
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR}/Modules/Scripted/SlicerCustomAppUtilities)


# SlicerIGT
set(extension_name "SlicerIGT")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/slicerigt/slicerigt.git
  GIT_TAG master
  GIT_PROGRESS 1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})


# SlicerIGT
set(extension_name "SlicerIGSIO")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/IGSIO/SlicerIGSIO.git
  GIT_TAG master
  GIT_PROGRESS 1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})


# SlicerOpenIGTLink
set(extension_name "SlicerOpenIGTLink")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
 SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
 GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/openigtlink/SlicerOpenIGTLink.git
 GIT_PROGRESS   1
 QUIET
 )
message(STATUS "Remote - ${extension_name} [OK]")
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})


# SlicerSandbox
set(extension_name "SlicerSandbox")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
 SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
 GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/PerkLab/SlicerSandbox.git
 GIT_PROGRESS   1
 QUIET
 )
message(STATUS "Remote - ${extension_name} [OK]")
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})


# Enable/Disable Slicer custom modules: To create a new module, use the SlicerExtensionWizard.
set(Slicer_EXTENSION_SOURCE_DIRS ${Navigation_SOURCE_DIR})


# Add Slicer sources
add_subdirectory(${slicersources_SOURCE_DIR} ${slicersources_BINARY_DIR})
</code></pre>
<p>Moreover, I really appriciate if you give me the example of CMakeList.txt you use.</p>
<p>Thanks</p>

---
