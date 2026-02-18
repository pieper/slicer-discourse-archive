# Poor resolution ultrasound stream

**Topic ID**: 33459
**Date**: 2023-12-19
**URL**: https://discourse.slicer.org/t/poor-resolution-ultrasound-stream/33459

---

## Post #1 by @J.vd.Zee (2023-12-19 11:51 UTC)

<p>Hi all!</p>
<p>I have a question regarding the streaming quality of my framegrabber to 3D Slicer (using the Plus Sever). I use the coding script for streaming named ‘Video for Windows compatible imaging device’ and change the CaptureDeviceId to ‘1’.</p>
<p>The resolution in the streamed viewer in 3D Slicer is too low for my application. Is there a work around to create a virtual camera device in OBS or something?</p>
<p>Thanks!</p>

---

## Post #2 by @Sunderlandkyl (2023-12-19 16:28 UTC)

<p>Try using the “<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html" rel="noopener nofollow ugc">Microsoft Media Foundation compatible imaging device</a>”  instead. You should be able to change the resolution.</p>

---
