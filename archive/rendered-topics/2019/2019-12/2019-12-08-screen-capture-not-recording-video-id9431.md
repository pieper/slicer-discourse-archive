---
topic_id: 9431
title: "Screen Capture Not Recording Video"
date: 2019-12-08
url: https://discourse.slicer.org/t/9431
---

# Screen capture not recording video

**Topic ID**: 9431
**Date**: 2019-12-08
**URL**: https://discourse.slicer.org/t/screen-capture-not-recording-video/9431

---

## Post #1 by @sarvpriya1985 (2019-12-08 14:21 UTC)

<p>Hi,<br>
I am trying to capture video recording of 3D segmentation. However, after clicking capture, it runs but the recording is empty. I am getting an error.</p>
<p>I am pasting  a screenshot of my settings and error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5f697212e0860651b96e9b4f687f8cdc07c3563.jpeg" data-download-href="/uploads/short-url/nGb6crLP5fCzyJMu1VqNUoSAeqv.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f697212e0860651b96e9b4f687f8cdc07c3563_2_690x395.jpeg" alt="Capture" data-base62-sha1="nGb6crLP5fCzyJMu1VqNUoSAeqv" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f697212e0860651b96e9b4f687f8cdc07c3563_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f697212e0860651b96e9b4f687f8cdc07c3563_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f697212e0860651b96e9b4f687f8cdc07c3563_2_1380x790.jpeg 2x" data-dominant-color="A69DD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1878×1077 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks,<br>
Sarv</p>

---

## Post #2 by @pieper (2019-12-08 14:34 UTC)

<p>Hi Sarv - can you look in the error log?  There should be more diagnostic info from ffmpeg.</p>

---

## Post #3 by @sarvpriya1985 (2019-12-08 14:36 UTC)

<p>Hi Steve,<br>
This is the error log I got.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a6d092a94d74a8ffe6f9ad21418da4f5c95a91.jpeg" data-download-href="/uploads/short-url/luJ1cWbTEPL5AsPvlTJNn7jwFup.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a6d092a94d74a8ffe6f9ad21418da4f5c95a91.jpeg" alt="Capture" data-base62-sha1="luJ1cWbTEPL5AsPvlTJNn7jwFup" width="690" height="364" data-dominant-color="EBEAEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">707×373 62.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2019-12-08 14:59 UTC)

<p>The error is “height not divisible by 2”. This is supposed to be taken care of by the module, but it seems that the mechanism is broken. We’ll fix this soon.</p>
<p>Until then, as a workaround, you can adjust the vertical size of the window and retry. After a few attempts, you should end up having a window height that is divisible by 2.</p>

---

## Post #5 by @sarvpriya1985 (2019-12-08 15:38 UTC)

<p>Thanks Andras, Changing the window height was able to fix it.</p>
<p>Thanks</p>

---

## Post #6 by @hherhold (2020-01-06 17:05 UTC)

<p>I did some poking at this and from what I can see, the vtkImageClip() call isn’t doing anything. I look at the image dimensions before and after the clip operation and it’s the same. Also, if the minX and maxX are 0 and 980, respectively, does this mean the width is 980, or 981? (i.e., do you include the last pixel)?</p>

---

## Post #7 by @lassoan (2020-01-06 17:09 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="6" data-topic="9431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>if the minX and maxX are 0 and 980</p>
</blockquote>
</aside>
<p>This means that the image size is 981, which cannot be encoded by many video codecs.</p>
<p>vtkImageClip should take care of this (clip the last row/column if the value is odd), but it seems to be broken due to recent update to the module. It would be great if you could have a look (file history should show how it worked before) and submit a pull request with a proposed fix.</p>

---

## Post #8 by @hherhold (2020-01-06 17:21 UTC)

<p>OK, I’ll see what changes have been made recently. Thanks for the info!</p>

---

## Post #9 by @hherhold (2020-01-08 14:08 UTC)

<p>This is exceedingly hard to reproduce on a Retina display. I seem to be only able to reproduce it when I use an external monitor. Not that this has anything to do with the issue in particular, but it’s interesting nonetheless. I’ve retrieved the version from a few checkins back and I’m checking diffs to see what change caused the issue. I’ll update again when I’m able to repro and fix it.</p>

---
