# Measure asymmetry of 3d jaw model (bone and tissue)

**Topic ID**: 9338
**Date**: 2019-11-30
**URL**: https://discourse.slicer.org/t/measure-asymmetry-of-3d-jaw-model-bone-and-tissue/9338

---

## Post #1 by @annom (2019-11-30 02:12 UTC)

<p>Hi There,</p>
<p>I have been given Dicom images of a jaw to measure the asymmetry of my jaw. My jaw is wider jaw on the left side but an extra vertical length on the right side of the jawline.</p>
<p>So far I was able to reconstruct the jaw but I would like to create a heatmap with measurements in mm to see exactly how much width there is on the left side compared to the right side of the face. Is this possible with 3D slicer or is there another tool with a short learning curve that I could use for that?</p>
<p><strong>(If it is too difficult for a beginner like me, then I would be willing to pay some money for it as I have a surgery in 3 weeks to make my jaw more symmetrical and normally the surgeon just does it by feeling but I would like to be more data-driven).</strong></p>
<p>Please see some examples of pictures here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a704579402da8de67042ccf654154f5dd1b96b.jpeg" data-download-href="/uploads/short-url/O0dBUUwlbHbWnFKQJYoCKpcBZx.jpeg?dl=1" title="Screenshot_20191130_021357" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05a704579402da8de67042ccf654154f5dd1b96b_2_685x500.jpeg" alt="Screenshot_20191130_021357" data-base62-sha1="O0dBUUwlbHbWnFKQJYoCKpcBZx" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05a704579402da8de67042ccf654154f5dd1b96b_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05a704579402da8de67042ccf654154f5dd1b96b_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05a704579402da8de67042ccf654154f5dd1b96b.jpeg 2x" data-dominant-color="A4B1A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20191130_021357</span><span class="informations">1070×780 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2019-11-30 10:27 UTC)

<p>You can do the followings to assess symmetry of a structure:</p>
<ul>
<li>copy the DICOM CD to your computer, drag-and-drop the folder to Slicer application windows, import it as DICOM, load the image using DICOM module</li>
<li>segment the structure of interest using Segment Editor module</li>
<li>export to model: in Data module by right-clicking on it and choosing the corresponding option</li>
<li>mirror the model using Surface Toolbox module</li>
<li>align the original and mirrored model based on matching anatomical landmarks using Fiducial registration wizard module</li>
<li>measure distance between the models (compute colormap) using Model to model distance module</li>
</ul>
<p>Install SlicerIGT and Model To Model distance to get all the necessary modules.</p>
<p>Note that using any information that you gain by your analysis to influence the surgery in any way would be risky for many reasons.  If you have any concerns then you may ask your surgeon or ask for second opinion from another clinician, but in general the best is to just trust the competence of your surgeon.</p>

---
