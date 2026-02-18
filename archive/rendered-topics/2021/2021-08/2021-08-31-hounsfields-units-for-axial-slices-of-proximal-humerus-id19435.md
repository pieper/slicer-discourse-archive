# hounsfields units for axial slices of proximal humerus

**Topic ID**: 19435
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/hounsfields-units-for-axial-slices-of-proximal-humerus/19435

---

## Post #1 by @alaynavaugan (2021-08-31 14:04 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
I am trying to figure out the hounsfield units for 3 separate slices of axial images of proximal humerus. I used the segementation editor to create segments, then used the paint feature–&gt; set the threshold to 0-1600–&gt; painted my segment to only include non-cortical bone–&gt; did this for the 3 slices–&gt; segmentation quantification–&gt; gathered the mean hu’s for each segmentation.</p>
<p>My issue lies in the variabliity between patients. Some slices give me a mean hu of 200 and others a mean of 60.Am I going about this correctly?</p>
<p>this is an image of what I am trying to achieve:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b4f9562378d146ea47a4afc02c5cfc2c24d51e7.jpeg" data-download-href="/uploads/short-url/8sGG10PsNDnzZ9cAj3Y1lc77rFl.jpeg?dl=1" title="Screen Shot 2021-08-31 at 9.48.54 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b4f9562378d146ea47a4afc02c5cfc2c24d51e7_2_448x500.jpeg" alt="Screen Shot 2021-08-31 at 9.48.54 AM" data-base62-sha1="8sGG10PsNDnzZ9cAj3Y1lc77rFl" width="448" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b4f9562378d146ea47a4afc02c5cfc2c24d51e7_2_448x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b4f9562378d146ea47a4afc02c5cfc2c24d51e7_2_672x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b4f9562378d146ea47a4afc02c5cfc2c24d51e7_2_896x1000.jpeg 2x" data-dominant-color="646463"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-31 at 9.48.54 AM</span><span class="informations">1120×1248 74.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-08-31 19:03 UTC)

<p>Clinical scanners are expected to be fairly well calibrated, so there should not be big error in measurements. Most probably the density values actually vary that much between patients (difference of 140 HU is not that much).</p>

---
