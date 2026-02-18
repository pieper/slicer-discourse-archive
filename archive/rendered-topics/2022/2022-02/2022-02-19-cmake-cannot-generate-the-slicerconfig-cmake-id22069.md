# Cmake cannot generate the SlicerConfig.cmake

**Topic ID**: 22069
**Date**: 2022-02-19
**URL**: https://discourse.slicer.org/t/cmake-cannot-generate-the-slicerconfig-cmake/22069

---

## Post #1 by @user5 (2022-02-19 18:38 UTC)

<p>I already follow the instruction to build the Slicer inner-build folder in git bash or cmake gui, but it still comes out this error.</p>
<blockquote>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions/Configure - Slicer Wiki</a></p>
</blockquote>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a></p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a746e03ed7410d80e2c1871993f25dec70d0188f.png" data-download-href="/uploads/short-url/nRNAuBqbzyEHjWFIbuerHDdQoHR.png?dl=1" title="23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a746e03ed7410d80e2c1871993f25dec70d0188f_2_690x356.png" alt="23" data-base62-sha1="nRNAuBqbzyEHjWFIbuerHDdQoHR" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a746e03ed7410d80e2c1871993f25dec70d0188f_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a746e03ed7410d80e2c1871993f25dec70d0188f_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a746e03ed7410d80e2c1871993f25dec70d0188f_2_1380x712.png 2x" data-dominant-color="030303"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">23</span><span class="informations">2508×1296 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, I use cmake to configure the code in this link first.</p>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a></p>
</blockquote>
<p>The build of this code is fine.</p>
<p>Second, I  configure the code of this extension (SlicerVR)</p>
<blockquote>
<p><a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a></p>
</blockquote>
<p>I cannot find out the SlicerConfig.camke in all build folder including Slicer-master’s inner-build folder.</p>
<p>Is it have anything that I forgot to do?</p>

---

## Post #2 by @lassoan (2022-02-19 19:44 UTC)

<p><code>SlicerConfig.cmake</code> is in your inner Slicer-build folder, such as <code>c:\D\S4D\Slicer-build\SlicerConfig.cmake</code> if the file is not there then your Slicer build was incomplete. Check the error messages that you got during the build and resolve them. If you are not sure how then upload the complete build log somewhere and post the link here.</p>

---

## Post #3 by @user5 (2022-02-20 06:32 UTC)

<p>For the first build,</p>
<pre><code class="lang-auto">Setting C++ standard
Setting C++ standard - C++14
Selecting Windows SDK version 10.0.22000.0 to target Windows 10.0.19044.
The C compiler identification is MSVC 19.29.30140.0
The CXX compiler identification is MSVC 19.29.30140.0
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe - skipped
Detecting C compile features
Detecting C compile features - done
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe - skipped
Detecting CXX compile features
Detecting CXX compile features - done
Configuring Slicer organization domain [www.na-mic.org]
Configuring Slicer organization name [NA-MIC]
Configuring Slicer default home module [Welcome]
Configuring Slicer default favorite modules [Data, Volumes, Models, Transforms, Markups, SegmentEditor]
Configuring Slicer text of disclaimer at startup [Thank you for using %1!

This software is not intended for clinical use.]
Configuring Slicer requires admin account [OFF]
Configuring Slicer install root [$LOCALAPPDATA/NA-MIC]
Configuring Slicer release type [Experimental]
CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:75 (message):
  Skipping repository info extraction: directory [C:/D/S4] is not a GIT or
  SVN checkout
Call Stack (most recent call first):
  CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)
  CMakeLists.txt:213 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

Configuring Slicer version [4.13.0-]
Configuring Slicer revision [3037]
CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:75 (message):
  Skipping repository info extraction: directory [C:/D/S4] is not a GIT or
  SVN checkout
Call Stack (most recent call first):
  CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)
  CMakeLists.txt:213 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

Configuring VTK
  Slicer_VTK_RENDERING_BACKEND is OpenGL2
  Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB
  Slicer_VTK_VERSION_MAJOR is 9
Configuring Slicer with Qt 5.15.2 (using modules: Core, Widgets, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, Multimedia, MultimediaWidgets, WebEngine, WebEngineWidgets, WebChannel, Script, LinguistTools, Test, )
Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins
Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin
Setting ExternalData_OBJECT_STORES to 'C:/D/S4D/ExternalData/Objects'
Configuring Slicer for [win-amd64]
Checking if CMake supports https
Checking if CMake supports https - ok
Remote - vtkAddon [OK]
Remote - MultiVolumeExplorer [OK]
Remote - MultiVolumeImporter [OK]
Remote - SimpleFilters [OK]
Remote - BRAINSTools [OK]
Remote - DataStore [OK]
Remote - CompareVolumes [OK]
Remote - LandmarkRegistration [OK]
Remote - SurfaceToolbox [OK]
SuperBuild - First pass
SuperBuild - First pass - done
SuperBuild - Slicer =&gt; Requires curl, CTKAppLauncherLib, teem, VTK, ITK, CTK, LibArchive, RapidJSON, SimpleITK, SlicerExecutionModel, qRestAPI, DCMTK, CTKAPPLAUNCHER, python, python-pythonqt-requirements, python-scipy, python-numpy, python-dicom-requirements, python-extension-manager-requirements, python-extension-manager-ssl-requirements, tbb, JsonCpp, 
SuperBuild -   curl =&gt; Requires zlib, OpenSSL, 
SuperBuild -     zlib[OK]
SuperBuild -     ZLIB_INCLUDE_DIR:C:/D/S4D/zlib-install/include
SuperBuild -     ZLIB_LIBRARY:C:/D/S4D/zlib-install/lib/zlib.lib
SuperBuild -     ZLIB_ROOT:C:/D/S4D/zlib-install
SuperBuild -     OpenSSL[OK]
SuperBuild -     LIB_EAY_DEBUG:C:/D/S4D/OpenSSL-install/Debug/lib/libcrypto.lib
SuperBuild -     LIB_EAY_RELEASE:C:/D/S4D/OpenSSL-install/Release/lib/libcrypto.lib
SuperBuild -     SSL_EAY_DEBUG:C:/D/S4D/OpenSSL-install/Debug/lib/libssl.lib
SuperBuild -     SSL_EAY_RELEASE:C:/D/S4D/OpenSSL-install/Release/lib/libssl.lib
SuperBuild -     OpenSSL 1.1.1g
SuperBuild -     OPENSSL_LIBRARY_DIR:C:/D/S4D/OpenSSL-install/$(Configuration)/lib
SuperBuild -     OPENSSL_EXPORT_LIBRARY_DIR:C:/D/S4D/OpenSSL-install/$(Configuration)/bin
SuperBuild -     OPENSSL_INCLUDE_DIR:C:/D/S4D/OpenSSL-install/$(Configuration)/include
SuperBuild -     OPENSSL_LIBRARIES:optimized;C:/D/S4D/OpenSSL-install/Release/lib/libssl.lib;debug;C:/D/S4D/OpenSSL-install/Debug/lib/libssl.lib;optimized;C:/D/S4D/OpenSSL-install/Release/lib/libcrypto.lib;debug;C:/D/S4D/OpenSSL-install/Debug/lib/libcrypto.lib
SuperBuild -   curl[OK]
SuperBuild -   CURL_INCLUDE_DIR:C:/D/S4D/curl-install/include
SuperBuild -   CURL_LIBRARY:C:/D/S4D/curl-install/lib/libcurl.lib
SuperBuild -   CTKAppLauncherLib[OK]
SuperBuild -   teem =&gt; Requires zlib[INCLUDED], VTK, 
SuperBuild -     VTK =&gt; Requires zlib[INCLUDED], python, tbb, 
SuperBuild -       python =&gt; Requires bzip2, CTKAPPLAUNCHER, LibFFI, LZMA, zlib[INCLUDED], sqlite, OpenSSL[INCLUDED], 
SuperBuild -         bzip2[OK]
SuperBuild -         BZIP2_INCLUDE_DIR:C:/D/S4D/bzip2
SuperBuild -         BZIP2_LIBRARIES:C:/D/S4D/bzip2-install/lib/libbz2.lib
SuperBuild -         CTKAPPLAUNCHER =&gt; Requires CTKResEdit, 
SuperBuild -           CTKResEdit[OK]
SuperBuild -         CTKAPPLAUNCHER[OK]
SuperBuild -         LibFFI[OK]
SuperBuild -         LibFFI_INCLUDE_DIR:C:/D/S4D/LibFFI-install/include
SuperBuild -         LibFFI_LIBRARY:C:/D/S4D/LibFFI-install/lib/ffi_static.lib
SuperBuild -         LZMA[OK]
SuperBuild -         sqlite[OK]
SuperBuild -       python[OK]
SuperBuild -       PYTHON_EXECUTABLE:C:/D/S4D/python-install/bin/PythonSlicer.exe
SuperBuild -       PYTHON_INCLUDE_DIR:C:/D/S4D/python-install/include
SuperBuild -       PYTHON_LIBRARY:C:/D/S4D/python-install/libs/python39.lib
SuperBuild -       PYTHON_DEBUG_LIBRARY:C:/D/S4D/python-install/libs/python39.lib
SuperBuild -       Python3_ROOT_DIR:C:/D/S4D/python-install
SuperBuild -       Python3_INCLUDE_DIR:C:/D/S4D/python-install/include
SuperBuild -       Python3_LIBRARY:C:/D/S4D/python-install/libs/python39.lib
SuperBuild -       Python3_LIBRARY_DEBUG:C:/D/S4D/python-install/libs/python39.lib
SuperBuild -       Python3_LIBRARY_RELEASE:C:/D/S4D/python-install/libs/python39.lib
SuperBuild -       Python3_EXECUTABLE:C:/D/S4D/python-install/bin/PythonSlicer.exe
SuperBuild -       tbb[OK]
SuperBuild -       TBB_DIR:C:/D/S4D/tbb-install/tbb2019_20191006oss/cmake
SuperBuild -     VTK[OK]
SuperBuild -   teem[OK]
SuperBuild -   ITK =&gt; Requires zlib[INCLUDED], VTK[INCLUDED], DCMTK, tbb[INCLUDED], 
SuperBuild -     DCMTK =&gt; Requires zlib[INCLUDED], 
SuperBuild -     DCMTK[OK]
SuperBuild -   ITK[OK]
SuperBuild -   CTK =&gt; Requires VTK[INCLUDED], ITK[INCLUDED], python[INCLUDED], DCMTK[INCLUDED], 
SuperBuild -   CTK[OK]
SuperBuild -   LibArchive =&gt; Requires zlib[INCLUDED], zlib[INCLUDED], 
SuperBuild -   LibArchive[OK]
SuperBuild -   RapidJSON[OK]
SuperBuild -   SimpleITK =&gt; Requires ITK[INCLUDED], Swig[INCLUDED], python[INCLUDED], python-setuptools, 
SuperBuild -     python-setuptools =&gt; Requires python[INCLUDED], python-ensurepip, 
SuperBuild -       python-ensurepip =&gt; Requires python[INCLUDED], 
SuperBuild -       python-ensurepip[OK]
SuperBuild -     python-setuptools[OK]
SuperBuild -   SimpleITK[OK]
SuperBuild -   SlicerExecutionModel =&gt; Requires ITK[INCLUDED], tbb[INCLUDED], 
SuperBuild -   SlicerExecutionModel[OK]
SuperBuild -   qRestAPI[OK]
SuperBuild -   python-pythonqt-requirements =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-pip, python-setuptools[INCLUDED], python-wheel, 
SuperBuild -     python-pip =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -     python-pip[OK]
SuperBuild -     python-wheel =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -     python-wheel[OK]
SuperBuild -   python-pythonqt-requirements[OK]
SuperBuild -   python-scipy =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-numpy, python-pip[INCLUDED], python-setuptools[INCLUDED], python-wheel[INCLUDED], 
SuperBuild -     python-numpy =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -     python-numpy[OK]
SuperBuild -   python-scipy[OK]
SuperBuild -   python-dicom-requirements =&gt; Requires python[INCLUDED], python-numpy[INCLUDED], python-pip[INCLUDED], python-requests-requirements, python-setuptools[INCLUDED], 
SuperBuild -     python-requests-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -     python-requests-requirements[OK]
SuperBuild -   python-dicom-requirements[OK]
SuperBuild -   python-extension-manager-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -   python-extension-manager-requirements[OK]
SuperBuild -   python-extension-manager-ssl-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-requests-requirements[INCLUDED], python-setuptools[INCLUDED], 
SuperBuild -   python-extension-manager-ssl-requirements[OK]
SuperBuild -   JsonCpp[OK]
SuperBuild - Slicer[OK]
Configuring done
Generating done
</code></pre>
<p>For SlicerVR build,</p>
<pre><code class="lang-auto">Selecting Windows SDK version 10.0.22000.0 to target Windows 10.0.19044.
CMake Error at CMakeLists.txt:20 (find_package):
  By not providing "FindSlicer.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Slicer", but
  CMake did not find one.

  Could not find a package configuration file provided by "Slicer" with any
  of the following names:

    SlicerConfig.cmake
    slicer-config.cmake

  Add the installation prefix of "Slicer" to CMAKE_PREFIX_PATH or set
  "Slicer_DIR" to a directory containing one of the above files.  If "Slicer"
  provides a separate development package or SDK, be sure it has been
  installed.


Configuring incomplete, errors occurred!
See also "C:/Users/Li/Downloads/SlicerVR_install/CMakeFiles/CMakeOutput.log".
</code></pre>
<p>and the output log is,</p>
<pre><code class="lang-auto">The system is: Windows - 10.0.19044 - AMD64
Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
Compiler:  
Build flags: /DWIN32;/D_WINDOWS;/W3
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 19/2/2022 10:47:04 PM.
Project "C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdC\CompilerIdC.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdC.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /external:W0 /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
  CompilerIdC.vcxproj -&gt; C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdC\CompilerIdC.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_C_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_C_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdC.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate".
Done Building Project "C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdC\CompilerIdC.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.25


Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.exe"

Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.vcxproj"

The C compiler identification is MSVC, found in "C:/Users/Li/Downloads/SlicerVR_build/CMakeFiles/3.23.0-rc1/CompilerIdC/CompilerIdC.exe"

Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
Compiler:  
Build flags: /DWIN32;/D_WINDOWS;/W3;/GR;/EHsc
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 19/2/2022 10:47:06 PM.
Project "C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdCXX\CompilerIdCXX.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc142.pdb" /external:W0 /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
  CompilerIdCXX.vcxproj -&gt; C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdCXX\CompilerIdCXX.exe
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_CXX_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_CXX_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdCXX.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate".
Done Building Project "C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\3.23.0-rc1\CompilerIdCXX\CompilerIdCXX.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.12


Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.exe"

Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.vcxproj"

The CXX compiler identification is MSVC, found in "C:/Users/Li/Downloads/SlicerVR_build/CMakeFiles/3.23.0-rc1/CompilerIdCXX/CompilerIdCXX.exe"

Detecting C compiler ABI info compiled with the following output:
Change Dir: C:/Users/Li/Downloads/SlicerVR_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f3013.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30140 for x64

  Copyright (C) Microsoft Corporation.  ?????,????????

  CMakeCCompilerABI.c

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_f3013.dir\Debug\\" /Fd"cmTC_f3013.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue "C:\Users\Li\Downloads\cmake-3.23.0-rc1-windows-x86_64\share\cmake-3.23\Modules\CMakeCCompilerABI.c"

  cmTC_f3013.vcxproj -&gt; C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\CMakeTmp\Debug\cmTC_f3013.exe




Detecting CXX compiler ABI info compiled with the following output:
Change Dir: C:/Users/Li/Downloads/SlicerVR_build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_93c2b.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30140 for x64

  Copyright (C) Microsoft Corporation.  ?????,????????

  CMakeCXXCompilerABI.cpp

  cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_93c2b.dir\Debug\\" /Fd"cmTC_93c2b.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue "C:\Users\Li\Downloads\cmake-3.23.0-rc1-windows-x86_64\share\cmake-3.23\Modules\CMakeCXXCompilerABI.cpp"

  cmTC_93c2b.vcxproj -&gt; C:\Users\Li\Downloads\SlicerVR_build\CMakeFiles\CMakeTmp\Debug\cmTC_93c2b.exe

</code></pre>

---

## Post #4 by @user5 (2022-02-20 11:37 UTC)

<p>It is the Slicer build’ s CMakeOutput log,</p>
<blockquote>
<p><a href="https://drive.google.com/file/d/1JFn98U8p-Xc4ePQhYxs--z0Tm0-mDw4E/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">CMakeOutput.log - Google Drive</a></p>
</blockquote>
<p>It is the SlicerVR’ s CMakeOutput log,</p>
<blockquote>
<p><a href="https://drive.google.com/file/d/1CpPbvMBol6rhfMiYbUxoGRSxTV_K3wTM/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">CMakeOutput (1).log - Google Drive</a></p>
</blockquote>

---

## Post #5 by @user5 (2022-02-21 06:02 UTC)

<p>The SlicerConfig.cmake problem have been fixed.<br>
CMake build the SlicerVR 's inner build folder successfully, but it still has some error in building the ALL_BUILD project.</p>
<p>It is the error,</p>
<pre><code class="lang-auto">Error	
Code:MSB8066	
Description: Custom build for 'C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-configure.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-build.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\vtkRenderingOpenVR-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\vtkRenderingOpenVR.rule' exited with code 1.	
Project: vtkRenderingOpenVR	
File: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	
Line: 241	

</code></pre>
<pre><code class="lang-auto">
Error	
Code: MSB8066	
Description: Custom build for 'C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-configure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-build.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-forceconfigure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\inner-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\inner.rule' exited with code 1.	
Project: inner	
File: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	
Line: 241	

</code></pre>
<p>I would like to ask that how to fix this error?</p>

---

## Post #6 by @user5 (2022-02-21 09:50 UTC)

<p>The SlicerConfig.cmake problem have been fixed.<br>
CMake build the SlicerVR 's inner build folder successfully, but it still has some error in building the ALL_BUILD project.<br>
If I use Slicer v4.11 in github to build, then It comes out those error,</p>
<pre><code class="lang-auto">Error	
Code:MSB8066	
Description: Custom build for 'C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-configure.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-build.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\vtkRenderingOpenVR-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\vtkRenderingOpenVR.rule' exited with code 1.	
Project: vtkRenderingOpenVR	
File: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	
Line: 241	

</code></pre>
<pre><code class="lang-auto">
Error	
Code: MSB8066	
Description: Custom build for 'C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-configure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-build.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-forceconfigure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\inner-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\inner.rule' exited with code 1.	
Project: inner	
File: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	
Line: 241	

</code></pre>
<p>It is the Output message,</p>
<pre><code class="lang-auto">Build started...
1&gt;------ Build started: Project: OpenVR, Configuration: Debug x64 ------
2&gt;------ Build started: Project: vtkRenderingOpenVR, Configuration: Debug x64 ------
2&gt;Performing configure step for 'vtkRenderingOpenVR'
2&gt;loading initial cache file C:/D/S4R/VR/vtkRenderingOpenVR-prefix/tmp/vtkRenderingOpenVR-cache-Debug.cmake
2&gt;-- Setting VTK_MODULE_SOURCE_DIR to C:/D/S4R/test/VTK-build/../VTK/Rendering/OpenVR
2&gt;-- Setting VTK_MODULE_NAME to RenderingOpenVR
2&gt;-- Setting VTK_MODULE_CMAKE_MODULE_PATH to C:/D/S4R/test/VTK-build/../VTK/CMake
2&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19044.
2&gt;CMake Error at CMakeLists.txt:28 (message):
2&gt;  VTK 8.90 or later is required.
2&gt;
2&gt;
2&gt;-- Configuring incomplete, errors occurred!
2&gt;See also "C:/D/S4R/VR/vtkRenderingOpenVR-build/CMakeFiles/CMakeOutput.log".
2&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-configure.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-build.rule;C:\D\S4R\VR\CMakeFiles\b2722ca355788db1cf50ea3d3b39227b\vtkRenderingOpenVR-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\vtkRenderingOpenVR-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\vtkRenderingOpenVR.rule' exited with code 1.
2&gt;Done building project "vtkRenderingOpenVR.vcxproj" -- FAILED.
3&gt;------ Build started: Project: inner, Configuration: Debug x64 ------
3&gt;Performing configure step for 'inner'
3&gt;loading initial cache file C:/D/S4R/VR/inner-prefix/tmp/inner-cache-Debug.cmake
3&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19044.
3&gt;-- Found PythonLibs: C:/D/S4R/test/python-install/libs/python36.lib (found version "3.6.7")
3&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
3&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
3&gt;-- RapidJSON found. Headers: ./include/Slicer-4.11
3&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
3&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
3&gt;-- Found PythonLibs: C:/D/S4R/test/python-install/libs/python36.lib
3&gt;-- Configuring SlicerVirtualReality with Qt 5.15.2 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )
3&gt;-- Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins
3&gt;-- Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin
3&gt;-- Checking EXTENSION_NAME variable
3&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED
3&gt;-- Checking MODULE_NAME variable
3&gt;-- Checking MODULE_NAME variable - NOTDEFINED
3&gt;-- Checking PROJECT_NAME variable
3&gt;-- Checking PROJECT_NAME variable - SlicerVirtualReality
3&gt;-- Setting EXTENSION_NAME ......................: SlicerVirtualReality
3&gt;-- Adding ConfigureAdditionalLauncherSettings target
3&gt;-- Adding ConfigureAdditionalLauncherSettings target - yes (because configuring inner-build)
3&gt;-- Setting EXTENSION_SOURCE_DIR ................: C:/D/S4/SlicerVirtualReality
3&gt;-- Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: C:/D/S4R/VR
3&gt;-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: inner-build
3&gt;-- Setting MIDAS_PACKAGE_URL ...................: http://slicer.kitware.com/midas3
3&gt;-- Setting MIDAS_PACKAGE_EMAIL .................: OBFUSCATED
3&gt;-- Setting MIDAS_PACKAGE_API_KEY ...............: OBFUSCATED
3&gt;-- Setting EXTENSION_SVNUSERNAME ...............: NOT DEFINED
3&gt;-- Setting EXTENSION_SVNPASSWORD ...............: NOT DEFINED
3&gt;-- Setting EXTENSION_DEPENDS ...................: NA
3&gt;-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: inner-build
3&gt;-- Setting EXTENSION_HOMEPAGE ..................: https://github.com/KitwareMedical/SlicerVirtualReality
3&gt;-- Setting EXTENSION_CONTRIBUTORS ..............: Jean-Baptiste Vimort (Kitware), Jean-Christophe Fillion-Robin (Kitware),  [...]
3&gt;-- Setting EXTENSION_CATEGORY ..................: Virtual Reality
3&gt;-- Setting EXTENSION_ICONURL ...................: https://raw.githubusercontent.com/KitwareMedical/SlicerVirtualReality/mas [...]
3&gt;-- Setting EXTENSION_DESCRIPTION ...............: Allows user to interact with a Slicer scene using virtual reality.
3&gt;-- Setting EXTENSION_SCREENSHOTURLS ............: https://www.slicer.org/w/images/4/49/SlicerVirtualReality_Screenshot1.png [...]
3&gt;-- Setting EXTENSION_ENABLED ...................: 1
3&gt;-- Setting EXTENSION_STATUS ....................: NOT DEFINED
3&gt;-- Setting default for EXTENSION_STATUS ........:
3&gt;-- Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE)
3&gt;CMake Error at VirtualReality/CMakeLists.txt:9 (find_package):
3&gt;  By not providing "FindvtkRenderingOpenVR.cmake" in CMAKE_MODULE_PATH this
3&gt;  project has asked CMake to find a package configuration file provided by
3&gt;  "vtkRenderingOpenVR", but CMake did not find one.
3&gt;
3&gt;  Could not find a package configuration file provided by
3&gt;  "vtkRenderingOpenVR" with any of the following names:
3&gt;
3&gt;    vtkRenderingOpenVRConfig.cmake
3&gt;    vtkrenderingopenvr-config.cmake
3&gt;
3&gt;  Add the installation prefix of "vtkRenderingOpenVR" to CMAKE_PREFIX_PATH or
3&gt;  set "vtkRenderingOpenVR_DIR" to a directory containing one of the above
3&gt;  files.  If "vtkRenderingOpenVR" provides a separate development package or
3&gt;  SDK, be sure it has been installed.
3&gt;
3&gt;
3&gt;-- Configuring incomplete, errors occurred!
3&gt;See also "C:/D/S4R/VR/inner-build/CMakeFiles/CMakeOutput.log".
3&gt;See also "C:/D/S4R/VR/inner-build/CMakeFiles/CMakeError.log".
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-configure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-build.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-forceconfigure.rule;C:\D\S4R\VR\CMakeFiles\0a0467f3e4411c40b9f5b422b63b034f\inner-install.rule;C:\D\S4R\VR\CMakeFiles\37e6f1e566e55713f40213b1e0af2a1c\inner-complete.rule;C:\D\S4R\VR\CMakeFiles\229cd6aac049427fbd82d93ebcce8543\inner.rule' exited with code 1.
3&gt;Done building project "inner.vcxproj" -- FAILED.
========== Build: 1 succeeded, 2 failed, 2 up-to-date, 0 skipped ==========
</code></pre>
<p>If I use the Slicer-master version in github,  then It comes out those error,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69463a7640de92d4855937a37c1a856147edbeb1.png" data-download-href="/uploads/short-url/f1iB4DddE3WFhZQ7d7huBonSFt7.png?dl=1" title="error-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69463a7640de92d4855937a37c1a856147edbeb1_2_690x225.png" alt="error-1" data-base62-sha1="f1iB4DddE3WFhZQ7d7huBonSFt7" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69463a7640de92d4855937a37c1a856147edbeb1_2_690x225.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69463a7640de92d4855937a37c1a856147edbeb1_2_1035x337.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69463a7640de92d4855937a37c1a856147edbeb1_2_1380x450.png 2x" data-dominant-color="F0F1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error-1</span><span class="informations">2174×709 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is the Output message,</p>
<pre><code class="lang-auto">Build started...
1&gt;------ Build started: Project: OpenVR, Configuration: Debug x64 ------
2&gt;------ Build started: Project: vtkRenderingOpenVR, Configuration: Debug x64 ------
3&gt;------ Build started: Project: inner, Configuration: Debug x64 ------
3&gt;Performing build step for 'inner'
3&gt;Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
3&gt;Copyright (C) Microsoft Corporation. All rights reserved.
3&gt;
3&gt;  For vtkSlicerVirtualRealityModuleMRML - updating vtkSlicerVirtualRealityModuleMRMLHierarchy.txt
3&gt;  vtkWrapHierarchy: couldn't open file C:/Users/Li/Downloads/Slicer_build/Slicer-build/MRMLCoreHierarchy.txt
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\D\S4R\1\inner-build\CMakeFiles\2193a776a658189df6b9853d8ffe0a89\vtkSlicerVirtualRealityModuleMRMLHierarchy.stamp.txt.rule' exited with code 1. [C:\D\S4R\1\inner-build\VirtualReality\MRML\vtkSlicerVirtualRealityModuleMRML.vcxproj]
3&gt;  qSlicerSubjectHierarchyVirtualRealityPlugin.cxx
3&gt;C:\Users\Li\Downloads\VTK\Slicer-master\Libs\MRML\Core\vtkObserverManager.h(22,10): fatal error C1083: Cannot open include file: 'vtkObject.h': No such file or directory [C:\D\S4R\1\inner-build\VirtualReality\SubjectHierarchyPlugins\qSlicerVirtualRealitySubjectHierarchyPlugins.vcxproj]
3&gt;  moc_qSlicerSubjectHierarchyVirtualRealityPlugin.cpp
3&gt;C:\Users\Li\Downloads\VTK\Slicer-master\Modules\Loadable\SubjectHierarchy\Widgets\qSlicerSubjectHierarchyAbstractPlugin.h(27,10): fatal error C1083: Cannot open include file: 'QObject': No such file or directory [C:\D\S4R\1\inner-build\VirtualReality\SubjectHierarchyPlugins\qSlicerVirtualRealitySubjectHierarchyPlugins.vcxproj]
3&gt;  Generating Code...
3&gt;  For vtkSlicerVirtualRealityModuleMRML - updating vtkSlicerVirtualRealityModuleMRMLHierarchy.txt
3&gt;  vtkWrapHierarchy: couldn't open file C:/Users/Li/Downloads/Slicer_build/Slicer-build/MRMLCoreHierarchy.txt
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\D\S4R\1\inner-build\CMakeFiles\2193a776a658189df6b9853d8ffe0a89\vtkSlicerVirtualRealityModuleMRMLHierarchy.stamp.txt.rule;C:\D\S4R\1\inner-build\CMakeFiles\d22f570a736261136b69e35b8fbe20cc\vtkSlicerVirtualRealityModuleMRMLHierarchy.rule' exited with code 1. [C:\D\S4R\1\inner-build\VirtualReality\MRML\vtkSlicerVirtualRealityModuleMRMLHierarchy.vcxproj]
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\D\S4R\1\CMakeFiles\ff4a336c0290a25a9e1f5a5e8961d6ea\inner-build.rule;C:\D\S4R\1\CMakeFiles\ff4a336c0290a25a9e1f5a5e8961d6ea\inner-forceconfigure.rule;C:\D\S4R\1\CMakeFiles\ff4a336c0290a25a9e1f5a5e8961d6ea\inner-install.rule;C:\D\S4R\1\CMakeFiles\5bd184956054e086aea34c80e30e37e4\inner-complete.rule;C:\D\S4R\1\CMakeFiles\b30dbca8c923171daf99bd56b0af22da\inner.rule' exited with code 1.
3&gt;Done building project "inner.vcxproj" -- FAILED.
========== Build: 2 succeeded, 1 failed, 2 up-to-date, 0 skipped ==========
</code></pre>
<p>I would like to ask that how to fix those error? I have no idea to fix it after I tried different method in internet.</p>

---

## Post #7 by @jcfr (2022-02-21 15:26 UTC)

<p>We are in the process of finalizing the update of VTK and also fixing the SlicerVirtualReality extension to account for these changes.</p>
<p>This should be completed in the next few days. Once completed, I suggest you give another try.</p>
<p>References:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/5978" class="inline-onebox">ENH: Update VTK9 from 9.0.20201111 to 9.1.20220125 by jadh4v · Pull Request #5978 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/89" class="inline-onebox">COMP: Attempt to fix build including vtkRenderingVR WIP by cpinter · Pull Request #89 · KitwareMedical/SlicerVirtualReality · GitHub</a></li>
<li><a href="https://discourse.slicer.org/t/transition-of-nightly-build-from-vtk-9-0-20201111-to-9-1-20220125/21669" class="inline-onebox">Transition of nightly build from VTK 9.0.20201111 to 9.1.20220125</a></li>
</ul>

---

## Post #8 by @user5 (2022-02-21 17:24 UTC)

<p>So it will be fine, if I change the VTK to other version, such as VTK8. Am I right?</p>

---

## Post #9 by @lassoan (2022-03-15 03:40 UTC)

<p>I see a build error on the dashboard - <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2626242" class="inline-onebox">CDash</a></p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Do you know about this error? Can you build SlicerVirtualReality with latest Slicer master version?</p>

---

## Post #10 by @cpinter (2022-03-16 16:01 UTC)

<p>The latest master does not work. We need to integrate this PR</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerVirtualReality</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90" target="_blank" rel="noopener">Update integration to support VTK 9.1</a>
    </h4>

    <div class="branches">
      <code>KitwareMedical:master</code> ← <code>jcfr:fix-build-against-vtk-9.1.20211022</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-26" data-time="10:40:30" data-timezone="UTC">10:40AM - 26 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="9 commits changed 27 files with 525 additions and 169 deletions">
        <a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90/files" target="_blank" rel="noopener">
          <span class="added">+525</span>
          <span class="removed">-169</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In addition of the API changes documented below, this commit also updates
`vtkV<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">irtualRealityViewInteractor` to allow retrieving the last tracked device
position stored in the array `vtkOpenVRRenderWindowInteractor::Trackers`.

The `Trackers` array contains `TrackerActions` each being a struct with
two entries:
- `Source` of type `vr::VRInputValueHandle_t`
- `LastPose` of type `vr::TrackedDevicePose_t`


Obsolete branches
-----------------

| branch | Notes |
|--|--|
| [cpinter@slicervr-vtkrenderingvr-build](https://github.com/cpinter/SlicerVirtualReality/tree/slicervr-vtkrenderingvr-build) | **Remove**, change integrated in this PR (#90) |
| [cpinter@fix-build-against-vtk-9.1.20211022](https://github.com/cpinter/SlicerVirtualReality/tree/fix-build-against-vtk-9.1.20211022) | **Remove**, change integrated in this PR (#90) |
| [cpinter@gui-widgets-module](https://github.com/cpinter/SlicerVirtualReality/tree/gui-widgets-module) | **Remove**, change integrated in this new branch: [jcfr@fix-build-against-vtk-9.1.20211022-with-gui-widgets-module](https://github.com/jcfr/SlicerVirtualReality/compare/fix-build-against-vtk-9.1.20211022...fix-build-against-vtk-9.1.20211022-with-gui-widgets-module) |


Remaining issues
----------------

### (1) Retrieval of last position associated with generic tracker

Retrieval of last position associated with generic tracker in
`vtkVirtualRealityViewInteractor::GetTrackedDevicePose` given
the index is not possible.

**:warning: TODO**: Handle retrieval of tracker position associated with generic tracker associated with index.

Background:

Add support for generic tracker originally contributed in these commits:
* kitware/VTK@6083532cf8 (ENH: Exposing the generic tracker openvr device type to downstream projects)
* KitwareMedical/SlicerVirtualReality@59b7d1bf3 (Adding interface and logic to maintain MRML transforms for each generic VR tracker)

but removed following the refactoring done in these commits:

* kitware/VTK@1aac3fe5f (Create VRInteractorStyle and VRRenderWindowInteractor)
* kitware/VTK@af0fab486 (Clean up VR and OpenVR classes)
* kitware/VTK@9bd64d666 (Cleanup and rework of the VRInteractorStyle and subclasses)
* kitware/VTK@09a478a22 (Cleanup VR camera code and subclasses)


### (2) RecognizeComplexGesture is not virtual  anymore in base VTK class

**:warning: TODO**: Assess with this function should still be overriden with VTK 9.1

Background: The function became non virtual in Kitware/VTK@af0fab486 (Clean up VR and OpenVR classes)


API changes
-----------

vtkEventData API changes:
* vtkEventDataButton3D -&gt; vtkEventDataDevice3D

RenderWindow API changes
* GetNumberOfTrackedDevicesForDevice -&gt; GetNumberOfDeviceHandlesForDevice
* GetTrackedDeviceIndexForDevice -&gt; GetDeviceHandleForDevice
* GetTrackedDeviceModel -&gt; GetModelForDevice
* GetTrackedDeviceIndexForDevice -&gt; GetDeviceHandleForDevice

InteractorStyle API changes
* PositionProp sinature updated to include "lwpos" and "lwori"</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I had the strangest problems on Windows 11 and <a class="mention" href="/u/dgmato">@dgmato</a> had other problems on his machine that he didn’t have with the previous VTK (the action manifest issue shown in the PR comments, that since then I had too). I want to reinstall the computer and try again, but I simply haven’t found the time yet.</p>

---
