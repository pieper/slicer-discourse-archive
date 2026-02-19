---
topic_id: 30586
title: "3D Slicer Compilation Under Armv8 Aarch64 Soc Rk3399"
date: 2023-07-13
url: https://discourse.slicer.org/t/30586
---

# 3D Slicer compilation under ARMv8 aarch64 (SoC RK3399)

**Topic ID**: 30586
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/3d-slicer-compilation-under-armv8-aarch64-soc-rk3399/30586

---

## Post #1 by @Mik (2023-07-13 15:04 UTC)

<p>Have anyone tried to compile 3D Slicer from scratch under the aarch64 architecture?</p>
<p>I have a RockPro64 board from Pine64 vendor with a RK3399 chip. Linux distribution is the same as for x86_64 machine. I’m trying to compile the Slicer debug build from source with default parameters. Compilation process for python 3.9.10 and DCMTK packages goes without problem, but VTK package compilation unable to start.</p>
<p>Shell output says that <code>PythonSlicer</code> file has wrong file format.</p>
<p>Some console output:</p>
<pre><code class="lang-auto">[ 41%] Completed 'python'
[ 41%] Built target python
[ 41%] Performing update step for 'VTK'
[ 41%] No patch step for 'VTK'
[ 41%] Performing configure step for 'VTK'
loading initial cache file /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-prefix/tmp/VTK-cache-Debug.cmake
CMake Deprecation Warning at CMake/vtkWrapSettings.cmake:14 (message):
  Manually specifying `VTK_PYTHON_VERSION` is deprecated as only Python3 is
  supported.
Call Stack (most recent call first):
  CMakeLists.txt:88 (include)


-- SplineDrivenImageSlicer: Building as a Remote VTK module
-- Could NOT find Python3 (missing: Interpreter) (found suitable version "3.9.10", minimum required is "3.4")
    Reason given by package: 
        Interpreter: Cannot run the interpreter "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/bin/PythonSlicer"

CMake Error at CMake/vtkModule.cmake:4685 (message):
  Could not find the Python3 external dependency.
Call Stack (most recent call first):
  Utilities/Python/CMakeLists.txt:28 (vtk_module_find_package)


-- Configuring incomplete, errors occurred!
make[2]: *** [CMakeFiles/VTK.dir/build.make:100: VTK-prefix/src/VTK-stamp/VTK-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:700: CMakeFiles/VTK.dir/all] Error 2
make: *** [Makefile:101: all] Error 2

</code></pre>
<p>I’ve checked <code>PythonSlicer</code> binary file and the <code>reafelf</code> command says that it’s a x86_64 binary, instread of aarch64. How can it be under the ARM architecture?</p>
<pre><code class="lang-auto">readelf -h /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/bin/PythonSlicer
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x4120f0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          10418416 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         9
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30

</code></pre>

---

## Post #2 by @pieper (2023-07-13 15:11 UTC)

<p>I only know of arm support for the new macs, which can be <a href="https://github.com/Slicer/Slicer/issues/5944#issuecomment-1328179343">compiled from source</a>.</p>
<p>It looks like you will need to investigate the python build arguments to get a workable python, but probably this can be made to work.  Let us know how it goes.</p>

---

## Post #3 by @Mik (2023-07-14 12:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="30586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It looks like you will need to investigate the python build arguments to get a workable python, but probably this can be made to work. Let us know how it goes.</p>
</blockquote>
</aside>
<p>The problem was with the CTKAPPLAUNCHER package. The binary packages is downloaded from CTK <a href="https://github.com/commontk/AppLauncher/releases/download/v0.1.31/CTKAppLauncher-0.1.31-linux-amd64.tar.gz" rel="noopener nofollow ugc">repo</a>, and it precompiled for amd64. Since there is no architecture check in <a href="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_CTKAPPLAUNCHER.cmake" rel="noopener nofollow ugc">cmake</a> file for CTKAPPLAUNCHER and there is no build release for arm64 anyway, the simple solution was to compile AppLauncher from the source and replace binary exec file.</p>
<p>Compilation is in progress.</p>

---

## Post #4 by @Mik (2023-07-19 14:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="30586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Let us know how it goes.</p>
</blockquote>
</aside>
<p>Good news: i’ve managed to compile successfully (the only problem was CTKAPPLAUNCHER).<br>
Bad news: first start shows that most of modules are failed to be installed.</p>
<p>Screen of the first start:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3185b4652be4f9dd6f64d40d55df23075311e045.png" data-download-href="/uploads/short-url/745R8fcAn61cWY1At2C96dGQlaB.png?dl=1" title="Slicer-output" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3185b4652be4f9dd6f64d40d55df23075311e045_2_690x378.png" alt="Slicer-output" data-base62-sha1="745R8fcAn61cWY1At2C96dGQlaB" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3185b4652be4f9dd6f64d40d55df23075311e045_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3185b4652be4f9dd6f64d40d55df23075311e045_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3185b4652be4f9dd6f64d40d55df23075311e045_2_1380x756.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-output</span><span class="informations">1920×1053 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Small part of console output:</p>
<pre><code class="lang-auto">michel@rockpro64:~/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build$ ./Slicer
Traceback (most recent call last):
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/AddManyMarkupsFiducialTest.py", line 5, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/AddManyMarkupsFiducialTest.py"  as module "AddManyMarkupsFiducialTest" !
Fail to instantiate module  "AddManyMarkupsFiducialTest"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/util.py", line 131, in importVTKClassesFromDirectory
    from vtk import vtkObjectBase
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/AtlasTests.py", line 5, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import *
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/ScriptedLoadableModule.py", line 8, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/AtlasTests.py"  as module "AtlasTests" !
Fail to instantiate module  "AtlasTests"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/BRAINSFitRigidRegistrationCrashIssue4139.py", line 4, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import *
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/ScriptedLoadableModule.py", line 8, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/BRAINSFitRigidRegistrationCrashIssue4139.py"  as module "BRAINSFitRigidRegistrationCrashIssue4139" !
Fail to instantiate module  "BRAINSFitRigidRegistrationCrashIssue4139"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/util.py", line 131, in importVTKClassesFromDirectory
    from vtk import vtkObjectBase
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/ColorLegendSelfTest.py", line 5, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import *
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/ScriptedLoadableModule.py", line 8, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/ColorLegendSelfTest.py"  as module "ColorLegendSelfTest" !
Fail to instantiate module  "ColorLegendSelfTest"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/util.py", line 131, in importVTKClassesFromDirectory
    from vtk import vtkObjectBase
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CompareVolumes.py", line 2, in &lt;module&gt;
    import vtk, qt, ctk, slicer
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CompareVolumes.py"  as module "CompareVolumes" !
Fail to instantiate module  "CompareVolumes"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/util.py", line 131, in importVTKClassesFromDirectory
    from vtk import vtkObjectBase
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CropVolumeSelfTest.py", line 2, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import *
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/ScriptedLoadableModule.py", line 8, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CropVolumeSelfTest.py"  as module "CropVolumeSelfTest" !
Fail to instantiate module  "CropVolumeSelfTest"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CropVolumeSequence.py", line 5, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/CropVolumeSequence.py"  as module "CropVolumeSequence" !
Fail to instantiate module  "CropVolumeSequence"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOM.py", line 10, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import *
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/bin/Python/slicer/ScriptedLoadableModule.py", line 8, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOM.py"  as module "DICOM" !
Fail to instantiate module  "DICOM"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMEnhancedUSVolumePlugin.py", line 1, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMEnhancedUSVolumePlugin.py"  as module "DICOMEnhancedUSVolumePlugin" !
Fail to instantiate module  "DICOMEnhancedUSVolumePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMGeAbusPlugin.py", line 5, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMGeAbusPlugin.py"  as module "DICOMGeAbusPlugin" !
Fail to instantiate module  "DICOMGeAbusPlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/python-install/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMImageSequencePlugin.py", line 4, in &lt;module&gt;
    import vtk
  File "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtk.py", line 4, in &lt;module&gt;
    from vtkmodules.vtkCommonCore import *
ImportError: /home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/VTK-build/lib/python3.9/site-packages/vtkmodules/vtkCommonCore.cpython-39-aarch64-linux-gnu.so: undefined symbol: _ZTI23vtkSOADataArrayTemplateIdE
loadSourceAsModule - Failed to load file "/home/michel/devel/git/Slicer/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-5.3/qt-scripted-modules/DICOMImageSequencePlugin.py"  as module "DICOMImageSequencePlugin" !
</code></pre>
<p>It looks like some sort of problem with VTK and python.</p>

---

## Post #5 by @pieper (2023-07-19 14:48 UTC)

<p>Nice progress <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Yes, it looks like a path problem.  You can inspect the environment by launching a shell with the launcher (e.g. <code>./Slicer --launch bash</code>) and see if the <code>PYTHONPATH</code> and <code>LD_LIBRARY_PATH</code> directories correspond to your build tree. Probably you can set them manually to get things to load.  Once you have that you can see how to fix the build process to set them automatically.</p>

---

## Post #6 by @Mik (2023-08-03 10:38 UTC)

<p>I was able to compile and run 3D Slicer successfully only the Release build with gcc-13.2 compiler and enabled VTK testing. First attempt with gcc-12.2 was a failure, mainly because of vtkSOADataArrayTemplate python wrapper (linker message <code>VTK python binding undefined symbols vtkSOADataArrayTemplate</code>), and only one third of VTK tests were successful.</p>
<p>After compiler upgrade and several failed attempts (Debug build; build without VTK tests) the compilation process was finally successful and 3D Slicer first start went without errors!</p>
<p>Some features will not work in any case due to limitations of Mali GPU in SoC. The MRHead test data was loaded and visualized (even simple VolumeRendering) but with a lot of VTK output because of shaders.</p>
<p>That topic was very useful as well.</p><aside class="quote quote-modified" data-post="1" data-topic="6459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-for-ubuntu-arm64/6459">Slicer for Ubuntu arm64</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Notes on compilation efforts for compiling Slicer for arm64: 
Problem: VTK does not compile. 
Solution: 

Set VTK_OPENGL_HAS_EGL and VTK_OPENGL_HAS_ES
In &lt;SlicerDir&gt;/SuperBuild/External_VTK.cmake remove section that has -DModule_vtkGUISupportQtOpenGL:BOOL=ON in it
Edit QVTKOpenGLNativeWidget.cxx to use QOpenGLExtraFunctions instead of QOpenGLFunctions_3_2_Core


Problem: CTKAPPLAUNCHER is a download of amd64 
Solution: Overwrite executable &lt;Slicer-build&gt;/CTKAPPLAUNCHER/bin/CTKAppLauncher with co…
  </blockquote>
</aside>


---
