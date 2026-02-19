---
topic_id: 15306
title: "Plustoolkit On Linux"
date: 2021-01-01
url: https://discourse.slicer.org/t/15306
---

# PlusToolkit on Linux

**Topic ID**: 15306
**Date**: 2021-01-01
**URL**: https://discourse.slicer.org/t/plustoolkit-on-linux/15306

---

## Post #1 by @manjula (2021-01-01 16:38 UTC)

<p>OS- Manjaro Linux<br>
Hardware - HP Pavivillion 14-CE<br>
Webcam -  HP Wide Vision HD Camera:</p>
<p>Expectation:  Is to do this.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="MOqh6wgOOYs" data-video-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/MOqh6wgOOYs/maxresdefault.jpg" title="Webcam-based tracking in 3D Slicer/SlicerIGT" width="" height="">
  </a>
</div>

<p>Problem:</p>
<p>Will the plus tool kit work on my laptop with Linux if I build the package? or Am I forced to use windows to do this?</p>
<p>Tried building and failed and it seems to be bit difficult, so just wondering will it be worth the hassle. So even if i did manage to build it will my webcam be recognized?</p>

---

## Post #2 by @lassoan (2021-01-01 17:13 UTC)

<p>Compared to Windows, Linux support is second-grade or non-existent for most medical imaging and position tracking hardware, but with some extra effort you should be able to implement most systems on Linux, too. Webcams should work, probably best via <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpenCVVideo.html">OpenCV imaging device</a>.</p>
<p>2D barcode tracking using single camera based tracking is very inaccurate: in-plane translation/rotation error is less than a millimeter/few degrees but error in distance from camera can be 10% and out of plane rotation error can be 5-15 degrees. Therefore it can only be used for demos or low-accuracy applications.</p>
<p>For proper tracking (with submillimeter/subdegree error, resulting total system accuracy of up to a few millimeters), you can use an inexpensive stereo tracker, such as the <a href="https://www.optitrack.com/cameras/v120-duo/">Optitrack Duo</a> (costs $2300).</p>

---
