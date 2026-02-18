# Overlaying Raw Data within Segmentations

**Topic ID**: 35073
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/overlaying-raw-data-within-segmentations/35073

---

## Post #1 by @Just1n (2024-03-25 19:54 UTC)

<p>Hi,</p>
<p>I was wondering if there was a feature in 3D slicer that would allow me to export my binary labelmap segmentation (very right image) as dicom files but overlaying the raw data within the segmentation, similar to how Vitrea segmentations (middle image) are shown when viewing them with ImageJ.</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01bde7a852706ade90d59c959c66451591dd8aa3.jpeg" data-download-href="/uploads/short-url/fplvmpMw0w8xH3cPQOD2IxVGdd.jpeg?dl=1" title="Labelmap.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01bde7a852706ade90d59c959c66451591dd8aa3_2_690x226.jpeg" alt="Labelmap.PNG" data-base62-sha1="fplvmpMw0w8xH3cPQOD2IxVGdd" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01bde7a852706ade90d59c959c66451591dd8aa3_2_690x226.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01bde7a852706ade90d59c959c66451591dd8aa3_2_1035x339.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01bde7a852706ade90d59c959c66451591dd8aa3_2_1380x452.jpeg 2x" data-dominant-color="6C6C6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Labelmap.PNG</span><span class="informations">1920×630 52.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-03-25 19:57 UTC)

<p>You mean show only the contents of the region you defined through segmentation? Sure you can use MaskVolume effect in SegmentEditor to do that.</p>

---

## Post #3 by @Just1n (2024-03-25 21:59 UTC)

<p>Got it, thank you so much <a class="mention" href="/u/muratmaga">@muratmaga</a>!</p>

---
