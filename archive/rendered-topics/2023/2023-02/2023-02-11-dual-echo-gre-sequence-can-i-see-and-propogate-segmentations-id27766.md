---
topic_id: 27766
title: "Dual Echo Gre Sequence Can I See And Propogate Segmentations"
date: 2023-02-11
url: https://discourse.slicer.org/t/27766
---

# Dual echo GRE sequence. Can I see and propogate segmentations in both IP and OOP images?

**Topic ID**: 27766
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/dual-echo-gre-sequence-can-i-see-and-propogate-segmentations-in-both-ip-and-oop-images/27766

---

## Post #1 by @Doctor06 (2023-02-11 13:56 UTC)

<p>Hello,<br>
I am using 3D Slicer 5.0.3.<br>
The dual echo GRE sequence contains both in (IP)- and out-of-phase (OOP) slices. When I import this sequence from the DCM Loading area, I only see out-of-phase images on the conventional screen. My goal here is to perform a semiautomatic segmentation and calculate the texture parameters, in both IP and OOP sequences.<br>
1- Can I see both in- and out-of-phase images alternately?<br>
2- Will my segmentations on out-of-phase be automatically propagated to in-phase by the 3D Slicer?<br>
3- I want to remove the hepatic and portal veins from the mask while segmenting the liver. I guess I need to use the Islands tool for this. I watched the liver segmentation video on youtube. Can you suggest any other online helpful resources?<br>
The video I mentioned was produced using version 4.10.2 and I couldn’t even find the Crop feature where it is explained in the video. I think new new videos are required for Version 5.x’s.</p>
<p>Thank you to the researchers who will help.</p>

---

## Post #2 by @lassoan (2023-02-15 06:14 UTC)

<aside class="quote no-group" data-username="Doctor06" data-post="1" data-topic="27766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ec9cab/48.png" class="avatar"> Doctor06:</div>
<blockquote>
<p>Can I see both in- and out-of-phase images alternately?</p>
</blockquote>
</aside>
<p>You can load any number of images and show 2 of them at the same time (blended with the chosen transparency) in a slice view.</p>
<aside class="quote no-group" data-username="Doctor06" data-post="1" data-topic="27766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ec9cab/48.png" class="avatar"> Doctor06:</div>
<blockquote>
<p>Will my segmentations on out-of-phase be automatically propagated to in-phase by the 3D Slicer?</p>
</blockquote>
</aside>
<p>If you register the images so that they are all spatially aligned then the segmentation that you create will be aligned with all of them.</p>
<aside class="quote no-group" data-username="Doctor06" data-post="1" data-topic="27766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ec9cab/48.png" class="avatar"> Doctor06:</div>
<blockquote>
<p>I want to remove the hepatic and portal veins from the mask while segmenting the liver. I guess I need to use the Islands tool for this. I watched the liver segmentation video on youtube. Can you suggest any other online helpful resources?</p>
</blockquote>
</aside>
<p>Can you provide some images and sketches that explain what exactly you would like to achieve?</p>
<aside class="quote no-group" data-username="Doctor06" data-post="1" data-topic="27766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ec9cab/48.png" class="avatar"> Doctor06:</div>
<blockquote>
<p>The video I mentioned was produced using version 4.10.2 and I couldn’t even find the Crop feature where it is explained in the video. I think new new videos are required for Version 5.x’s.</p>
</blockquote>
</aside>
<p>Please send a link to the video (include the time where the feature is used).</p>

---
