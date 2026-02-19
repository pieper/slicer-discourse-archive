---
topic_id: 399
title: "Segmentation And Rotating"
date: 2017-05-29
url: https://discourse.slicer.org/t/399
---

# Segmentation and rotating

**Topic ID**: 399
**Date**: 2017-05-29
**URL**: https://discourse.slicer.org/t/segmentation-and-rotating/399

---

## Post #1 by @pieper (2017-05-29 21:35 UTC)

<p>(Repost from slicer-users)</p>
<p>Hi Slicer-Users,</p>
<p>I have a DICOM set of MR images (shoulder) and I made it 3D with 3D slicer.<br>
<a href="http://slicer-users.65878.n3.nabble.com/file/n4032270/soru_1.png">http://slicer-users.65878.n3.nabble.com/file/n4032270/soru_1.png</a></p>
<p>And with segmentation modul (with scissors) I cut the humerus bone and<br>
created surface. That why it appears blue.</p>
<p><a href="http://slicer-users.65878.n3.nabble.com/file/n4032270/soru2.png">http://slicer-users.65878.n3.nabble.com/file/n4032270/soru2.png</a></p>
<p>My question is how can I rotate only humerus bone (blue part in 3D). Right<br>
now it rotates as a whole.</p>
<p>My second question is; Is there a better way to segment humerus bone apart<br>
from whole? Because scissors  kind of change the shape of humerus bone and I<br>
dont want it to change.</p>
<p>Any help will be appreciated<br>
Thank you very much.</p>

---

## Post #2 by @pieper (2017-05-29 21:40 UTC)

<p>Segmenting the humerus from MR will be a challenge.  Probably the best is to get familiar with the various tools in the Segment Editor and see what works best for you.</p>
<p>Once you have the segmentation you can apply rotations with the Transforms module:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms</a></p>

---

## Post #3 by @lassoan (2017-05-30 01:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="399">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>My question is how can I rotate only humerus bone (blue part in 3D). Right<br>
now it rotates as a whole</p>
</blockquote>
</aside>
<p>If you apply a transform to a segmentation node, the transformation is applied to all segments. To transform a segment separately, create a new segmentation node and copy or move the segment that you want to move separately into the new segmentation node (use Segmentations module Copy/move segments function).</p>

---

## Post #4 by @lassoan (2017-05-30 01:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="399">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Is there a better way to segment humerus bone apart<br>
from whole? Because scissors  kind of change the shape of humerus bone and I<br>
dont want it to change.</p>
</blockquote>
</aside>
<p>Scissors is intended for pre- and post-processing. For accurate delineation of a bone, I would suggest to use the manual “Paint” effect or semi-automatic “Grow from seeds” effect.</p>

---
