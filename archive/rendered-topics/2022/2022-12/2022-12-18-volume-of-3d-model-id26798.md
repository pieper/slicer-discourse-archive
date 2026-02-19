---
topic_id: 26798
title: "Volume Of 3D Model"
date: 2022-12-18
url: https://discourse.slicer.org/t/26798
---

# Volume of 3D model

**Topic ID**: 26798
**Date**: 2022-12-18
**URL**: https://discourse.slicer.org/t/volume-of-3d-model/26798

---

## Post #1 by @damiazlkflee (2022-12-18 03:58 UTC)

<p>Windows 10, slicer 4.11.<br>
This is a common question I think. My apologies for asking this simple question but after reading all the manuals, definitions, and answers in the support, I still cannot understand.</p>
<p>Issue: I have produced a 3D model of the frontal sinus cavity by cropping the region and applying threshold value. Now, I want to know the volume of my 3D frontal sinus cavity. I click on segment statistics to get the volume. But there is three volume given which is computed from labelmap statistic, scalar volume statistic and closed surface statistic.</p>
<p>May I know the difference between these three in a brief/simple term?<br>
and which one of these three should I choose to represent the volume of my reconstructed 3D model?</p>
<p>Thank you in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/080fe64c722a12c8d033316e92b8c06248e86708.jpeg" data-download-href="/uploads/short-url/19jSQ31o3q4dzjW11MwGvAbEl8k.jpeg?dl=1" title="vol" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/080fe64c722a12c8d033316e92b8c06248e86708_2_690x319.jpeg" alt="vol" data-base62-sha1="19jSQ31o3q4dzjW11MwGvAbEl8k" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/080fe64c722a12c8d033316e92b8c06248e86708_2_690x319.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/080fe64c722a12c8d033316e92b8c06248e86708_2_1035x478.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/080fe64c722a12c8d033316e92b8c06248e86708.jpeg 2x" data-dominant-color="999795"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vol</span><span class="informations">1366×632 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-12-18 14:38 UTC)

<p>They are all different ways of calculating the same basic quantity but may have different behaviors based on the size/shape of your object and images.  If these descriptions are not clear perhaps we can work together to improve them:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>

---

## Post #3 by @lassoan (2022-12-18 16:48 UTC)

<p>I’ve added some clarifications <a href="https://slicer--6739.org.readthedocs.build/en/6739/user_guide/modules/segmentstatistics.html#what-is-the-difference-between-the-surface-and-volume-values-computed-by-various-plugins">here</a>. Please check and let us know if we need to add further details.</p>

---

## Post #4 by @damiazlkflee (2022-12-19 02:34 UTC)

<p>Thank you.</p>
<p>I need a few further clarification.<br>
Is  closed surface means it is empty inside?</p>
<p>For scalar volume (values are computed for only that part of the segments that overlap with the bounding box of the scalar volume), I dont understand the ‘segments that overlap’. How can I know it is overlap?<br>
Where is the bounding  box of scalar volume? Is it the white box in the 3D pane?</p>

---

## Post #5 by @lassoan (2022-12-19 05:32 UTC)

<aside class="quote no-group" data-username="damiazlkflee" data-post="4" data-topic="26798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/damiazlkflee/48/65986_2.png" class="avatar"> damiazlkflee:</div>
<blockquote>
<p>Is closed surface means it is empty inside?</p>
</blockquote>
</aside>
<p>A segment in Slicer is a solid 3D object. It is not empty inside. A closed surface representation specifies a segment by a closed surface boundary. Anything within that closed surface is inside the segment.</p>
<aside class="quote no-group" data-username="damiazlkflee" data-post="4" data-topic="26798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/damiazlkflee/48/65986_2.png" class="avatar"> damiazlkflee:</div>
<blockquote>
<p>For scalar volume (values are computed for only that part of the segments that overlap with the bounding box of the scalar volume), I dont understand the ‘segments that overlap’. How can I know it is overlap?</p>
</blockquote>
</aside>
<p>I’ve rephrased the text. Please check and let us know if it is clear now.</p>
<aside class="quote no-group" data-username="damiazlkflee" data-post="4" data-topic="26798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/damiazlkflee/48/65986_2.png" class="avatar"> damiazlkflee:</div>
<blockquote>
<p>Where is the bounding box of scalar volume? Is it the white box in the 3D pane?</p>
</blockquote>
</aside>
<p>I meant that it is within the scalar volume. I’ve removed the “bounding box” term to avoid confusion.</p>

---
