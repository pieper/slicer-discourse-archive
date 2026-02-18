# Unable to build from source on Ubuntu 18.04

**Topic ID**: 9470
**Date**: 2019-12-11
**URL**: https://discourse.slicer.org/t/unable-to-build-from-source-on-ubuntu-18-04/9470

---

## Post #1 by @aamesAtTanzle (2019-12-11 03:41 UTC)

<p>Is anyone aware of issues building Slicer from source with the following error on Ubuntu 18.04 (and PopOS)?</p>
<p>/home/aames/projects/Slicer/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsCurveNode.cxx:31:10: fatal error: vtkFrenetSerretFrame.h: No such file or directory<br>
<span class="hashtag">#include</span> &lt;vtkFrenetSerretFrame.h&gt;<br>
^~~~~~~~~~~~~~~~~~~~~~~~<br>
compilation terminated.<br>
Modules/Loadable/Markups/MRML/CMakeFiles/vtkSlicerMarkupsModuleMRML.dir/build.make:148: recipe for target ‘Modules/Loadable/Markups/MRML/CMakeFiles/vtkSlicerMarkupsModuleMRML.dir/vtkMRMLMarkupsCurveNode.cxx.o’ failed</p>

---

## Post #2 by @lassoan (2019-12-11 03:43 UTC)

<p>vtkFrenetSerretFrame comes from a VTK remote module, which should be downloaded automatically to (slicer-build-dir)/VTK/Remote/SplineDrivenImageSlicer.</p>

---

## Post #3 by @aamesAtTanzle (2019-12-11 17:54 UTC)

<p>I have discovered this text in the build scripts:</p>
<p><code>Module_SplineDrivenImageSlicer:BOOL=ON</code></p>
<p>I wonder if my local build of Slicer master branch (HEAD) is using an incompatible VTK.</p>
<p>Shouldn’t that cmake var be the following?</p>
<p><code>VTK_MODULE_ENABLE_VTK_SplineDrivenImageSlicer:STRING=WANT</code></p>

---

## Post #4 by @lassoan (2019-12-11 18:25 UTC)

<p>Are you trying to build Slicer with an externally built VTK?</p>

---

## Post #5 by @aamesAtTanzle (2019-12-11 18:29 UTC)

<p>It is using an internal VTK. The other VTK headers are being included from Slicer/.build/VTK/…</p>
<p>The .build folder is my cmake build folder. When I <code>git status</code> that VTK folder, I get:</p>
<p><code>HEAD detached at 73e89e85c4</code></p>

---

## Post #6 by @lassoan (2019-12-11 18:30 UTC)

<p>Has Slicer built VTK as part of the superbuild process?</p>

---

## Post #7 by @aamesAtTanzle (2019-12-11 18:36 UTC)

<p>That appears to be the case. I can find all of the VTK libs here:</p>
<p><code>Slicer/.build/VTK-build/lib/libvtk******</code></p>
<p>I loosely followed these instructions: <a href="https://discourse.slicer.org/t/building-slicer-on-a-freshly-installed-ubuntu-18-04/5627">https://discourse.slicer.org/t/building-slicer-on-a-freshly-installed-ubuntu-18-04/5627</a></p>
<p>In summary:</p>
<pre><code>sudo apt install qtcreator qtdeclarative5-dev qtmultimedia5-dev qtbase5-private-dev libqt5xmlpatterns5-dev libqt5svg5-dev libqt5webenginewidgets5 qtwebengine5-dev qtscript5-dev qttools5-dev libxt-dev libqt5x11extras5-dev
sudo apt install git cmake
git clone --recursive https://github.com/Slicer/Slicer.git
cd Slicer
mkdir .build
cd .build
cmake -DQt5_DIR=/usr/lib/qt5 -DCMAKE_BUILD_TYPE:STRING=Debug -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF -DSlicer_USE_SimpleITK:BOOL=OFF -DSlicer_USE_QtTesting:BOOL=OFF -DSlicer_BUILD_DataStore:BOOL=OFF -DSlicer_USE_SYSTEM_QT:BOOL=1 …/
make
</code></pre>
<p>I also applied the workaround at the bottom of that thread for fixing the system curl and OpenSSL.</p>
<p>Thank you so much for your time.</p>

---

## Post #8 by @lassoan (2019-12-11 18:45 UTC)

<p>Is this the latest master version of Slicer? Have you started the build from scratch or you have built some Slicer version first and then updated Slicer and rebuilt?</p>

---
