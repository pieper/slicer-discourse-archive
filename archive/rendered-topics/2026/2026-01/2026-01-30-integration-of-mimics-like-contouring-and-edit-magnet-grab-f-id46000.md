# Integration of Mimics-like contouring and edit (magnet + grab) functionality into 3D Slicer for segmentation of CT Lumbar bones

**Topic ID**: 46000
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/integration-of-mimics-like-contouring-and-edit-magnet-grab-functionality-into-3d-slicer-for-segmentation-of-ct-lumbar-bones/46000

---

## Post #1 by @Mirza_Ahmad_Awais (2026-01-30 13:20 UTC)

<p>Hello! I am trying to add contouring and edit contouring functionality into 3D slicer as a replacement to mimics or mimics-like tool so we can accurately segment lumbar bodies for surgical implant design purposes. Firstly, I’d like to know about the feasibility of building such a solution into 3D Slicer, and secondly about the high-level workflow in order to achieve such a task.</p>
<p>A little about what we are currently working with on a high level understanding, we have a NIFTI file of a lumbar body that we want to load into 3D slicer, with binary lap map as representation and generate contours over the mask and be able to edit/smooth or manipulate it as we are able to do in materialize mimics(which is a paid software). I want to know about the possibility and practicality of such a solution in medical/surgical level settings and its accuracy and how would we go about doing it.</p>

---

## Post #2 by @muratmaga (2026-01-30 18:50 UTC)

<p>I never used Mimics, so I do not know of the functionalities you mentioned. Googling suggests that Level Trace in segment editor is very similar, if not identical, to magnet feature. Not sure what the grab does.</p>
<p>Based on this, I would say it should be able to implement what you want to do.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d09c27725cd90f718d689229dd432f2be0b1a726.png" data-download-href="/uploads/short-url/tLrS5GecSHnKqZVRAvvRRvOVDT0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09c27725cd90f718d689229dd432f2be0b1a726_2_577x500.png" alt="image" data-base62-sha1="tLrS5GecSHnKqZVRAvvRRvOVDT0" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09c27725cd90f718d689229dd432f2be0b1a726_2_577x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09c27725cd90f718d689229dd432f2be0b1a726_2_865x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d09c27725cd90f718d689229dd432f2be0b1a726.png 2x" data-dominant-color="ADADAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×869 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
