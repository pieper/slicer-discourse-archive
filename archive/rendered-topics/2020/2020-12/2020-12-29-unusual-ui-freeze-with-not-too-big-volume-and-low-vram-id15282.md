---
topic_id: 15282
title: "Unusual Ui Freeze With Not Too Big Volume And Low Vram"
date: 2020-12-29
url: https://discourse.slicer.org/t/15282
---

# Unusual UI freeze with not too big volume and low VRAM

**Topic ID**: 15282
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/unusual-ui-freeze-with-not-too-big-volume-and-low-vram/15282

---

## Post #1 by @chir.set (2020-12-29 19:41 UTC)

<p>I just wish to report this unexpected behavior. It is not a fundamental problem.</p>
<p>My laptop has 1 GB shared VRAM. Loaded a DICOM volume 1024x1024x499 volume and initiated a Volume Rendering display (GPU tay casting, normal quality). No 3D view is obtained, that was expected.</p>
<p>What’s weird is a partial UI freeze : the module’s widgets, slice views and 3D view do not respond at all, while the upper Module selection combobox and the menus work normally, though not altering the UI anymore. No background process is hung nor eating CPU.</p>
<p>Below is console output.</p>
<blockquote>
<p>Imported a DICOM directory, checking for extensions<br>
The following data types are in your database:</p>
<p>Structured Report Objects</p>
<p>The following extensions are not installed, but may help you work with this data:</p>
<p>QuantitativeReporting</p>
<p>You can install extensions using the Extensions Manager option from the View menu.<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 3: TSA Willis 1024<br>
Switch to module:  “VolumeRendering”<br>
amdgpu: Not enough memory for command submission.<br>
Switch to module:  “Volumes”<br>
Switch to module:  “Transforms”<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /home/arc/src/Slicer4138-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
…<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /home/arc/src/Slicer4138-SuperBuild/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.</p>
<p>DevTools listening on ws://127.0.0.1:1337/devtools/browser/360087ad-40d1-40d3-8dca-b3c4141061a1<br>
Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="noopener nofollow ugc">http://127.0.0.1:1337</a><br>
Switch to module:  “Volumes”</p>
</blockquote>
<p>The amdgpu module declares “Not enough memory for command submission” very quickly.</p>
<p>I’m wondering if Slicer can catch this limit, issue a warning and restore control to the main thread.</p>
<p>Not a fundamental problem, just FYI.</p>
<p>Regards.</p>

---

## Post #2 by @pieper (2020-12-29 19:45 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="15282">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>The amdgpu module declares “Not enough memory for command submission” very quickly.</p>
<p>I’m wondering if Slicer can catch this limit, issue a warning and restore control to the main thread.</p>
</blockquote>
</aside>
<p>Slicer catches C++ exceptions generated from library code, but this looks like a driver error so it may not be possible for us to catch.  Once you start getting these driver errors the system may be in a corrupt state that is not recoverable.</p>

---
