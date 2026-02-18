# Light Weigh Robot IGT

**Topic ID**: 5094
**Date**: 2018-12-16
**URL**: https://discourse.slicer.org/t/light-weigh-robot-igt/5094

---

## Post #1 by @Mary7291 (2018-12-16 13:27 UTC)

<p>Hi every one,<br>
I want to build an extension(Lignt Weight Robot IGT) on slicer. But i get this error on Cmake-gui:</p>
<hr>
<p>CMake Error at CMakeLists.txt:14 (find_package):<br>
By not providing "FindSlicer.cmake" in CMAKE_MODULE_PATH this project has<br>
asked CMake to find a package configuration file provided by "Slicer", but<br>
CMake did not find one.</p>
<p>Could not find a package configuration file provided by "Slicer" with any<br>
of the following names:</p>
<p>SlicerConfig.cmake<br>
slicer-config.cmake</p>
<p>Add the installation prefix of "Slicer" to CMAKE_PREFIX_PATH or set<br>
"Slicer_DIR" to a directory containing one of the above files. If "Slicer"<br>
provides a separate development package or SDK, be sure it has been<br>
installed.</p>
<hr>
<p>I have built the slicer from source on my system using visual studio 2015 and i can open the slicer using slicer.exe.</p>
<p>I would be so appreciated if anyone could help me…</p>
<p>Operating system: windows 7 (64 bit operating system)<br>
Slicer version: build: nightly 4.11.  install on windows: 4.8.<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-12-16 15:31 UTC)

<p>When you configure the extension in CMake, set Slicer_DIR to the Slicer-build subfolder in the Slicer build tree.</p>

---

## Post #3 by @Mary7291 (2018-12-16 16:22 UTC)

<p>Thanks Mr. Lasso.</p>
<p>I do this way and it seem that the module is configured and generated.<br>
But 96 errors are appeared when i try to build the module in release mode (by opening the LightWeightRobotIGT.sln in VS and build the all build in release mode). The output errors are such as:<br>
**<br>
12&gt;LINK : fatal error LNK1181: cannot open input file ‘…\lib\Slicer-4.11\qt-loadable-modules\Release\qSlicerLightWeightRobotIGTModuleWidgets.lib’</p>
<p>and</p>
<p>9&gt;E:\LightWeightRobotIGT\LightWeightRobotIGT\Widgets\qSlicerLightWeightRobotIGTFooBarWidget.cxx(53): fatal error C1083: Cannot open include file: ‘vtkMRMLIGTLConnectorNode.h’: No such file or directory<br>
**<br>
Finally, the output of the VS is:<br>
========== Build: 6 succeeded, 10 failed, 0 up-to-date, 0 skipped ==========</p>
<p>could you please help me in building the module correctly?</p>

---

## Post #4 by @lassoan (2018-12-16 17:41 UTC)

<p>The dashboard shows build error, too: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1462832" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1462832</a></p>
<p>It should be easy to fix, seems to be caused by moving out OpenIGTLinkIF module to an extension.</p>
<p>Please submit an issue to the extension’s GitHub repository. If you don’t get an answer within a few days then let us know and we’ll help.</p>

---

## Post #5 by @Mary7291 (2018-12-16 18:34 UTC)

<p>Thanks Mr. Lasso.<br>
Ok, I will do that.</p>

---
