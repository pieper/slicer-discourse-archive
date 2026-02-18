# GPA 3D model and Landmarks not lining up

**Topic ID**: 24520
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/gpa-3d-model-and-landmarks-not-lining-up/24520

---

## Post #1 by @ejames26 (2022-07-27 07:08 UTC)

<p>Hello Everyone,</p>
<p>I am having some trouble getting my segmentation model to align with landmarks in my GPA analysis.</p>
<p>Landmarks were placed on volume renders from tiff stack images with spacing representative of the resolution the skulls were scanned at (eg. 43.33 is 0.4333).</p>
<p>I followed a few tutorials regarding creating a model through segment editor and the scale is reflective of the spacing in the tiff stack.</p>
<p>However, once I proceed to the GPA analysis in Slicermorph and add the segement model and the associated landmarks to the specific skull, the landmarks and model do not align. I am not sure what I am missing here.</p>
<p>I tried with a scale of 1 for just the model and the landmarks clustered in the corner of the ROI. The current way I scaled to the resolution of the scan and the landmarks are bigger this time but are not on the model as they are supposed to be to allow me to visualise realtime 3D PCAs with the model and manipulate the model.</p>
<p>Any help would be great to resolve this issue.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b3a28a2288a592e0c9173d9a1290d68ae3ec31a.jpeg" data-download-href="/uploads/short-url/8rWM43tCnHRzK8YTJqhXhsEPcAa.jpeg?dl=1" title="slicermorph issues" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3a28a2288a592e0c9173d9a1290d68ae3ec31a_2_690x480.jpeg" alt="slicermorph issues" data-base62-sha1="8rWM43tCnHRzK8YTJqhXhsEPcAa" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3a28a2288a592e0c9173d9a1290d68ae3ec31a_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b3a28a2288a592e0c9173d9a1290d68ae3ec31a_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b3a28a2288a592e0c9173d9a1290d68ae3ec31a.jpeg 2x" data-dominant-color="9D9EC2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicermorph issues</span><span class="informations">1341×934 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
