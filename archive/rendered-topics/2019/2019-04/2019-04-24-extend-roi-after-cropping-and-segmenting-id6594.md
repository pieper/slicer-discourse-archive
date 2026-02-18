# Extend ROI after cropping and segmenting

**Topic ID**: 6594
**Date**: 2019-04-24
**URL**: https://discourse.slicer.org/t/extend-roi-after-cropping-and-segmenting/6594

---

## Post #1 by @ED1 (2019-04-24 20:32 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.10.0</p>
<p>Action:<br>
Cropped region of interest using Crop Volume. Segmented on the ROI.</p>
<p>Want to extend the ROI of interest 1 cm vertically so that I can do more segmenting on the existing segment. Is there a feature that allows the cropped ROI to be altered, specifically increased?</p>
<p>Would be very grateful for an answer on this query either way.</p>
<p>Thanks<br>
Ed</p>

---

## Post #2 by @muratmaga (2019-04-25 04:54 UTC)

<p>This may not be the easiest way, but you can try something like this:</p>
<ol>
<li>COnvert your segmentation to a label map</li>
<li>Crop your original volume with the new ROI, and make a note of your new image dimensions.</li>
<li>Go to SimpleFilters and pad your label map with 0s to match the new dimensions of your segmentations</li>
<li>Import your new label map as segmentation, and try continuing the segmentation with the new volume. If the padding is right, everything should line up I think.<br>
But again there might be other and easier ways of doing this…</li>
</ol>

---

## Post #3 by @lassoan (2019-04-25 15:59 UTC)

<aside class="quote no-group" data-username="ED1" data-post="1" data-topic="6594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ed1/48/3534_2.png" class="avatar"> ED1:</div>
<blockquote>
<p>Is there a feature that allows the cropped ROI to be altered, specifically increased?</p>
</blockquote>
</aside>
<p>You can draw an Annotation ROI and set the region where you want to edit your segmentation:</p>
<ul>
<li>Click down-arrow on the Place button on the toolbar, select ROI, click in the image, adjust the ROI size</li>
<li>Go to Segment Editor, click “Specify geometry” button (next to Master volume selector)</li>
<li>Choose the ROI node as source geometry, set spacing values, click OK</li>
</ul>
<p>This method may require less steps than what <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested above but has the disadvantage that the spacing and origin values of the segmentation will not match exactly the master volume’s (that you might find confusing).</p>

---

## Post #4 by @ED1 (2019-04-26 16:20 UTC)

<p>Thank you both for your answers. In the end, I redid the segmentation as I wanted to guarantee the accuracy of the segmentation.</p>

---
