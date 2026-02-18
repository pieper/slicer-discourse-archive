# Segmentation displaced regarding TC image

**Topic ID**: 35251
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/segmentation-displaced-regarding-tc-image/35251

---

## Post #1 by @ILB (2024-04-03 12:28 UTC)

<p>Hi!</p>
<p>Is there a way to correct the fact that when I use TC images for segmentation, if they have several scenes (i.e, with and without contrast), if I use one of them for vessel segmentation and the other one for organ segmentation, since they are not exactly in the same position, the final segmentation appears moved (see image below). Also, this may alter the spacial relationship representation in my final 3D model.<br>
How can I solve this?<br>
Thank you!</p>

---

## Post #2 by @pieper (2024-04-03 12:33 UTC)

<p>This could happen if you are seeing patient motion between series.  You could try registration techniques (e.g. this <a href="https://github.com/SlicerRt/SegmentRegistration">approach</a>)</p>

---

## Post #3 by @cpinter (2024-04-03 12:36 UTC)

<p>Indeed, the Segment Registration extension has been created for this exact purpose. You can find it in the Extensions Manager under this name, and instructions on how to use it following the link <a class="mention" href="/u/pieper">@pieper</a> provided.</p>

---

## Post #4 by @ILB (2024-04-04 11:47 UTC)

<p>Thank you both! That was really helpful!</p>

---

## Post #5 by @ILB (2024-04-04 13:18 UTC)

<p>Now I don’t know if my problem is a registration one, because I realized that I segmented from a “zoomed in” image some organs, and other from a “zoomed out” (because of visibility).<br>
When I see for example de liver in the zoomed out, it is somehow with the scaled size, but not in the correct position. I attach some images so you can compare.</p>
<p>I’m not sure I can register the two TC images, and the module didn’t work for that. Is there a way in which I can manually move the coordinates of the segmentation, or something like that, to make it overlap with the zoomed out image?</p>
<p>Thank you in advance!</p>
<p>Best wishes</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21b4af7296207aa6e181b177bb2c001157d6871f.jpeg" alt="image" data-base62-sha1="4OaS88D5OVPxZRa01ZSAtAARiz5" width="633" height="322"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ec46b12dc412ba1d62dea3d6fa17286f30488f4.png" alt="image" data-base62-sha1="kmYCKpEDf7Y7jMPdndcKGJK9xgo" width="633" height="306"></p>

---

## Post #6 by @pieper (2024-04-04 14:08 UTC)

<p>It’s unlikely, but possible you are seeing <a href="https://github.com/Slicer/Slicer/issues/7668">this issue</a>.  You should try using the latest preview version of Slicer to check.</p>
<aside class="quote no-group" data-username="ILB" data-post="5" data-topic="35251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e9c0ed/48.png" class="avatar"> ILB:</div>
<blockquote>
<p>manually move the coordinates of the segmentation</p>
</blockquote>
</aside>
<p>Yes, you can use the transforms for that if it’s really what you need.</p>
<p>But also it’s hard for us to know from just the screenshots.  What would help is to know if you can replicate this issue on data for which you can share an entire scene.  E.g. if you could replicate it on already public data or on anonymized data you can share.</p>

---
