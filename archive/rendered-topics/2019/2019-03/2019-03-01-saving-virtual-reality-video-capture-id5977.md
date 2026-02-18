# Saving Virtual Reality video capture

**Topic ID**: 5977
**Date**: 2019-03-01
**URL**: https://discourse.slicer.org/t/saving-virtual-reality-video-capture/5977

---

## Post #1 by @justdcinaus (2019-03-01 03:29 UTC)

<p>Good morning gentle persons. (depending on time zone)<br>
I’m now comfortable with both segmenting and creating models, and using Volume Rendering and viewing both in Virtual Reality.</p>
<p>However while Screen Capture does a good job by rotating the model and capturing that output, I’d like to be able to capture my view from within Virtual Reality (Oculus Rift) as I can then both rotate and lean in as required.</p>
<p>I’ve used the Oculus Mirror program, which does a competent job; sometimes, however it appears to add significant overheads and makes the scene ‘jumpy’.<br>
Is there another method of doing this from within Slicer itself?</p>

---

## Post #2 by @lassoan (2019-03-01 18:45 UTC)

<p>We record videos as described here: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#how-to-record-virtual-reality-videos" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality/#how-to-record-virtual-reality-videos</a>. I’ve never experienced that SteamVR’s built-in mirror view would have any performance impact - maybe try that instead of Oculus Mirror.</p>
<p>You may try <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#rendering-is-slow" rel="nofollow noopener">these tips</a> to improve rendering performance.</p>

---
