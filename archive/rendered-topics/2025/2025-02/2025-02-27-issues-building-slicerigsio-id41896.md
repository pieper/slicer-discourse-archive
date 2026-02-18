# Issues building SlicerIGSIO

**Topic ID**: 41896
**Date**: 2025-02-27
**URL**: https://discourse.slicer.org/t/issues-building-slicerigsio/41896

---

## Post #1 by @Arber_Demi (2025-02-27 10:31 UTC)

<p>Hello everyone.<br>
Im trying to build Slicer from source, managed to build Slicer itself with no issues, however when building SlicerIGSIO (I need it for SlicerIGT), I am running into some issues.</p>
<pre><code class="lang-auto">cannot open input file 'vtkAddon.lib' [D:\SlicerIGSIOBuild\IGSIO-build\inner-build\Codecs\vtkIGSIOCodecs.vcxproj] [D:\SlicerIGSIOBuild\IGSIO-build\inner-build.vcxproj]
Custom build for 'D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-mkdir.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-download.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-update.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-patch.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-configure.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-build.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\99c8373aa38db437a2df59e96caa977f\inner-build-install.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\8fcbc8da5ed9e9165b70d94a0d19e077\inner-build-complete.rule;D:\SlicerIGSIOBuild\IGSIO-build\CMakeFiles\819051b13dc5853f09756c9b4c97aa8f\inner-build.rule;D:\SlicerIGSIOBuild\IGSIO\CMakeLists.txt' exited with code 1. [D:\SlicerIGSIOBuild\IGSIO-build\inner-build.vcxproj]
Custom build for 'D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-mkdir.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-download.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-update.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-patch.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-configure.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-build.rule;D:\SlicerIGSIOBuild\CMakeFiles\594d8b22cb048ab4a0a496ff0b8ed32d\IGSIO-install.rule;D:\SlicerIGSIOBuild\CMakeFiles\e6bc41f96f66305c242df4d4796588c3\IGSIO-complete.rule;D:\SlicerIGSIOBuild\CMakeFiles\028f43e02a0816fd1684920450899b5f\IGSIO.rule;D:\SlicerIGSIOExtension\CMakeLists.txt' exited with code 1.
cannot open input file 'MRMLCore.lib' [D:\SlicerIGSIOBuild\inner-build\SlicerIGSIOCommon\vtkSlicerIGSIOCommon.vcxproj]
cannot open input file 'ITKFactoryRegistration.lib' [D:\SlicerIGSIOBuild\inner-build\MetafileImporter\Logic\vtkSlicerMetafileImporterModuleLogic.vcxproj]
Custom build for 'D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-mkdir.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-download.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-update.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-patch.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-configure.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-build.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-forceconfigure.rule;D:\SlicerIGSIOBuild\CMakeFiles\931fc747f475fae8e59c3ee35244946e\inner-install.rule;D:\SlicerIGSIOBuild\CMakeFiles\e6bc41f96f66305c242df4d4796588c3\inner-complete.rule;D:\SlicerIGSIOBuild\CMakeFiles\028f43e02a0816fd1684920450899b5f\inner.rule;D:\SlicerIGSIOExtension\CMakeLists.txt' exited with code 1.
</code></pre>
<p>I couldn’t really find anyone else reporting this issue online, so I’m not sure what is going on here :[. As far as I understand from the CMake files, as long as I am providing the Slicer-build directory correctly, all of these dependencies should be covered. To configure and build, I am following the Developer guide, so using CMake GUI.</p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @pieper (2025-02-27 13:05 UTC)

<p>It’s hard to say, but since you are on windows you could try a shorter build path like <code>d:\b</code>.</p>

---

## Post #3 by @Arber_Demi (2025-02-27 13:08 UTC)

<p>I tried doing that after seeing it mentioned on the developer help page somewhere, with a 5 letter folder “SIGSS”. I also tried naming it just “L”, but I got the same errors. I tried building SlicerOpenIGTLink aswell (which I have separate build issues with), but that had no issues finding the vtkAddon folder.</p>
<p>Are there any extra CMAKE options I need to set or enable that might be missing from the usual config? It should not have issues finding it if VTK_DIR and the SLICER_DIR are set correct?</p>

---

## Post #4 by @cpinter (2025-02-27 14:23 UTC)

<p>I don’t think it’s a path issue. For extensions it is not that problematic. I build IGSIO successfully from source at <code>c:\d\_Extensions\SlicerIGSIO</code> and build directory at <code>c:\d\_Extensions\SlicerIGSIO_R</code>.</p>
<p>If you specified <code>VTK_DIR</code> maybe that is the problem. I build SlicerIGSIO with these scripts:</p>
<p>BuildExtension.bat:</p>
<pre><code class="lang-auto">set argC=0
for %%x in (%*) do Set /A argC+=1
if %argC% lss 2 echo First argument needs to be the extension source directory path, second is configuration (e.g. 'R' or 'Release'), third optional is for additional CMake options

if %argC% geq 3 echo Additional CMake options: %3

set SRC_DIR=%1
if not exist %SRC_DIR%\ (
  @echo The source directory %SRC_DIR% does not exist
  exit /b 1
)

REM // Parse configuration
set CONFIG=Release
if %argC% geq 2 set CONFIG=%2
if %CONFIG% == D set CONFIG=Debug
if %CONFIG% == R set CONFIG=Release
if %CONFIG% == Debug (
  set BIN_DIR_POSTFIX=_D
  set SLICER_SUPERBUILD_DIR_NAME=S5D
)
if %CONFIG% == Release (
  set BIN_DIR_POSTFIX=_R
  set SLICER_SUPERBUILD_DIR_NAME=S5R
)

set BIN_DIR=%SRC_DIR%%BIN_DIR_POSTFIX%
mkdir %BIN_DIR%
cd /d %BIN_DIR%

cmake -G "Visual Studio 17 2022" -DSlicer_DIR:PATH=c:/d/%SLICER_SUPERBUILD_DIR_NAME%/Slicer-build %3 %SRC_DIR%

"c:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Current\Bin\MSBuild.exe" %BIN_DIR%\ALL_BUILD.vcxproj /p:Configuration=%CONFIG%
</code></pre>
<p>and then</p>
<p><code>BuildExtension.bat c:\d\_Extensions\SlicerIGSIO R</code></p>

---

## Post #5 by @Arber_Demi (2025-02-27 14:26 UTC)

<p>VTK_DIR is just set by the CMAKE GUI, I have also tried should cmd but no difference between the two. I will try out the batch script and get back to you, thank you :]</p>

---

## Post #6 by @Arber_Demi (2025-02-27 14:59 UTC)

<p>Thanks a lot for the script. Looking at the differences between my actions and this script, I can only notice that this specifically builds ALL_BUILD, which I wasn’t doing either through command line or Visual Studio (I was just running the one .sln file that didn’t include all of the builds)<br>
I guess that solves the dependency issues!</p>
<p>Really appreciate the help, have a great day.</p>

---
