# Switching between CT -lung and CT Abdomen in Segment Editor?

**Topic ID**: 33394
**Date**: 2023-12-14
**URL**: https://discourse.slicer.org/t/switching-between-ct-lung-and-ct-abdomen-in-segment-editor/33394

---

## Post #1 by @Hannnonk (2023-12-14 11:26 UTC)

<p>Operating system:Windows 11<br>
Slicer version:Slicer version 4.13.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>In “Volumes” you can switch between CT -lung and CT Abdomen. Is there a key-stroke short cut or a quick way to do this in “Segment Editor”?</p>

---

## Post #2 by @pieper (2023-12-14 12:36 UTC)

<p>You can right-click in the slice views to access these via the context menu.</p>

---

## Post #3 by @Hannnonk (2023-12-16 13:17 UTC)

<p>So on Segment editor I can right click on a slice and access a context menu? That does not seem to work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5658158090890f74658669b0ea439a46351d9d31.jpeg" data-download-href="/uploads/short-url/cjPMsfDsAoaFOG5T8rQ8jLLTtYt.jpeg?dl=1" title="2023-12-16_8-12-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5658158090890f74658669b0ea439a46351d9d31_2_690x327.jpeg" alt="2023-12-16_8-12-03" data-base62-sha1="cjPMsfDsAoaFOG5T8rQ8jLLTtYt" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5658158090890f74658669b0ea439a46351d9d31_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5658158090890f74658669b0ea439a46351d9d31_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5658158090890f74658669b0ea439a46351d9d31_2_1380x654.jpeg 2x" data-dominant-color="B9BAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-12-16_8-12-03</span><span class="informations">1858×883 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In addition, is there a shortcut to make all segments visible?<br>
THX</p>

---

## Post #4 by @Hannnonk (2023-12-18 11:38 UTC)

<p>Thanks I updated my 3D Slicer version and found this option.<br>
Is there a way to make all segments visible at once?</p>

---

## Post #5 by @pieper (2023-12-18 18:14 UTC)

<aside class="quote no-group" data-username="Hannnonk" data-post="4" data-topic="33394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/b5a626/48.png" class="avatar"> Hannnonk:</div>
<blockquote>
<p>Is there a way to make all segments visible at once?</p>
</blockquote>
</aside>
<p>If it’s something you use a lot you could write a little python script for it and then tie it to a hotkey.  What I often do is multi-select segments in the Data module and the use Toggle Visibility in the context menu; you get quite a bit of flexibility without much clicking.</p>

---
