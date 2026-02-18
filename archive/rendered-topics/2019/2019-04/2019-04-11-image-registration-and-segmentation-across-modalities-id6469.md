# Image Registration and Segmentation Across Modalities

**Topic ID**: 6469
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/image-registration-and-segmentation-across-modalities/6469

---

## Post #1 by @MSpindler (2019-04-11 14:01 UTC)

<p>Dear Slicer community,</p>
<p>i plan on doing slice-by-slice segmentation of subcortical structures using T1,T2, and diffusion direction information. I want to start by aligning the individual brain in the midsagittal plane and in AC-PC in all modalities.<br>
If I use these aligned images as input for Slicer, drawing on one slice produces a segment covering three slices (the one before and after my current slice).<br>
As far as I understood, I can prevent this with the “Rotate to volume plane” option. But this way, the aligned image is of course shifted back into its inherent position, but I want to segment in AC-PC orientation.<br>
How can I do the AC-PC alignment in Slicer itself to get five images (t1,t2,dti,tissue probability maps) in the same orientation (for overlays) and still be able to do the segmentations without spreading to other slices?<br>
I also have the reorientation matrix to do this automatically, but I dont know where to put it.</p>
<p>Maybe someone knows which module is the right choice for that?</p>
<p>Cheers<br>
Melanie</p>

---
