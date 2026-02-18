# Cutting through all the segmentation nodes

**Topic ID**: 42480
**Date**: 2025-04-08
**URL**: https://discourse.slicer.org/t/cutting-through-all-the-segmentation-nodes/42480

---

## Post #1 by @Mikko_Pyysalo (2025-04-08 03:06 UTC)

<p>Dear community,<br>
I have 2 CT scans of the same sinus. STL models of the scans are aligned and converted to segmentation nodes.<br>
Is it possible to cut through (with scissors, segment editor module) all the segmentation nodes simultaneously and export the cutted nodes as aligned models?</p>
<p>Thank you in advance,<br>
Mikko</p>

---

## Post #2 by @mau_igna_06 (2025-04-08 12:36 UTC)

<aside class="quote no-group" data-username="Mikko_Pyysalo" data-post="1" data-topic="42480">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mikko_pyysalo/48/79903_2.png" class="avatar"> Mikko_Pyysalo:</div>
<blockquote>
<p>Is it possible to cut through (with scissors, segment editor module) all the segmentation nodes simultaneously and export the cutted nodes as aligned models?</p>
</blockquote>
</aside>
<p>No, it is not possible as you propose it. But you can move the segments from Segmentation1 to Segmentation2, and then cut through all segments on the same segmentation. See picture below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff899fd465ce964903a0f1c89fef841a06ba7168.jpeg" data-download-href="/uploads/short-url/AsAC3dPq1D8zrNthvtuN9acCjFu.jpeg?dl=1" title="Screenshot from 2025-04-08 09-32-16_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff899fd465ce964903a0f1c89fef841a06ba7168_2_690x391.jpeg" alt="Screenshot from 2025-04-08 09-32-16_2" data-base62-sha1="AsAC3dPq1D8zrNthvtuN9acCjFu" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff899fd465ce964903a0f1c89fef841a06ba7168_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff899fd465ce964903a0f1c89fef841a06ba7168_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff899fd465ce964903a0f1c89fef841a06ba7168_2_1380x782.jpeg 2x" data-dominant-color="ACAEC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-04-08 09-32-16_2</span><span class="informations">1920×1088 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And then you can “Export visible segments to models” from the Data module as usual</p>

---

## Post #3 by @Mikko_Pyysalo (2025-04-08 12:52 UTC)

<p>Thank you!<br>
It worked!</p>
<p>Best regards,<br>
Mikko</p>

---
