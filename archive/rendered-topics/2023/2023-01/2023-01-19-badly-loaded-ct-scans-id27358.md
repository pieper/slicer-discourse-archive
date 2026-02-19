---
topic_id: 27358
title: "Badly Loaded Ct Scans"
date: 2023-01-19
url: https://discourse.slicer.org/t/27358
---

# badly loaded ct scans

**Topic ID**: 27358
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/badly-loaded-ct-scans/27358

---

## Post #1 by @pawel (2023-01-19 18:01 UTC)

<p>Hello<br>
I have a problem with loaded ct scans. In te red window ct scany are properly visible but in green an yellow view ct scan are stretched or narrowed. I send screen with my problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86543d1e9c61defa26de86201016b4511e8445a1.png" data-download-href="/uploads/short-url/jaksCSgaVIGIyed6XEEwyzMd0wF.png?dl=1" title="Ct scan problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86543d1e9c61defa26de86201016b4511e8445a1_2_690x477.png" alt="Ct scan problem" data-base62-sha1="jaksCSgaVIGIyed6XEEwyzMd0wF" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86543d1e9c61defa26de86201016b4511e8445a1_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86543d1e9c61defa26de86201016b4511e8445a1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86543d1e9c61defa26de86201016b4511e8445a1.png 2x" data-dominant-color="3B3A46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ct scan problem</span><span class="informations">829×574 95.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best,</p>
<p>Pawel</p>

---

## Post #2 by @pieper (2023-01-19 18:52 UTC)

<p>Please post what kind of files these are and how you loaded them (e.g. dicom, tiff, etc).</p>

---

## Post #3 by @pawel (2023-01-19 20:07 UTC)

<p>This Ct scans are tiff and I loaded them as tiff.</p>

---

## Post #4 by @pieper (2023-01-19 20:38 UTC)

<p>That explains a lot.  Tiff files don’t track the spacing so you need to add it manually.  In the Volumes → Volume Information you can add the spacing manually for the pixel and slice spacing.  Or you may find SlicerMorph’s <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">ImageStacks module</a> useful.</p>

---

## Post #5 by @pawel (2023-01-19 21:17 UTC)

<p>Thank you:) I have different ct scans for several skulls and only one ct scan loaded good although  these ct scan also are Tiff files.<br>
I add the spacing manually and I think that is all good. Do  I have to add in  the  Image spacing same value (e.g 30 mm) to all ct scan  in windows (red , yellow and green)  have this same proportion?<br>
Best,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6baa468b5631eb56bae22d092da5efbfb2a844c5.png" data-download-href="/uploads/short-url/fmrTZkeMc4oJQ3OhlRrSP7dAKix.png?dl=1" title="Ct scan problem 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6baa468b5631eb56bae22d092da5efbfb2a844c5_2_690x281.png" alt="Ct scan problem 1" data-base62-sha1="fmrTZkeMc4oJQ3OhlRrSP7dAKix" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6baa468b5631eb56bae22d092da5efbfb2a844c5_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6baa468b5631eb56bae22d092da5efbfb2a844c5_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6baa468b5631eb56bae22d092da5efbfb2a844c5.png 2x" data-dominant-color="86868C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ct scan problem 1</span><span class="informations">1348×550 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2023-01-19 21:23 UTC)

<aside class="quote no-group" data-username="pawel" data-post="5" data-topic="27358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecae2f/48.png" class="avatar"> pawel:</div>
<blockquote>
<p>Do I have to add in the Image spacing same value (e.g 30 mm) to all ct scan in windows (red , yellow and green) have this same proportion?</p>
</blockquote>
</aside>
<p>You have to check that with whoever provided you with the dataset. Often microCT scans are isotropic (same spacing along all axes), but not guaranteed to be that way.</p>
<p>Also spacing units are mm. I don’t  think you have 30mm spacing in your scan. 30 micrometers perhaps? (=0.030mm). Again check this with whoever gave you the data.</p>

---

## Post #7 by @pawel (2023-01-19 22:23 UTC)

<p>Thank you for your help.</p>

---

## Post #8 by @pawel (2023-01-20 10:51 UTC)

<p>Do I understand correctly that the introduced good values in the Image spacing will cause that  measurements made on ct scans will be correct? For example, I know that the skull is 40 mm lenght.<br>
Correct data in the Image spacing will cause that measurements made on ct scans  skull is also 40 mm length.</p>

---

## Post #9 by @pieper (2023-01-20 13:10 UTC)

<p>Yes, if the spacing is correct the measurements should be correct.  But using a format such as tiff where you need to enter values manually there’s always room for human error.  Better would be to work on the acquisition process to use a format where the spacing is automatically encoded (perhaps dicom) and do some test runs with calibration phantoms to be sure it’s working as expected.</p>

---
