---
topic_id: 751
title: "Slicer Debug Mode Buid Error In 2017 07 23 Version On Window"
date: 2017-07-23
url: https://discourse.slicer.org/t/751
---

# Slicer debug-mode buid error in 2017-07-23 version on Windows due to bzip2

**Topic ID**: 751
**Date**: 2017-07-23
**URL**: https://discourse.slicer.org/t/slicer-debug-mode-buid-error-in-2017-07-23-version-on-windows-due-to-bzip2/751

---

## Post #1 by @lassoan (2017-07-23 19:06 UTC)

<p>This error now prevents all debug-mode builds on Windows, so it would be important to get a fix soon.</p>
<p>The build error is in Python, due to libbz2.lib not found in Release subdirectory. Building of this library is very similar to zlib, which works well. Probably the difference is that for zlib an install directory is created and python picks it up from there.</p>
<p>Build log (error is at the end):</p>
<pre><code>1&gt;------ Build started: Project: CTKResEdit, Configuration: Debug x64 ------
2&gt;------ Build started: Project: bzip2, Configuration: Debug x64 ------
3&gt;------ Build started: Project: tcl, Configuration: Debug x64 ------
4&gt;------ Build started: Project: OpenSSL, Configuration: Debug x64 ------
2&gt;  Performing update step for 'bzip2'
5&gt;------ Build started: Project: CTKAPPLAUNCHER, Configuration: Debug x64 ------
6&gt;------ Build started: Project: python-source, Configuration: Debug x64 ------
7&gt;------ Build started: Project: zlib, Configuration: Debug x64 ------
7&gt;  Performing update step for 'zlib'
8&gt;------ Build started: Project: JsonCpp, Configuration: Debug x64 ------
8&gt;  Performing update step for 'JsonCpp'
9&gt;------ Build started: Project: CTKAppLauncherLib, Configuration: Debug x64 ------
10&gt;------ Build started: Project: python, Configuration: Debug x64 ------
11&gt;------ Build started: Project: DCMTK, Configuration: Debug x64 ------
9&gt;  Performing update step for 'CTKAppLauncherLib'
11&gt;  Performing update step for 'DCMTK'
12&gt;------ Build started: Project: DataStore, Configuration: Debug x64 ------
12&gt;  Performing update step for 'DataStore'
13&gt;------ Build started: Project: EMSegment, Configuration: Debug x64 ------
14&gt;------ Build started: Project: LandmarkRegistration, Configuration: Debug x64 ------
13&gt;  Performing update step (SVN update) for 'EMSegment'
14&gt;  Performing update step for 'LandmarkRegistration'
13&gt;  Updating '.':
15&gt;------ Build started: Project: LibArchive, Configuration: Debug x64 ------
10&gt;  Performing update step for 'python'
15&gt;  Performing update step for 'LibArchive'
16&gt;------ Build started: Project: MultiVolumeExplorer, Configuration: Debug x64 ------
10&gt;  Performing configure step for 'python'
13&gt;  At revision 17130.
10&gt;  loading initial cache file C:/D/S4D/python-prefix/tmp/python-cache-Debug.cmake
16&gt;  Performing update step for 'MultiVolumeExplorer'
10&gt;CUSTOMBUILD : -- warning : Did not find file Compiler/MSVC-ASM
17&gt;------ Build started: Project: MultiVolumeImporter, Configuration: Debug x64 ------
10&gt;  -- SRC_DIR: C:/D/S4D/Python-2.7.13
10&gt;  -- PY_VERSION: 2.7.13
17&gt;  Performing update step for 'MultiVolumeImporter'
10&gt;  -- The system name is Windows
10&gt;  -- The system processor is AMD64
10&gt;  -- The system version is 10.0.15063
18&gt;------ Build started: Project: OpenIGTLink, Configuration: Debug x64 ------
19&gt;------ Build started: Project: RapidJSON, Configuration: Debug x64 ------
20&gt;------ Build started: Project: curl, Configuration: Debug x64 ------
21&gt;------ Build started: Project: BRAINSTools, Configuration: Debug x64 ------
22&gt;------ Build started: Project: jqPlot, Configuration: Debug x64 ------
20&gt;  Performing update step for 'curl'
21&gt;  Performing update step for 'BRAINSTools'
23&gt;------ Build started: Project: CompareVolumes, Configuration: Debug x64 ------
24&gt;------ Build started: Project: OtsuThresholdImageFilter, Configuration: Debug x64 ------
25&gt;------ Build started: Project: qRestAPI, Configuration: Debug x64 ------
23&gt;  Performing update step for 'CompareVolumes'
24&gt;  Performing update step for 'OtsuThresholdImageFilter'
25&gt;  Performing update step for 'qRestAPI'
26&gt;------ Build started: Project: OpenIGTLinkIF, Configuration: Debug x64 ------
27&gt;------ Skipped Build: Project: Experimental, Configuration: Debug x64 ------
27&gt;Project not selected to build for this solution configuration 
28&gt;------ Skipped Build: Project: RUN_TESTS, Configuration: Debug x64 ------
28&gt;Project not selected to build for this solution configuration 
26&gt;  Performing update step for 'OpenIGTLinkIF'
10&gt;  -- bdist_wininst: Generated 'Windows Installer' name is 'wininst-12.0-amd64'
10&gt;  -- bdist_wininst: Looking for executable named 'wininst-12.0-amd64.exe' in source tree
10&gt;  -- bdist_wininst: Looking for executable named 'wininst-12.0-amd64.exe' in source tree - not found
10&gt;  -- bdist_wininst: Configuring 'Windows Installer' named 'wininst-12.0-amd64'
10&gt;  -- 
10&gt;  -- The following extensions will NOT be built:
10&gt;  -- 
10&gt;  --     crypt (not set: HAVE_LIBCRYPT)
10&gt;  --     atexit (not set: IS_PY3)
10&gt;  --     _codecs (not set: IS_PY3)
10&gt;  --     faulthandler (not set: IS_PY3)
10&gt;  --     _opcode (not set: IS_PY3)
10&gt;  --     _operator (not set: IS_PY3)
10&gt;  --     _pickle (not set: IS_PY3)
10&gt;  --     _sre (not set: IS_PY3)
10&gt;  --     _stat (not set: IS_PY3)
10&gt;  --     _symtable (not set: IS_PY3)
10&gt;  --     _testbuffer (not set: IS_PY3)
10&gt;  --     _testimportmultiple (not set: IS_PY3)
10&gt;  --     _testmultiphase (not set: IS_PY3)
10&gt;  --     _tracemalloc (not set: IS_PY3)
10&gt;  --     _weakref (not set: IS_PY3)
10&gt;  --     xxlimited (not set: IS_PY3)
10&gt;  --     xxsubtype (not set: IS_PY3)
10&gt;  --     zipimport (not set: IS_PY3)
10&gt;  --     fcntl (not set: UNIX)
10&gt;  --     grp (not set: UNIX)
10&gt;  --     nis (not set: UNIX HAVE_LIBNSL)
10&gt;  --     posix (not set: UNIX)
10&gt;  --     pwd (not set: UNIX)
10&gt;  --     resource (not set: UNIX)
10&gt;  --     spwd (not set: UNIX HAVE_GETSPNAM HAVE_GETSPENT)
10&gt;  --     syslog (not set: UNIX)
10&gt;  --     termios (not set: UNIX)
10&gt;  --     errno (not set: IS_PY3 UNIX)
10&gt;  --     _posixsubprocess (not set: IS_PY3 UNIX)
10&gt;  --     _scproxy (not set: APPLE HAVE_LIBSYSTEMCONFIGURATION)
10&gt;  --     linuxaudiodev (not set: LINUX)
10&gt;  --     ossaudiodev (not set: LINUX)
10&gt;  --     overlapped (not set: IS_PY3)
10&gt;  --     _winapi (not set: IS_PY3)
10&gt;  --     _bsddb (not set: DB_INCLUDE_PATH DB_LIBRARIES)
10&gt;  --     _curses_panel (not set: CURSES_LIBRARIES PANEL_LIBRARIES HAVE_PANEL_H OR HAVE_NCURSES_PANEL_H)
10&gt;  --     _curses (not set: CURSES_LIBRARIES)
10&gt;  --     dbm (not set: NDBM_TAG GDBM_LIBRARY GDBM_COMPAT_LIBRARY)
10&gt;  --     gdbm (not set: GDBM_INCLUDE_PATH GDBM_LIBRARY GDBM_COMPAT_LIBRARY)
10&gt;  --     readline (not set: READLINE_INCLUDE_PATH READLINE_LIBRARY CURSES_LIBRARIES HAVE_READLINE_READLINE_H)
10&gt;  --     _sqlite3 (not set: SQLITE3_INCLUDE_PATH SQLITE3_LIBRARY)
10&gt;  -- 
10&gt;  -- Configuring done
10&gt;  -- Generating done
10&gt;  -- Build files have been written to: C:/D/S4D/python-build
10&gt;  Performing build step for 'python'
10&gt;  Microsoft (R) Build Engine version 12.0.40629.0
10&gt;  [Microsoft .NET Framework, version 4.0.30319.42000]
10&gt;  Copyright (C) Microsoft Corporation. All rights reserved.
10&gt;  
10&gt;  Build started 7/23/2017 2:37:56 PM.
10&gt;  Project "C:\D\S4D\python-build\ALL_BUILD.vcxproj" on node 1 (default targets).
10&gt;  Project "C:\D\S4D\python-build\ALL_BUILD.vcxproj" (1) is building "C:\D\S4D\python-build\ZERO_CHECK.vcxproj" (2) on node 1 (default targets).
10&gt;  InitializeBuildStatus:
10&gt;    Creating "x64\Release\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
10&gt;  CustomBuild:
10&gt;    All outputs are up-to-date.
10&gt;  FinalizeBuildStatus:
10&gt;    Deleting file "x64\Release\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild".
10&gt;    Touching "x64\Release\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate".
10&gt;  Done Building Project "C:\D\S4D\python-build\ZERO_CHECK.vcxproj" (default targets).
10&gt;  Project "C:\D\S4D\python-build\ALL_BUILD.vcxproj" (1) is building "C:\D\S4D\python-build\CMakeBuild\bdist_wininst\bdist_wininst.vcxproj" (3) on node 1 (default targets).
10&gt;  InitializeBuildStatus:
10&gt;    Creating "bdist_wininst.dir\Release\bdist_wininst.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
10&gt;  CustomBuild:
10&gt;    All outputs are up-to-date.
10&gt;  ClCompile:
10&gt;    All outputs are up-to-date.
10&gt;  Link:
10&gt;    All outputs are up-to-date.
10&gt;    bdist_wininst.vcxproj -&gt; C:\D\S4D\python-build\Lib\distutils\command\Release\wininst-12.0-amd64.exe
10&gt;  PostBuildEvent:
10&gt;    Description: bdist_wininst: Copying installer into 'Lib/distutils/command'
10&gt;    setlocal
10&gt;    "C:\Program Files\CMake\bin\cmake.exe" -E copy_if_different C:/D/S4D/python-build/Lib/distutils/command/Release/wininst-12.0-amd64.exe C:/D/S4D/python-build/Lib/distutils/command/wininst-12.0-amd64.exe
10&gt;    if %errorlevel% neq 0 goto :cmEnd
10&gt;    :cmEnd
10&gt;    endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
10&gt;    :cmErrorLevel
10&gt;    exit /b %1
10&gt;    :cmDone
10&gt;    if %errorlevel% neq 0 goto :VCEnd
10&gt;    :VCEnd
10&gt;  FinalizeBuildStatus:
10&gt;    Deleting file "bdist_wininst.dir\Release\bdist_wininst.tlog\unsuccessfulbuild".
10&gt;    Touching "bdist_wininst.dir\Release\bdist_wininst.tlog\bdist_wininst.lastbuildstate".
10&gt;  Done Building Project "C:\D\S4D\python-build\CMakeBuild\bdist_wininst\bdist_wininst.vcxproj" (default targets).
10&gt;  Project "C:\D\S4D\python-build\ALL_BUILD.vcxproj" (1) is building "C:\D\S4D\python-build\CMakeBuild\extensions\extension_binascii\extension_binascii.vcxproj" (4) on node 1 (default targets).
10&gt;  Project "C:\D\S4D\python-build\CMakeBuild\extensions\extension_binascii\extension_binascii.vcxproj" (4) is building "C:\D\S4D\python-build\CMakeBuild\libpython\libpython-shared.vcxproj" (5) on node 1 (default targets).
10&gt;  InitializeBuildStatus:
10&gt;    Creating "libpython-shared.dir\Release\libpython-shared.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
10&gt;  CustomBuild:
10&gt;    All outputs are up-to-date.
10&gt;  ClCompile:
10&gt;    All outputs are up-to-date.
10&gt;    All outputs are up-to-date.
10&gt;    All outputs are up-to-date.
10&gt;  Link:
10&gt;    All outputs are up-to-date.
10&gt;    libpython-shared.vcxproj -&gt; C:\D\S4D\python-build\bin\Release\python27.dll
10&gt;  FinalizeBuildStatus:
10&gt;    Deleting file "libpython-shared.dir\Release\libpython-shared.tlog\unsuccessfulbuild".
10&gt;    Touching "libpython-shared.dir\Release\libpython-shared.tlog\libpython-shared.lastbuildstate".
10&gt;  Done Building Project "C:\D\S4D\python-build\CMakeBuild\libpython\libpython-shared.vcxproj" (default targets).
10&gt;  InitializeBuildStatus:
10&gt;    Creating "extension_binascii.dir\Release\extensio.F36E4D0D.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
10&gt;  CustomBuild:
10&gt;    All outputs are up-to-date.
10&gt;  ClCompile:
10&gt;    All outputs are up-to-date.
10&gt;  Link:
10&gt;    All outputs are up-to-date.
10&gt;    extension_binascii.vcxproj -&gt; C:\D\S4D\python-build\Lib\lib-dynload\Release\binascii.pyd
10&gt;  FinalizeBuildStatus:
10&gt;    Deleting file "extension_binascii.dir\Release\extensio.F36E4D0D.tlog\unsuccessfulbuild".
10&gt;    Touching "extension_binascii.dir\Release\extensio.F36E4D0D.tlog\extension_binascii.lastbuildstate".
10&gt;  Done Building Project "C:\D\S4D\python-build\CMakeBuild\extensions\extension_binascii\extension_binascii.vcxproj" (default targets).
10&gt;  Project "C:\D\S4D\python-build\ALL_BUILD.vcxproj" (1) is building "C:\D\S4D\python-build\CMakeBuild\extensions\extension_bz2\extension_bz2.vcxproj" (6) on node 1 (default targets).
10&gt;  InitializeBuildStatus:
10&gt;    Touching "extension_bz2.dir\Release\extension_bz2.tlog\unsuccessfulbuild".
10&gt;  CustomBuild:
10&gt;    All outputs are up-to-date.
10&gt;  ClCompile:
10&gt;    All outputs are up-to-date.
10&gt;  Link:
10&gt;    C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"C:\D\S4D\python-build\Lib\lib-dynload\Release\bz2.pyd" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib "C:\D\S4D\bzip2-build\Release\libbz2.lib" ..\..\..\libs\Release\python27.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /PDB:"C:/D/S4D/python-build/Lib/lib-dynload/Release/bz2.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"C:/D/S4D/python-build/libs/Release/bz2.lib" /MACHINE:X64   /machine:x64 /DLL extension_bz2.dir\Release\bz2module.obj
10&gt;LINK : fatal error LNK1181: cannot open input file 'C:\D\S4D\bzip2-build\Release\libbz2.lib' [C:\D\S4D\python-build\CMakeBuild\extensions\extension_bz2\extension_bz2.vcxproj]
10&gt;  Done Building Project "C:\D\S4D\python-build\CMakeBuild\extensions\extension_bz2\extension_bz2.vcxproj" (default targets) -- FAILED.
</code></pre>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, could you please have a look?</p>

---

## Post #2 by @lassoan (2017-07-25 01:24 UTC)

<p>See also <a href="https://issues.slicer.org/view.php?id=4398">https://issues.slicer.org/view.php?id=4398</a></p>

---

## Post #3 by @jcfr (2017-07-25 02:14 UTC)

<p>Thanks for the report. I will review and integrate the patch of <a class="mention" href="/u/adamrankin">@adamrankin</a> tonight.</p>

---

## Post #4 by @jcfr (2017-07-25 03:37 UTC)

<p>This should be fixed in</p>
<p><a href="https://github.com/Slicer/Slicer/pull/751" class="onebox" target="_blank">https://github.com/Slicer/Slicer/pull/751</a></p>
<p>Thanks <a class="mention" href="/u/adamrankin">@adamrankin</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your suggestions, it was helpful to implement the fix.</p>

---

## Post #5 by @lassoan (2017-07-25 04:05 UTC)

<p>Thank you, I’ve started a clean build with the patch.</p>

---

## Post #6 by @lassoan (2017-07-25 12:48 UTC)

<p>Unfortunately, it’s still broken - see details in the <a href="https://issues.slicer.org/view.php?id=4398">issue tracker</a>.</p>

---

## Post #7 by @jcfr (2017-07-25 13:53 UTC)

<p>Thanks for the report. I now have a local build with VS2013, i will report back shortly</p>

---

## Post #8 by @jcfr (2017-07-25 18:56 UTC)

<p>This should now be fixed. I tested locally and I can successfully build python in Debug</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Would you mind updating your local checkout and giving an other try ?</p>
<p><a href="https://github.com/Slicer/Slicer/pull/751" class="onebox" target="_blank">https://github.com/Slicer/Slicer/pull/751</a></p>

---

## Post #9 by @jcfr (2017-07-26 02:05 UTC)

<p>Fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26174">r26174</a></p>

---
