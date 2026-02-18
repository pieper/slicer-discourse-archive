# Lines appear other than centerline

**Topic ID**: 18531
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/lines-appear-other-than-centerline/18531

---

## Post #1 by @parvaneh.a (2021-07-06 14:27 UTC)

<p>Operating system:<br>
Slicer version:4.11<br>
Expected behavior: Only one line as centerline<br>
Actual behavior:getting another colorful network such as a graph</p>
<p>I am using the tutorial to get the center line of the vessels attached to a bigger organ with the following settings :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbbb78c76016893f3698856867b0b94c2ba95dad.jpeg" data-download-href="/uploads/short-url/t4iA8UxM8XR2CUxV3RSakwdpEoR.jpeg?dl=1" title="Screen Shot 2021-07-06 at 10.25.28 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbbb78c76016893f3698856867b0b94c2ba95dad_2_393x500.jpeg" alt="Screen Shot 2021-07-06 at 10.25.28 AM" data-base62-sha1="t4iA8UxM8XR2CUxV3RSakwdpEoR" width="393" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbbb78c76016893f3698856867b0b94c2ba95dad_2_393x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbbb78c76016893f3698856867b0b94c2ba95dad_2_589x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbbb78c76016893f3698856867b0b94c2ba95dad_2_786x1000.jpeg 2x" data-dominant-color="E4E4E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-06 at 10.25.28 AM</span><span class="informations">1184×1504 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the output I get one green line which is the center line but I also get another colorful network such as a graph and the edges of that graph is sometimes connected to each other from out of the mesh. What are those lines are exactly and why they are colorful?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a591e8eb929cbbaab3ff6fc9bcd2ddc309668355.jpeg" data-download-href="/uploads/short-url/nCHomMHdMGEKPo7JnFqkzi1N1Gt.jpeg?dl=1" title="Screen Shot 2021-07-06 at 10.17.21 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a591e8eb929cbbaab3ff6fc9bcd2ddc309668355_2_673x500.jpeg" alt="Screen Shot 2021-07-06 at 10.17.21 AM" data-base62-sha1="nCHomMHdMGEKPo7JnFqkzi1N1Gt" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a591e8eb929cbbaab3ff6fc9bcd2ddc309668355_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a591e8eb929cbbaab3ff6fc9bcd2ddc309668355.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a591e8eb929cbbaab3ff6fc9bcd2ddc309668355.jpeg 2x" data-dominant-color="9A9BB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-06 at 10.17.21 AM</span><span class="informations">894×664 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-07-09 05:15 UTC)

<p>The <a href="https://github.com/vmtk/SlicerExtension-VMTK#extract-centerline">Extract centerline module’s documentation</a> should answer most of your questions. If anything is not clear then let us know. To make sure we point you to the right direction, please also describe what your clinical end goal is (how do you plan to use the extracted centerlines).</p>

---
