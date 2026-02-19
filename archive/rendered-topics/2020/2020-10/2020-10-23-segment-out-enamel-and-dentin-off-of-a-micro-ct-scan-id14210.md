---
topic_id: 14210
title: "Segment Out Enamel And Dentin Off Of A Micro Ct Scan"
date: 2020-10-23
url: https://discourse.slicer.org/t/14210
---

# Segment out enamel and dentin off of a micro CT scan?

**Topic ID**: 14210
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/segment-out-enamel-and-dentin-off-of-a-micro-ct-scan/14210

---

## Post #1 by @simple (2020-10-23 06:17 UTC)

<p>Hello,<br>
I’m just wondering if anyone is able to segment out enamel and dentin with 3D slicer and been able to take volumetric measurements of the enamel and dentin? Could someone please show me how to do that on slicer? I would greatly appreciate it!</p>

---

## Post #2 by @manjula (2020-10-23 13:12 UTC)

<p>You can follow the discussions at</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/teeth-segmentation/9775/9">Teeth Segmentation</a></div>
<blockquote>
<p>I’ve checked this and found that all teeth can be quite quickly and accurately segmented at once by the following steps:</p>
</blockquote>
</aside>

---

## Post #3 by @muratmaga (2020-10-23 15:53 UTC)

<aside class="quote no-group" data-username="simple" data-post="1" data-topic="14210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e36b37/48.png" class="avatar"> simple:</div>
<blockquote>
<p>volumetric measurements of the enamel and dentin</p>
</blockquote>
</aside>
<p>The link above will give you the whole tooth segmentation. You can then use the threshold with local intensity option and just extract the enamel as a individual structure, and subtract it from the whole tooth. Then you can use the segment statistics to obtain volumes of just enamel and dentin.</p>

---

## Post #4 by @simple (2020-10-23 18:14 UTC)

<p>Would someone be willing to show screenshots of how to do this? How would you subtract the rest of the tooth? Or specifically, take a threshold with local intensity and separate out the enamel? Any additional help would be much appreciated!</p>

---

## Post #5 by @muratmaga (2020-10-23 18:23 UTC)

<p>I do not have access to the data shown in the link, assuming you segmented all teeth individually, missing steps are</p>
<ol>
<li>Creating a blank segment</li>
<li>Expanding the local histogram option of threshold, choosing circle option, and making selection within enamel only area. You may have to sample in a few different places.</li>
<li>Changing the  editable area to the segment number of the tooth you are trying to split into enamel and dentin.</li>
</ol>
<p>At the end of these steps your original segment should be only dentin and your new segment should be only enamel.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/009fc9ada400d23d9534798fe6a87e40838d57d6.jpeg" data-download-href="/uploads/short-url/5wljxZ6cdtxb92njAPOo68nFxI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/009fc9ada400d23d9534798fe6a87e40838d57d6_2_690x438.jpeg" alt="image" data-base62-sha1="5wljxZ6cdtxb92njAPOo68nFxI" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/009fc9ada400d23d9534798fe6a87e40838d57d6_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/009fc9ada400d23d9534798fe6a87e40838d57d6_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/009fc9ada400d23d9534798fe6a87e40838d57d6_2_1380x876.jpeg 2x" data-dominant-color="B0AEB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×1078 379 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
