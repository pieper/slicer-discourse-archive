---
topic_id: 18166
title: "Slicer Quit Unexpectedly Mac"
date: 2021-06-16
url: https://discourse.slicer.org/t/18166
---

# Slicer quit unexpectedly- Mac

**Topic ID**: 18166
**Date**: 2021-06-16
**URL**: https://discourse.slicer.org/t/slicer-quit-unexpectedly-mac/18166

---

## Post #1 by @Kruthi (2021-06-16 12:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b329dc52de5b1e8ecf368f1fd12e1b83861edd8.jpeg" data-download-href="/uploads/short-url/hzRaLXnUgYUofOZfpAcTFWCnbao.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b329dc52de5b1e8ecf368f1fd12e1b83861edd8_2_620x499.jpeg" alt="image" data-base62-sha1="hzRaLXnUgYUofOZfpAcTFWCnbao" width="620" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b329dc52de5b1e8ecf368f1fd12e1b83861edd8_2_620x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b329dc52de5b1e8ecf368f1fd12e1b83861edd8_2_930x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b329dc52de5b1e8ecf368f1fd12e1b83861edd8_2_1240x998.jpeg 2x" data-dominant-color="EFEFEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1998×1610 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello,</p>
<p>I am trying to open .mrb file but this is the error message I get every time. I am using a MacBook Pro.</p>

---

## Post #2 by @lassoan (2021-06-16 17:22 UTC)

<p>You can try if latest Slicer Stable Release or Slicer Preview Release can read the scene. If not, then you can rename the file to have .zip file extension (instead of .mrb) and load each data file into the application (instead of the .mrml or .mrb scene file).</p>

---

## Post #3 by @Kruthi (2021-06-16 20:29 UTC)

<p>It works when I changed the folder to .zip and loaded them.<br>
For future purposes, how do I avoid this error? Should I save everything as .zip?</p>

---

## Post #4 by @lassoan (2021-06-16 20:37 UTC)

<p>The crash occurred because a node could not be loaded from the file (e.g., because the file got corrupted, you have run out of memory when the scene was saved, …). If you load from the zip file then you only load whatever is in the file, not what is described in the mrml scene file, so there will be no failed attempt of loading a non-existing/corrupted file.</p>
<p>If you use a recent Slicer version (especially a recent Preview Release) then you get much more detailed error reporting both during saving and loading mrb files, so you will know if something went wrong and what to do about it.</p>

---
