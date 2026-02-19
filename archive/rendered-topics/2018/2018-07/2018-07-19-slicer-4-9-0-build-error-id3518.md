---
topic_id: 3518
title: "Slicer 4 9 0 Build Error"
date: 2018-07-19
url: https://discourse.slicer.org/t/3518
---

# Slicer 4.9.0 build error

**Topic ID**: 3518
**Date**: 2018-07-19
**URL**: https://discourse.slicer.org/t/slicer-4-9-0-build-error/3518

---

## Post #1 by @shellyverde (2018-07-19 02:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0 check out on July 15, 2018<br>
Expected behavior: Build slicer successfully<br>
Actual behavior: Build error occured</p>
<p>Use VS 2013 to build, QT 4.8.7. Build mode: debug, x64.<br>
The following error reported:<br>
…\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx(52): fatal error C1083: Cannot open include file: ‘vtkMultiVolume.h’: No such file or directory […\Slicer-build\Modules\Loadable\VolumeRendering\MRMLDM\vtkSlicerVolumeRenderingModuleMRMLDisplayableManager.vcxproj]<br>
53&gt;</p>
<p>Any help is appreciated.<br>
Thanks,</p>
<p>-Shelly</p>

---

## Post #2 by @lassoan (2018-07-19 05:37 UTC)

<p>Thanks for reporting this.</p>
<p>As described on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">Slicer build instructions page</a>, recent Slicer nightly versions require Qt5 and VTK9 now.</p>
<p>To allow more time for transitioning, we make Slicer-4.9 compatible with Qt4 and VTK7 as well. However, we don’t have nightly dashboards for this configuration, so we may not see regressions immediately.</p>
<p>I’ve fixed the build error in r27287. If you update Slicer source code to the latest trunk/master version then build should succeed.</p>

---

## Post #3 by @shellyverde (2018-07-19 11:56 UTC)

<p>Hi Dr. Lasso,</p>
<p>Thanks for the quick fix! The build is working now.</p>
<p>-Shelly</p>

---

## Post #4 by @lassoan (2018-07-19 14:02 UTC)

<p>Great, thanks for letting us know. I would recommend to upgrade your build infrastructure to use Qt5 (this will also switch Slicer’s VTK version to VTK9), as we will drop Qt4 support after releasing Slicer-4.10.</p>

---
