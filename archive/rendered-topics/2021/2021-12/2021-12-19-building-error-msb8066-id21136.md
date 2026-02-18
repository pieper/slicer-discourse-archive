# Building Error MSB8066

**Topic ID**: 21136
**Date**: 2021-12-19
**URL**: https://discourse.slicer.org/t/building-error-msb8066/21136

---

## Post #1 by @siqueirl (2021-12-19 20:11 UTC)

<p>Hello everyone, I am trying to build slicer, but I am receiving the following error:</p>
<p>|Error|MSB8066|Custom build for ‘C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-mkdir.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-download.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-update.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-patch.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-configure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-build.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-forceconfigure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\Slicer-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\Slicer.rule;C:\D\S4\CMakeLists.txt’ exited with code 1.|Slicer|C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets|241||</p>
<p>I have seen answers regarding connection issues, and I have disabled my firewall, but the problem persists. Has anyone been able to solve this issue? Thank you!</p>

---

## Post #2 by @Sam_Horvath (2021-12-20 14:02 UTC)

<p>Could you provide the build output log in addition to just the error?</p>

---

## Post #3 by @siqueirl (2021-12-20 18:52 UTC)

<p>Thank you, here it is:</p>
<blockquote>
<p>Blockquote<br>
The system is: Windows - 10.0.19043 - AMD64<br>
Compiling the C compiler identification source file “CMakeCCompilerId.c” succeeded.<br>
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe<br>
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;<br>
Id flags:</p>
</blockquote>
<p>The output was:<br>
0<br>
Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework<br>
Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Build started 12/19/2021 7:00:48 PM.<br>
Project “C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdC\CompilerIdC.vcxproj” on node 1 (default targets).<br>
PrepareForBuild:<br>
Creating directory “Debug".<br>
Creating directory “Debug\CompilerIdC.tlog".<br>
InitializeBuildStatus:<br>
Creating “Debug\CompilerIdC.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.<br>
ClCompile:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\” /Fd"Debug\vc142.pdb” /external:W0 /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c<br>
CMakeCCompilerId.c<br>
Link:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:“.\CompilerIdC.exe” /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:“level=‘asInvoker’ uiAccess=‘false’” /manifest:embed /PDB:“.\CompilerIdC.pdb” /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:“.\CompilerIdC.lib” /MACHINE:X64 Debug\CMakeCCompilerId.obj<br>
CompilerIdC.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdC\CompilerIdC.exe<br>
PostBuildEvent:<br>
for %%i in (cl.exe) do <span class="mention">@echo</span> CMAKE_C_COMPILER=%%~$PATH:i<br>
:VCEnd<br>
CMAKE_C_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe<br>
FinalizeBuildStatus:<br>
Deleting file “Debug\CompilerIdC.tlog\unsuccessfulbuild”.<br>
Touching “Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate”.<br>
Done Building Project “C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdC\CompilerIdC.vcxproj” (default targets).</p>
<p>Build succeeded.<br>
0 Warning(s)<br>
0 Error(s)</p>
<p>Time Elapsed 00:00:00.92</p>
<p>Compilation of the C compiler identification source “CMakeCCompilerId.c” produced “CompilerIdC.exe”</p>
<p>Compilation of the C compiler identification source “CMakeCCompilerId.c” produced “CompilerIdC.vcxproj”</p>
<p>The C compiler identification is MSVC, found in “C:/D/S4R/Slicer-build/CMakeFiles/3.22.1/CompilerIdC/CompilerIdC.exe”</p>
<p>Compiling the CXX compiler identification source file “CMakeCXXCompilerId.cpp” succeeded.<br>
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe<br>
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;/GR;/EHsc;<br>
Id flags:</p>
<p>The output was:<br>
0<br>
Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework<br>
Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Build started 12/19/2021 7:00:49 PM.<br>
Project “C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdCXX\CompilerIdCXX.vcxproj” on node 1 (default targets).<br>
PrepareForBuild:<br>
Creating directory “Debug".<br>
Creating directory “Debug\CompilerIdCXX.tlog".<br>
InitializeBuildStatus:<br>
Creating “Debug\CompilerIdCXX.tlog\unsuccessfulbuild” because “AlwaysCreate” was specified.<br>
ClCompile:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\” /Fd"Debug\vc142.pdb” /external:W0 /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp<br>
CMakeCXXCompilerId.cpp<br>
Link:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:“.\CompilerIdCXX.exe” /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:“level=‘asInvoker’ uiAccess=‘false’” /manifest:embed /PDB:“.\CompilerIdCXX.pdb” /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:“.\CompilerIdCXX.lib” /MACHINE:X64 Debug\CMakeCXXCompilerId.obj<br>
CompilerIdCXX.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdCXX\CompilerIdCXX.exe<br>
PostBuildEvent:<br>
for %%i in (cl.exe) do <span class="mention">@echo</span> CMAKE_CXX_COMPILER=%%~$PATH:i<br>
:VCEnd<br>
CMAKE_CXX_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe<br>
FinalizeBuildStatus:<br>
Deleting file “Debug\CompilerIdCXX.tlog\unsuccessfulbuild”.<br>
Touching “Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate”.<br>
Done Building Project “C:\D\S4R\Slicer-build\CMakeFiles\3.22.1\CompilerIdCXX\CompilerIdCXX.vcxproj” (default targets).</p>
<p>Build succeeded.<br>
0 Warning(s)<br>
0 Error(s)</p>
<p>Time Elapsed 00:00:00.82</p>
<p>Compilation of the CXX compiler identification source “CMakeCXXCompilerId.cpp” produced “CompilerIdCXX.exe”</p>
<p>Compilation of the CXX compiler identification source “CMakeCXXCompilerId.cpp” produced “CompilerIdCXX.vcxproj”</p>
<p>The CXX compiler identification is MSVC, found in “C:/D/S4R/Slicer-build/CMakeFiles/3.22.1/CompilerIdCXX/CompilerIdCXX.exe”</p>
<p>Detecting C compiler ABI info compiled with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_03075.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>CMakeCCompilerABI.c</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR="Debug"” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_03075.dir\Debug\" /Fd"cmTC_03075.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue “C:\Program Files\CMake\share\cmake-3.22\Modules\CMakeCCompilerABI.c”</p>
<p>cmTC_03075.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_03075.exe</p>
<p>Detecting CXX compiler ABI info compiled with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f7ffe.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>CMakeCXXCompilerABI.cpp</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR="Debug"” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_f7ffe.dir\Debug\" /Fd"cmTC_f7ffe.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue “C:\Program Files\CMake\share\cmake-3.22\Modules\CMakeCXXCompilerABI.cpp”</p>
<p>cmTC_f7ffe.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_f7ffe.exe</p>
<p>Determining if files stdint.h exist passed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_70df8.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>HAVE_STDINT_H.c</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR="Debug"” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_70df8.dir\Debug\" /Fd"cmTC_70df8.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CheckIncludeFiles\HAVE_STDINT_H.c”</p>
<p>cmTC_70df8.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_70df8.exe</p>
<p>Performing C SOURCE FILE Test C_HAS_WARNING-W3 succeeded with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_afd4c.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>src.c</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-W3” /D “CMAKE_INTDIR="Debug"” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_afd4c.dir\Debug\" /Fd"cmTC_afd4c.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue  /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cmTC_afd4c.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_afd4c.exe</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-W3 succeeded with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_1d894.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-W3” /D “CMAKE_INTDIR="Debug"” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_1d894.dir\Debug\" /Fd"cmTC_1d894.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_1d894.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_1d894.exe</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test have_avx_extensions_var succeeded with the following compile output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_16b6c.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D have_avx_extensions_var /D “CMAKE_INTDIR="Debug"” /Gm- /EHsc /RTC1 /MDd /GS /arch:AVX /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_16b6c.dir\Debug\" /Fd"cmTC_16b6c.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_16b6c.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_16b6c.exe</p>
<p>…and run output:</p>
<p>Return value: 1<br>
Source file was:</p>
<pre><code>#include &lt;immintrin.h&gt;
int main()
{
  __m256 a, b, c;
  const float src[8] = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f };
  float dst[8];
  a = _mm256_loadu_ps( src );
  b = _mm256_loadu_ps( src );
  c = _mm256_add_ps( a, b );
  _mm256_storeu_ps( dst, c );

  for( int i = 0; i &lt; 8; i++ ){
    if( ( src[i] + src[i] ) != dst[i] ){
      return -1;
    }
  }

  return 0;
}
</code></pre>
<p>Performing C++ SOURCE FILE Test have_avx2_extensions_var succeeded with the following compile output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_67b43.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30138 for x64</p>
<p>Copyright (C) Microsoft Corporation.  All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D have_avx2_extensions_var /D “CMAKE_INTDIR="Debug"” /Gm- /EHsc /RTC1 /MDd /GS /arch:AVX2 /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_67b43.dir\Debug\" /Fd"cmTC_67b43.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_67b43.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_67b43.exe</p>
<p>…and run output:</p>
<p>Return value: 1<br>
Source file was:</p>
<pre><code>#include &lt;immintrin.h&gt;
int main()
{
  __m256i a, b, c;
  const int src[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
  int dst[8];
  a =  _mm256_loadu_si256( (__m256i*)src );
  b =  _mm256_loadu_si256( (__m256i*)src );
  c = _mm256_add_epi32( a, b );
  _mm256_storeu_si256( (__m256i*)dst, c );

  for( int i = 0; i &lt; 8; i++ ){
    if( ( src[i] + src[i] ) != dst[i] ){
      return -1;
    }
  }

  return 0;
}
</code></pre>

---

## Post #4 by @pranjal.sahu (2022-09-30 06:00 UTC)

<p>Did you figure out the issue ?<br>
Could you please share your findings here ?</p>
<p>Thank You</p>

---

## Post #5 by @siqueirl (2022-09-30 14:22 UTC)

<p>It has been a while, so I might not remember the fix for this one problem. Back then, I was building Slicer 4.x. I am currently building 5.X with VS2022, and I no longer have issues with it. Some of the previous problems were related to the git protocol as it was failing to download the packages, so it needs to be unchecked in CMake. Check your version of Qt to see if it matches what the building guide recommends.</p>

---

## Post #6 by @2733845631 (2024-04-15 11:03 UTC)

<p>Did you figure out the issue ?</p>

---
