# Can rectangle tool be used to create 2D box proposals in a CT datastet?

**Topic ID**: 6026
**Date**: 2019-03-05
**URL**: https://discourse.slicer.org/t/can-rectangle-tool-be-used-to-create-2d-box-proposals-in-a-ct-datastet/6026

---

## Post #1 by @David_D (2019-03-05 13:35 UTC)

<p>Slicer neophyte here.</p>
<p>I’d like to train an R-CNN to label pathology on CT with box proposals</p>
<p>First, can I use the rectangle tool in this way, and save all the box proposals placed throughout the CT as a label map for training an R-CNN?</p>
<p>Second- The box should have a visible outline (solid, dotted, or dashed lines) but should otherwise be transparent. When I select a color, it flood fills the box, obscuring the pathology.</p>
<p>Is the rectangle tool the best approach for this purpose, and if so, can I modify the tool so it only shows the box outline?</p>

---

## Post #2 by @cpinter (2019-03-05 14:27 UTC)

<aside class="quote no-group" data-username="David_D" data-post="1" data-topic="6026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/f14d63/48.png" class="avatar"> David_D:</div>
<blockquote>
<p>it flood fills the box, obscuring the pathology</p>
</blockquote>
</aside>
<p>Segmentation does not paint in the CT image. It creates a separate object, so it does not “flood fill” or “obscure” anything, simply mark regions in the segmentation.</p>
<p>Would it solve your problem if you could “crop” out the selected (segmented) area from the volume, making everything else black? Please try the Mask volume effect in Segment Editor and see if it works for you. (Painting on the image is not something that’s normally done in medical image computing)</p>

---
