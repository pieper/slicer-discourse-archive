# Segmentation on Rotated Data (or should we stick with axial,coronal,saggital planes?)

**Topic ID**: 23766
**Date**: 2022-06-08
**URL**: https://discourse.slicer.org/t/segmentation-on-rotated-data-or-should-we-stick-with-axial-coronal-saggital-planes/23766

---

## Post #1 by @joosicky (2022-06-08 13:04 UTC)

<p>Hello there. We are new at 3dslicer and we just trying to annotate some of our MRI datas, using 3dslicer segmentation tools.</p>
<p>We have completed 1 of our data with fully manual segmentation. But in the end we have discovered our MRI data was rotated a bit. İn the slice oriantation button, theres a option called Reformat. While we were thinking our annotations was done at Sagittal screen, it was already switched to reformat option. And if we change that mode to standart Sagittal screen, then our annotations getting broken. Tons of little holes, extra pixels etc.</p>
<p>Should we start over and fix our data first to Sagittal plane (to fix the little rotattion) and then start segmentation? or maybe its posible to fix from this point? (Sory if I couldnt describe it very well, Im not a native English speaker.) Thank you.</p>

---

## Post #2 by @pieper (2022-06-08 13:07 UTC)

<p>What you decide to do depends on how you intend to use the segmentations.  See this for more information: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---

## Post #3 by @mikebind (2022-06-08 16:33 UTC)

<p>What Slicer considers the “Sagittal” plane is based on orientation information from the header of the image file(s). For medical imaging, this is typically ultimately based on a coordinate system based on the scanner rather than actually on the patient.  For MRI imaging, the orientation of the image grid is often chosen to reflect the actual orientation of the patient.  For example, if a patient has her head turned so that she is not looking straight up relative to the scanner, the MR acquisition box is often rotated so that the resulting image planes are better aligned with the anatomical planes of the head than with the scanner vertical or horizontal planes. In your imaging, it is likely that you did your manual segmentations with the slice views oriented with the planes of the imaging grid, and that this grid is rotated relative to the scanner coordinate axes.  If this is the case, you can probably ignore what Slicer labels as the “sagittal” plane as the “reformat” plane which is aligned with your image grid planes is likely to be closer to the true anatomical sagittal plane relative to the patient.  Of course you should check whether this appears to be true for your images, but in my experience looking at clinical head MRI imaging this is usually true. The link that <a class="mention" href="/u/pieper">@pieper</a> shared is very helpful for understanding what you are looking at when you view a segmentation in slice views which are not aligned with the image voxel grid planes and is definitely recommended reading.</p>

---
