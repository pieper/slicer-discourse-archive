# Masking a segment

**Topic ID**: 13020
**Date**: 2020-08-16
**URL**: https://discourse.slicer.org/t/masking-a-segment/13020

---

## Post #1 by @whirl (2020-08-16 06:58 UTC)

<p>Hello. I’m trying to segment a knee. I started with menisci. I’ve almost finished the green one and I want to segment the yellow. I’ve chosen the right areas and I want to use “Fill between slices” but I do not want to edit the green meniscus. How can I mask it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3134fc15e65ac3339b8ed28198556c73fe3ea3cf.jpeg" data-download-href="/uploads/short-url/71iUKhXc3JpXAXqoFZCDhPqqYDZ.jpeg?dl=1" title="Screenshot from 2020-08-16 10-36-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134fc15e65ac3339b8ed28198556c73fe3ea3cf_2_690x387.jpeg" alt="Screenshot from 2020-08-16 10-36-12" data-base62-sha1="71iUKhXc3JpXAXqoFZCDhPqqYDZ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134fc15e65ac3339b8ed28198556c73fe3ea3cf_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134fc15e65ac3339b8ed28198556c73fe3ea3cf_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3134fc15e65ac3339b8ed28198556c73fe3ea3cf.jpeg 2x" data-dominant-color="B1B1B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-16 10-36-12</span><span class="informations">1366×768 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-16 14:37 UTC)

<p>I don’t think there should be any interference, but if you find that there is, then hide the segment. Hidden segments are excluded from “Fill between slices”.</p>
<p>You can also create a new segmentation node and move segments to that. Segments in other segmentations nodes are of course not impacted in any way by any editing operations.</p>
<p>Masking settings, too, can be used to prevent segments from being modified, but probably the two other methods described above are simpler.</p>

---

## Post #3 by @whirl (2020-08-17 08:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13020" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t think there should be any interference,</p>
</blockquote>
</aside>
<p>Unfortunately, it is.</p>
<p>By saing about hiding the segment, do you mean clicking an “eye” button next to the name of the segment? If so, it doesn’t work.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13020" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also create a new segmentation node and move segments to that. Segments in other segmentations nodes are of course not impacted in any way by any editing operations.</p>
</blockquote>
</aside>
<p>Do you mean creating a new segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80c0c2ff41726ea9295b0e4206b4b3193f4ed05a.png" data-download-href="/uploads/short-url/in06AvkbixTkxdoNS92SSrMPJto.png?dl=1" title="Screenshot from 2020-08-17 11-55-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0c2ff41726ea9295b0e4206b4b3193f4ed05a_2_690x387.png" alt="Screenshot from 2020-08-17 11-55-12" data-base62-sha1="in06AvkbixTkxdoNS92SSrMPJto" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0c2ff41726ea9295b0e4206b4b3193f4ed05a_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0c2ff41726ea9295b0e4206b4b3193f4ed05a_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80c0c2ff41726ea9295b0e4206b4b3193f4ed05a.png 2x" data-dominant-color="B1B1B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-17 11-55-12</span><span class="informations">1366×768 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-08-17 17:47 UTC)

<aside class="quote no-group quote-modified" data-username="whirl" data-post="3" data-topic="13020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7cd45c/48.png" class="avatar"> whirl:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also create a new segmentation node and move segments to that. Segments in other segmentations nodes are of course not impacted in any way by any editing operations.</p>
</blockquote>
</aside>
<p>Do you mean creating a new segmentation?</p>
</blockquote>
</aside>
<p>Yes. You can then move segments around in Segmentations module (or by drag-and-dropping segments in the subject hierarchy tree in Data module).</p>

---
