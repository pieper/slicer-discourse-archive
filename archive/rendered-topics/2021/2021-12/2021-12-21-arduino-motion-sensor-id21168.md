---
topic_id: 21168
title: "Arduino Motion Sensor"
date: 2021-12-21
url: https://discourse.slicer.org/t/21168
---

# Arduino motion sensor

**Topic ID**: 21168
**Date**: 2021-12-21
**URL**: https://discourse.slicer.org/t/arduino-motion-sensor/21168

---

## Post #1 by @PaoloZaffino (2021-12-21 11:02 UTC)

<p>Hi all,<br>
a student of mine, for his thesis, developed a new module of the ArduinoController extension: Arduino Motion Sensor.</p>
<p>The module allows interacting with the view controllers module by using gestures captured via a very chip IR sensor.<br>
A basic guide is provided in the <a href="https://github.com/pzaffino/SlicerArduinoController#readme" rel="noopener nofollow ugc">README.md file</a></p>
<p>This video shows a small demo of the new module:</p><div class="youtube-onebox lazy-video-container" data-video-id="h1KTOkB4TMk" data-video-title="3D Slicer motion sensor" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=h1KTOkB4TMk" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/h1KTOkB4TMk/maxresdefault.jpg" title="3D Slicer motion sensor" width="" height="">
  </a>
</div>

<p>Any suggestion and/or comment is more than welcome.</p>
<p>Thanks a lot,<br>
Paolo</p>

---

## Post #2 by @lassoan (2021-12-21 15:10 UTC)

<p>Thanks for sharing, it looks promising. It would be useful to have a way to continuously set parameters, such as the slice offset, zoom factor, window, level. For panning the zoomed image, adjust window/level, it would be necessary to adjust two variables at the same time (e.g., by tracking motion along two axes).</p>

---

## Post #3 by @PaoloZaffino (2021-12-27 15:17 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
Yes, of course it’s just a first implementation, we hope to add more features in the future.<br>
For the moment the slice offset can be set via GUI (it’s the only parameter you can set now).</p>
<p>In addition consider that the gesture sensor is extremely basic, so the performance are very limited.</p>
<p>Paolo</p>

---
