# CMAKE_CXX_COMPILER is not a full path to an existing compiler tool when configure an extension

**Topic ID**: 19355
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/cmake-cxx-compiler-is-not-a-full-path-to-an-existing-compiler-tool-when-configure-an-extension/19355

---

## Post #1 by @upupming (2021-08-25 09:23 UTC)

<p>I am trying to build a C++ extension for 3D Slicer. I have tested SlicerIGT and SlicerFreeSurfer. I have followed the instruction here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ/Extensions - Slicer Wiki</a></p>
<p>On both SlicerIGT and SlicerFreeSurfer, I got the CMAKE_CXX_COMPILER is not a full path to an existing compiler tool when configure an extension  error. Could you please help me, thanks!</p>
<p>This is configure command I used:</p>
<pre><code class="lang-auto">"C:\Program Files\CMake\bin\cmake.EXE" --no-warn-unused-cli -DSlicer_DIR:PATH=C:/D/S4R/Slicer-build -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE -Hc:/Users/ming/projects/SlicerFreeSurfer -Bc:/Users/ming/projects/SlicerFreeSurfer/build -G "Visual Studio 16 2019"
</code></pre>
<p>This is the CMake error log:</p>
<pre><code class="lang-auto">[cmake] Not searching for unused variables given on the command line.
[cmake] -- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.
[cmake] -- The C compiler identification is MSVC 19.29.30133.0
[cmake] -- The CXX compiler identification is MSVC 19.29.30133.0
[cmake] -- Detecting C compiler ABI info
[cmake] -- Detecting C compiler ABI info - done
[cmake] -- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe - skipped
[cmake] -- Detecting C compile features
[cmake] -- Detecting C compile features - done
[cmake] -- Detecting CXX compiler ABI info
[cmake] -- Detecting CXX compiler ABI info - done
[cmake] -- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe - skipped
[cmake] -- Detecting CXX compile features
[cmake] -- Detecting CXX compile features - done
[cmake] -- Found PythonLibs: C:/D/S4R/python-install/libs/python36.lib (found version "3.6.7") 
[cmake] -- Trying to find DCMTK expecting DCMTKConfig.cmake
[cmake] -- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
[cmake] -- Found CURL: C:/D/S4R/curl-install/lib/libcurl.lib (found version "7.70.0-DEV")  
[cmake] -- RapidJSON found. Headers: ./include/Slicer-4.13
[cmake] -- Trying to find DCMTK expecting DCMTKConfig.cmake
[cmake] -- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
[cmake] -- Found PythonLibs: C:/D/S4R/python-install/libs/python36.lib  
[cmake] -- Found PythonInterp: C:/D/S4R/python-install/bin/PythonSlicer.exe (found version "3.6.7") 
[cmake] -- Found SWIG: C:/D/S4R/swigwin-4.0.2/swig.exe (found version "4.0.2")  
[cmake] -- Configuring SlicerFreeSurfer with Qt 5.15.2 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )
[cmake] -- Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins
[cmake] -- Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin
[cmake] -- Checking EXTENSION_NAME variable
[cmake] -- Checking EXTENSION_NAME variable - NOTDEFINED
[cmake] -- Checking MODULE_NAME variable
[cmake] -- Checking MODULE_NAME variable - NOTDEFINED
[cmake] -- Checking PROJECT_NAME variable
[cmake] -- Checking PROJECT_NAME variable - SlicerFreeSurfer
[cmake] -- Setting EXTENSION_NAME ......................: SlicerFreeSurfer
[cmake] -- Checking to see if CXX compiler accepts flag -features=no%anachronisms
[cmake] -- Checking to see if CXX compiler accepts flag -features=no%anachronisms - No
[cmake] -- Adding ConfigureAdditionalLauncherSettings target
[cmake] -- Adding ConfigureAdditionalLauncherSettings target - yes
[cmake] -- Setting EXTENSION_SOURCE_DIR ................: C:/Users/ming/projects/SlicerFreeSurfer
[cmake] -- Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: C:/Users/ming/projects/SlicerFreeSurfer/build
[cmake] -- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
[cmake] -- Setting MIDAS_PACKAGE_URL ...................: http://slicer.kitware.com/midas3
[cmake] -- Setting MIDAS_PACKAGE_EMAIL .................: OBFUSCATED
[cmake] -- Setting MIDAS_PACKAGE_API_KEY ...............: OBFUSCATED
[cmake] -- Setting EXTENSION_SVNUSERNAME ...............: NOT DEFINED
[cmake] -- Setting EXTENSION_SVNPASSWORD ...............: NOT DEFINED
[cmake] -- Setting EXTENSION_DEPENDS ...................: NA
[cmake] -- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
[cmake] -- Setting EXTENSION_HOMEPAGE ..................: https://github.com/PerkLab/SlicerFreeSurfer
[cmake] -- Setting EXTENSION_CONTRIBUTORS ..............: Kyle Sunderland (Perk Lab (Queen's University)), Andras Lasso (Perk Lab ( [...]
[cmake] -- Setting EXTENSION_CATEGORY ..................: Neuroimaging
[cmake] -- Setting EXTENSION_ICONURL ...................: https://github.com/PerkLab/SlicerFreeSurfer/raw/master/SlicerFreeSurfer.p [...]
[cmake] -- Setting EXTENSION_DESCRIPTION ...............: Extension for handling FreeSurfer files in Slicer. Features importer for  [...]
[cmake] -- Setting EXTENSION_SCREENSHOTURLS ............: https://github.com/PerkLab/SlicerFreeSurfer/raw/master/Screenshots/FreeSu [...]
[cmake] -- Setting EXTENSION_ENABLED ...................: 1
[cmake] -- Setting EXTENSION_STATUS ....................: NOT DEFINED
[cmake] -- Setting default for EXTENSION_STATUS ........: 
[cmake] -- Found Git: C:/Program Files/Git/cmd/git.exe  
[cmake] -- Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE) 
[cmake] CMake Error at FreeSurfer/CMakeLists.txt:1 (project):
[cmake]   The CMAKE_C_COMPILER:
[cmake] 
[cmake]     C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe
[cmake] 
[cmake]   is not a full path to an existing compiler tool.
[cmake] 
[cmake] 
[cmake] 
[cmake] CMake Error at FreeSurfer/CMakeLists.txt:1 (project):
[cmake]   The CMAKE_CXX_COMPILER:
[cmake] 
[cmake]     C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe
[cmake] 
[cmake]   is not a full path to an existing compiler tool.
[cmake] 
[cmake] 
[cmake] 
[cmake] -- Configuring incomplete, errors occurred!
[cmake] See also "C:/Users/ming/projects/SlicerFreeSurfer/build/CMakeFiles/CMakeOutput.log".
[cmake] See also "C:/Users/ming/projects/SlicerFreeSurfer/build/CMakeFiles/CMakeError.log".

</code></pre>

---

## Post #2 by @upupming (2021-08-25 09:43 UTC)

<p>Oh I found the cause of the error. I built Slicer a few days ago, after that I update the Visual Studio version, and the <code>cl.exe</code> path has changed.</p>

---
