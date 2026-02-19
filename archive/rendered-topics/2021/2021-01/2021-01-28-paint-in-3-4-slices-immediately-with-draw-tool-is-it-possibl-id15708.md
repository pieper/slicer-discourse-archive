---
topic_id: 15708
title: "Paint In 3 4 Slices Immediately With Draw Tool Is It Possibl"
date: 2021-01-28
url: https://discourse.slicer.org/t/15708
---

# Paint in 3-4 slices immediately with draw tool? Is it possible?

**Topic ID**: 15708
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/paint-in-3-4-slices-immediately-with-draw-tool-is-it-possible/15708

---

## Post #1 by @NoobForSlicer (2021-01-28 05:50 UTC)

<p>I have a question.<br>
I used a draw tool a few times to fix a slice or two but now I am wondering, can this tool actualy apply the drawing to not just 1 but let’s say 3 slices right away?</p>
<p>For example I define 1.5 mm as a range in that axis?</p>
<p>So let’s say i draw a circle on one slice and then the exact same circle is segmented in the upper slice and the lower slice?</p>

---

## Post #2 by @lassoan (2021-01-28 05:57 UTC)

<p>You can adjust the brush thickness by modifying the slice spacing in the slice view controller:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f03bef4e4ef757650c9329d80b38a9a37f8d6f62.png" data-download-href="/uploads/short-url/yhd09ZHIBsjMSeZDlqMLJAJ4cSK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f03bef4e4ef757650c9329d80b38a9a37f8d6f62_2_690x305.png" alt="image" data-base62-sha1="yhd09ZHIBsjMSeZDlqMLJAJ4cSK" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f03bef4e4ef757650c9329d80b38a9a37f8d6f62_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f03bef4e4ef757650c9329d80b38a9a37f8d6f62_2_1035x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f03bef4e4ef757650c9329d80b38a9a37f8d6f62.png 2x" data-dominant-color="787786"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1297×575 60.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I would not recommend this, because you it does not produce optimal segmentation results (creates very visible staircase artifacts). Instead, a very simple alternative is to enable sphere brush to paint on neighbor slices. It makes you less tempted to paint the exact same shape on several slices. Still quite similar, but much more flexible and provides much nicer results is “Fill between slices” effect. It allows you to skip any number of slices and interpolates smoothly between slices that you segment.</p>
<p>There are many other 3D tools, depending on what exactly you want to segment. You can check out the segmentation tutorials or ask here for further advice.</p>

---
