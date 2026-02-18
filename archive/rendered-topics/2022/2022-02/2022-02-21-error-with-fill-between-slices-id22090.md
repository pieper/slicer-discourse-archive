# Error with "Fill between slices" 

**Topic ID**: 22090
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/error-with-fill-between-slices/22090

---

## Post #1 by @frmrz (2022-02-21 17:15 UTC)

<p>Dear community,</p>
<p>I’m trying to propagate the manual annotations I have, using the “Fill between slices” method.<br>
In some volume-segmentation pairs, I get the error “Auto-complete operation skipped: all visible segments are empty”. My pipeline is always the same: load volume and segmentation → set segmentation and master volume → set visibility for all segments → initialize “Fill between slices”.<br>
I have no clear indicator why in some volumes this works, while in others I have this problem. Do you know why this problem might occur? or point me in the direction where to search?</p>
<p>If I can resolve this problem I’d like to automate this process for all the volumes I have. Do you know of any snippets that might be of help?</p>
<p>Thank you all, have a great day!<br>
Francesco</p>

---

## Post #2 by @lassoan (2022-02-21 17:31 UTC)

<p>You can only initialize “Fill between slices” if you have some non-empty visible segments. Please try with the latest Slicer Preview Release. If the problem persists then the best would be if you could share a scene (upload somewhere and post the link) where initialization fails and there are non-empty segments. Make sure no patient health information is included in publicly shared files.</p>

---

## Post #3 by @frmrz (2022-02-22 09:41 UTC)

<p>Hi Andras,</p>
<p>thank you for your answer. Here <a href="https://we.tl/t-a7f02DBkCi" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a> you can find one of the volume-segmentation pair that raises the error.<br>
I had no luck in installing the Preview release since it raised the error: libITKniftiio-5.3.so.1: cannot open shared object file: No such file or directory. I don’t know if this is a common problem, I’ll try to solve it later.<br>
As for automating the “Fill” process, can you point me in the direction of the correct API to use?</p>

---

## Post #4 by @lassoan (2022-02-24 05:45 UTC)

<p>The <a href="https://github.com/Slicer/Slicer/issues/6202">ITK packaging issue</a> will be fixed on Friday. Until then you can use a Slicer Preview Release from 10 days ago: <a href="https://download.slicer.org/?offset=-10">https://download.slicer.org/?offset=-10</a>.</p>
<p>I’ve just tested this on Linux using Slicer-4.13.0-2022-02-14 and it worked well:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7809f88f646ab3f69b2124f6853009596eb3aa.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7809f88f646ab3f69b2124f6853009596eb3aa.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b7809f88f646ab3f69b2124f6853009596eb3aa.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #5 by @frmrz (2022-02-24 07:14 UTC)

<p>I’ll try on the version you mentioned, in the meantime, I’ve managed to do it programmatically, probably I’m messing something up when using the GUI.<br>
Thanks for the awesome support!</p>

---
