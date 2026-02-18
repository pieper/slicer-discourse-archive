# Zoom in linked slices gets out of sync when using ctl+scroll

**Topic ID**: 9994
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/zoom-in-linked-slices-gets-out-of-sync-when-using-ctl-scroll/9994

---

## Post #1 by @Felipe_Silveira (2020-01-29 12:35 UTC)

<p>Hi, I noticed that if I have a couple of slice views linked and try to zoom in/out using ctrl+scroll only the slice view in focus is changed. If I later zoom in using right click, all views get synced up again.<br>
Is this a bug or a expected behavior?</p>
<p>I’m using the nightly 4.11.0 vesion from January 10th on linux.</p>

---

## Post #2 by @lassoan (2020-01-29 17:29 UTC)

<p>Thanks for reporting this. It is a bug that we will fix soon - I’ve added it to the issue tracker: <a href="https://issues.slicer.org/view.php?id=4720">https://issues.slicer.org/view.php?id=4720</a></p>

---

## Post #3 by @fbordignon (2020-04-28 14:21 UTC)

<p>Hi guys, I’ve noticed the improvement in this issue, but I believe there is a undesired behavior when I use the ctrl+scroll zoom on linked slices. The action zooms in and out centering the window on the mouse position, but on the other linked slices the zoom is relative to the center of the respective slice.<br>
Example: If I position the mouse on top of the head and perform ctrl+scroll, I expect all linked slices to zoom in centering on the top of the head. What happens is depicted bellow. I am zooming on the rightmost slice where the red cross is and the approximated presumed mouse position in RAS is the red cross. Top row is before zooming, bottom row is after zooming. Always with ctrl+zoom<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/349b844a73eef94ec9c549579267c69499ba638b.jpeg" data-download-href="/uploads/short-url/7vo1kYQv3pKOTO37uofMAwqTJZF.jpeg?dl=1" title="headzoom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/349b844a73eef94ec9c549579267c69499ba638b_2_690x380.jpeg" alt="headzoom" data-base62-sha1="7vo1kYQv3pKOTO37uofMAwqTJZF" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/349b844a73eef94ec9c549579267c69499ba638b_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/349b844a73eef94ec9c549579267c69499ba638b_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/349b844a73eef94ec9c549579267c69499ba638b.jpeg 2x" data-dominant-color="525150"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">headzoom</span><span class="informations">1360×749 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-04-28 15:16 UTC)

<p>This could be a nice improvement. Would you be interested in trying to implement this change? We can point you to the relevant part of the code.</p>

---

## Post #5 by @fbordignon (2020-04-28 17:33 UTC)

<p>I can try. Cannot promise a deadline, but it would be nice to give it a go.</p>

---

## Post #6 by @fbordignon (2020-05-26 17:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> can you point me to the directions of how to implement this change? Thank you very much.</p>

---
