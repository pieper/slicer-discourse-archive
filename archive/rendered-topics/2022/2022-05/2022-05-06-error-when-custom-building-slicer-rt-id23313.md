# Error when custom building Slicer RT

**Topic ID**: 23313
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/error-when-custom-building-slicer-rt/23313

---

## Post #1 by @cay18 (2022-05-06 16:39 UTC)

<p>Hello, I managed to build Slicer from Source and am trying to do the same for SlicerRT to use it as an extension. I followed the instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" rel="noopener nofollow ugc">here</a> and successfully generated the project using CMake-GUI. But when I try to build the project in VS, I get this error:</p>
<p><code>fatal error C1083: Cannot open include file: 'pthread.h'</code></p>
<p>I have tried the following but the same error still persists:<br>
(1) Shorten directory paths<br>
(2) Installing pthreads NuGet Package<br>
(3) Using vcpkg to install pthreads for Windows</p>
<p>Can someone help me find a solution please? Thank you very much. I am using VS 2017, CMake ver 3.23 and Qt 5.15.2</p>

---

## Post #2 by @cay18 (2022-05-06 16:42 UTC)

<p>CMake Error Log:</p>
<pre><code class="lang-auto">Determining if the include file pthread.h exists failed with the following output:
Change Dir: C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe cmTC_e8a74.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=15.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.16.27045 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  

  cl /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /Zi /W2 /WX- /diagnostics:classic /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_e8a74.dir\Debug\\" /Fd"cmTC_e8a74.dir\Debug\vc141.pdb" /Gd /TC /errorReport:queue "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\CheckIncludeFile.c"

  CheckIncludeFile.c

  

C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'pthread.h': No such file or directory [C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\cmTC_e8a74.vcxproj]




Determining if the CXX compiler accepts the flag -features=no%anachronisms passed with the following output:
Change Dir: C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe cmTC_69608.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=15.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.16.27045 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  

  cl /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /Zi /W2 /WX- /diagnostics:classic /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_69608.dir\Debug\\" /Fd"cmTC_69608.dir\Debug\vc141.pdb" /Gd /TP /errorReport:queue  /bigobj -features=no%%anachronisms "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\src.cxx"

  src.cxx

  

cl : Command line warning D9002: ignoring unknown option '-features=no%%anachronisms' [C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\cmTC_69608.vcxproj]

  cmTC_69608.vcxproj -&gt; C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\Debug\cmTC_69608.exe



Source file was:
int main() { return 0;}
</code></pre>
<p>CMake Output Log:</p>
<pre><code class="lang-auto">The system is: Windows - 10.0.19043 - AMD64
Compiling the C compiler identification source file "CMakeCCompilerId.c" succeeded.
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe 
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 06/05/2022 13:38:03.
Project "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\CompilerIdC.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdC.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdC.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
VcpkgTripletSelection:
  Using triplet "x64-windows" from "C:\Users\CAY\vcpkg\installed\x64-windows\"
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\CL.exe /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /nologo /W0 /WX- /diagnostics:classic /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc141.pdb" /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c
  CMakeCCompilerId.c
Link:
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO /LIBPATH:"C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib" /LIBPATH:"C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib\manual-link" kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib "C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib\*.lib" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj
  CompilerIdC.vcxproj -&gt; C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\.\CompilerIdC.exe
AppLocalFromInstalled:
  pwsh.exe -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\.\CompilerIdC.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdC.tlog\CompilerIdC.write.1u.tlog" "Debug\vcpkg.applocal.log"
  'pwsh.exe' is not recognized as an internal or external command,
  operable program or batch file.
  The command "pwsh.exe -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\.\CompilerIdC.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdC.tlog\CompilerIdC.write.1u.tlog" "Debug\vcpkg.applocal.log"" exited with code 9009.
  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\.\CompilerIdC.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdC.tlog\CompilerIdC.write.1u.tlog" "Debug\vcpkg.applocal.log"
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_C_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_C_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\Hostx86\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdC.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate".
Done Building Project "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdC\CompilerIdC.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.03


Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.exe"

Compilation of the C compiler identification source "CMakeCCompilerId.c" produced "CompilerIdC.vcxproj"

The C compiler identification is MSVC, found in "C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/3.23.0-rc2/CompilerIdC/CompilerIdC.exe"

Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" succeeded.
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe 
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;/GR;/EHsc;
Id flags:  

The output was:
0
Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 06/05/2022 13:38:04.
Project "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\CompilerIdCXX.vcxproj" on node 1 (default targets).
PrepareForBuild:
  Creating directory "Debug\".
  Creating directory "Debug\CompilerIdCXX.tlog\".
InitializeBuildStatus:
  Creating "Debug\CompilerIdCXX.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
VcpkgTripletSelection:
  Using triplet "x64-windows" from "C:\Users\CAY\vcpkg\installed\x64-windows\"
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\CL.exe /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /nologo /W0 /WX- /diagnostics:classic /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\\" /Fd"Debug\vc141.pdb" /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp
  CMakeCXXCompilerId.cpp
Link:
  C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO /LIBPATH:"C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib" /LIBPATH:"C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib\manual-link" kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib "C:\Users\CAY\vcpkg\installed\x64-windows\debug\lib\*.lib" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj
  CompilerIdCXX.vcxproj -&gt; C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\.\CompilerIdCXX.exe
AppLocalFromInstalled:
  pwsh.exe -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\.\CompilerIdCXX.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdCXX.tlog\CompilerIdCXX.write.1u.tlog" "Debug\vcpkg.applocal.log"
  'pwsh.exe' is not recognized as an internal or external command,
  operable program or batch file.
  The command "pwsh.exe -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\.\CompilerIdCXX.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdCXX.tlog\CompilerIdCXX.write.1u.tlog" "Debug\vcpkg.applocal.log"" exited with code 9009.
  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy Bypass -noprofile -File "C:\Users\CAY\vcpkg\scripts\buildsystems\msbuild\applocal.ps1" "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\.\CompilerIdCXX.exe" "C:\Users\CAY\vcpkg\installed\x64-windows\debug\bin" "Debug\CompilerIdCXX.tlog\CompilerIdCXX.write.1u.tlog" "Debug\vcpkg.applocal.log"
PostBuildEvent:
  for %%i in (cl.exe) do @echo CMAKE_CXX_COMPILER=%%~$PATH:i
  :VCEnd
  CMAKE_CXX_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\Hostx86\x64\cl.exe
FinalizeBuildStatus:
  Deleting file "Debug\CompilerIdCXX.tlog\unsuccessfulbuild".
  Touching "Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate".
Done Building Project "C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\3.23.0-rc2\CompilerIdCXX\CompilerIdCXX.vcxproj" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:01.20


Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.exe"

Compilation of the CXX compiler identification source "CMakeCXXCompilerId.cpp" produced "CompilerIdCXX.vcxproj"

The CXX compiler identification is MSVC, found in "C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/3.23.0-rc2/CompilerIdCXX/CompilerIdCXX.exe"

Detecting C compiler ABI info compiled with the following output:
Change Dir: C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe cmTC_bd3f1.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=15.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.16.27045 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  

  cl /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /Zi /W2 /WX- /diagnostics:classic /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_bd3f1.dir\Debug\\" /Fd"cmTC_bd3f1.dir\Debug\vc141.pdb" /Gd /TC /errorReport:queue "C:\Work\cmake-3.23.0-rc2-windows-x86_64\share\cmake-3.23\Modules\CMakeCCompilerABI.c"

  CMakeCCompilerABI.c

  

  cmTC_bd3f1.vcxproj -&gt; C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\Debug\cmTC_bd3f1.exe




Detecting CXX compiler ABI info compiled with the following output:
Change Dir: C:/D/S4D/Slicer-build/r/inner-build/CMakeFiles/CMakeTmp

Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/MSBuild/15.0/Bin/MSBuild.exe cmTC_43155.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=15.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 15.9.21+g9802d43bc3 for .NET Framework

Copyright (C) Microsoft Corporation. All rights reserved.



  Microsoft (R) C/C++ Optimizing Compiler Version 19.16.27045 for x64

  Copyright (C) Microsoft Corporation.  All rights reserved.

  

  cl /c /I"C:\Users\CAY\vcpkg\installed\x64-windows\include" /Zi /W2 /WX- /diagnostics:classic /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D "CMAKE_INTDIR=\"Debug\"" /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_43155.dir\Debug\\" /Fd"cmTC_43155.dir\Debug\vc141.pdb" /Gd /TP /errorReport:queue "C:\Work\cmake-3.23.0-rc2-windows-x86_64\share\cmake-3.23\Modules\CMakeCXXCompilerABI.cpp"

  CMakeCXXCompilerABI.cpp

  

  cmTC_43155.vcxproj -&gt; C:\D\S4D\Slicer-build\r\inner-build\CMakeFiles\CMakeTmp\Debug\cmTC_43155.exe
</code></pre>

---

## Post #3 by @lassoan (2022-05-12 02:40 UTC)

<p><code>pthread</code> is not needed. What you see is a try-compile check for detecting if <code>pthread</code> is present or not. Do not install pthread, it is not expected to be present on Windows.</p>
<p>If CMake configuration and generation was successful then CMake logs are not relevant anymore. Instead, build the SlicerRT.sln project and see what errors are shown in Visual Studio. If you get any build error then open the corresponding .sln file in Visual Studio and build that to see the actual error message. Make sure you build SlicerRT in the same build mode (Debug, Release, RelWithDebInfo, MinSizeRel) as you used for building Slicer.</p>

---
