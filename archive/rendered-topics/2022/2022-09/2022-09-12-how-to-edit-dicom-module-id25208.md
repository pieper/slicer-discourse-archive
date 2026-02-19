---
topic_id: 25208
title: "How To Edit Dicom Module"
date: 2022-09-12
url: https://discourse.slicer.org/t/25208
---

# How to edit DICOM module

**Topic ID**: 25208
**Date**: 2022-09-12
**URL**: https://discourse.slicer.org/t/how-to-edit-dicom-module/25208

---

## Post #1 by @miniminic (2022-09-12 03:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4736bb695ab05f451f3383f63563ccad40e71e6.png" data-download-href="/uploads/short-url/wAY9mMJQ4ysE0E9wnQf4fOrtwJU.png?dl=1" title="捕获1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4736bb695ab05f451f3383f63563ccad40e71e6_2_690x211.png" alt="捕获1" data-base62-sha1="wAY9mMJQ4ysE0E9wnQf4fOrtwJU" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4736bb695ab05f451f3383f63563ccad40e71e6_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4736bb695ab05f451f3383f63563ccad40e71e6_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4736bb695ab05f451f3383f63563ccad40e71e6_2_1380x422.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获1</span><span class="informations">2221×680 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to modify some of the code and UI of the DICOM module, but when I click Edit, a py.exe appears and then disappears. When I click Edit UI, error: Application does NOT exists [E:/Company/SlicerBuild/Slicer-build/bin/D:/Qt/5.15.2/5.15.2/msvc2019_64/bin/./designer.exe].<br>
Slicer gets an incorrect path.<br>
Thanks.</p>

---

## Post #2 by @miniminic (2022-09-13 03:50 UTC)

<p>I found hou to edit ui<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce8ce26b5da2dfba089fbe7d3a6d44125710466a.jpeg" data-download-href="/uploads/short-url/ttecyeYLLabiXrdKu2mPVRayFS2.jpeg?dl=1" title="屏幕截图 2022-09-13 114936" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce8ce26b5da2dfba089fbe7d3a6d44125710466a_2_576x499.jpeg" alt="屏幕截图 2022-09-13 114936" data-base62-sha1="ttecyeYLLabiXrdKu2mPVRayFS2" width="576" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce8ce26b5da2dfba089fbe7d3a6d44125710466a_2_576x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce8ce26b5da2dfba089fbe7d3a6d44125710466a_2_864x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce8ce26b5da2dfba089fbe7d3a6d44125710466a.jpeg 2x" data-dominant-color="F3F3F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-13 114936</span><span class="informations">963×835 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pieper (2022-09-13 12:33 UTC)

<p>Yes, you can do that for modifying your local installation or experimenting.  If you want to make improvements to the UI or add hooks to more easily support alternate use cases please consider making contributions to the slicer repository.</p>

---
