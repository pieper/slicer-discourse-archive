---
topic_id: 38236
title: "Segment Statistics Volume And Hu Values"
date: 2024-09-05
url: https://discourse.slicer.org/t/38236
---

# Segment Statistics volume and HU values

**Topic ID**: 38236
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/segment-statistics-volume-and-hu-values/38236

---

## Post #1 by @XMTian (2024-09-05 13:15 UTC)

<p>Hi everyone,</p>
<p>Thank you for developing this amazing software, it is very efficient and easy to use, and I benefited a lot from it.</p>
<p>Please allow me to briefly introduce my questions. I am studying a fish with bilateral asymmetry in the head, and I want to use 3D slicer to compare the volume and density differences of the bones on the left and right sides of the head. I used Segment Editor to separate the left and right sides of the bones of interest, and used Segment Statistics to count the volume and density differences.</p>
<p>However, I don’t have reference phantoms to do HU correction. But considering that I am comparing the differences between the left and right sides of the same fish, I am considering whether I can compare them directly without correction.</p>
<p>In this regard, I have the following questions and hope to get your answers.</p>
<ol>
<li>
<p>What file should be placed in the Scalar volume? Can I put the unseparated volume of the fish?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec31bb139773b2f311fb5ac8ceeca4dbefe1a69e.png" data-download-href="/uploads/short-url/xHteiPjgH6XzlYqqyjYkdKglXwq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec31bb139773b2f311fb5ac8ceeca4dbefe1a69e_2_690x424.png" alt="image" data-base62-sha1="xHteiPjgH6XzlYqqyjYkdKglXwq" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec31bb139773b2f311fb5ac8ceeca4dbefe1a69e_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec31bb139773b2f311fb5ac8ceeca4dbefe1a69e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec31bb139773b2f311fb5ac8ceeca4dbefe1a69e.png 2x" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×533 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>This is the Segment statistics of the left and right sides of the three bones<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752a1c9f6f22402c48af8054969a1d32e5a54759.png" data-download-href="/uploads/short-url/gIu5sWte90mXdFeKlylBESbkedH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752a1c9f6f22402c48af8054969a1d32e5a54759_2_690x101.png" alt="image" data-base62-sha1="gIu5sWte90mXdFeKlylBESbkedH" width="690" height="101" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/752a1c9f6f22402c48af8054969a1d32e5a54759_2_690x101.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752a1c9f6f22402c48af8054969a1d32e5a54759.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/752a1c9f6f22402c48af8054969a1d32e5a54759.png 2x" data-dominant-color="F2F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×138 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>If I understand correctly, column J (Mean) can be understood as density difference, and column N (Volume (mm3)) can be understood as volume difference, is it correct?<br>
Can I interpret that the left and right sides of the bones of this fish have consistent considerable volume differences and slight density differences? I think this is very interesting.<br>
Thanks in advance for your answers.</p>
<p>Best regards,<br>
Xiaomeng</p>

---

## Post #2 by @pieper (2024-09-05 13:25 UTC)

<p>From what I can see it sounds like you have a good understanding.  Yes you can use the original scan as the scalar volume and yes, the per-segment means would reflect the values from the scan and should be comparable within the scan.  Volume differences should also be valid if the image geometry is correct.  If you aren’t sure you could do some try some experiments to doublecheck (e.g. physically measure some piece of anatomy and compare it to a measure from the scan).</p>

---

## Post #3 by @XMTian (2024-09-05 13:38 UTC)

<p>Thank you very much for your prompt reply. It’s much clearer now, and also thank you for your suggestions! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---
