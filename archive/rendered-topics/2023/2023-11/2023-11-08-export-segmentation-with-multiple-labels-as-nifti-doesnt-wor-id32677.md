---
topic_id: 32677
title: "Export Segmentation With Multiple Labels As Nifti Doesnt Wor"
date: 2023-11-08
url: https://discourse.slicer.org/t/32677
---

# Export segmentation with multiple labels as nifti doesn't work

**Topic ID**: 32677
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/export-segmentation-with-multiple-labels-as-nifti-doesnt-work/32677

---

## Post #1 by @lvdw (2023-11-08 16:12 UTC)

<p>Hi,</p>
<p>System: Linux Ubuntu<br>
Slicer: 5.2.2<br>
Input: nifti (both source volume and segmentation map)</p>
<p>So I have some sort of lesion map (nifti) I want to edit. This lesion map consists of non-overlapping segmentations ranging in value from 1 to 15. The source volume is a brain nifti and I load the lesion map as a segmentation. Next I can edit it with the segmentation editor but there is a problem if I want to export my new map. If I try to export it using export to files or export to labelmap, it picks random voxels from all the different segments in the map (visible on images below).<br>
However, if I export it using the save module (where I unfortunately cannot select nifti but only nrrd) I can export my new map with all my new segmentations just fine.</p>
<p>The problem is that the scripts we are working with need nifti. Currently, the only way to get these from the edited map is to next reload the nrrd as a volume and then save it in the Save module as a nifti.<br>
I have worked with segmentations consisting of different labels before on nifti’s and so far never had an issue with exporting them all together as a nifti, so I don’t know where these random voxel selected exports come from or how I can fix this.</p>
<p>Images for illustration of the problem:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877e208ed9b829d725496e5a538fc3f6b8042179.jpeg" data-download-href="/uploads/short-url/jkCGsamsNCVrQ0uc9JyXXFA1YKd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877e208ed9b829d725496e5a538fc3f6b8042179_2_630x500.jpeg" alt="image" data-base62-sha1="jkCGsamsNCVrQ0uc9JyXXFA1YKd" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877e208ed9b829d725496e5a538fc3f6b8042179_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877e208ed9b829d725496e5a538fc3f6b8042179_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877e208ed9b829d725496e5a538fc3f6b8042179_2_1260x1000.jpeg 2x" data-dominant-color="949492"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1788×1418 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8aeb564908174835ebb0de2d6e0788bf4a9135.jpeg" data-download-href="/uploads/short-url/jUs066C8gEuOTFTTpd3N2PKRFrL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8aeb564908174835ebb0de2d6e0788bf4a9135_2_630x500.jpeg" alt="image" data-base62-sha1="jUs066C8gEuOTFTTpd3N2PKRFrL" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8aeb564908174835ebb0de2d6e0788bf4a9135_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8aeb564908174835ebb0de2d6e0788bf4a9135_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8aeb564908174835ebb0de2d6e0788bf4a9135_2_1260x1000.jpeg 2x" data-dominant-color="777878"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1788×1418 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to export my complete segmentation map directly as a nifti or to make this export to files as nifti work as before?</p>

---

## Post #2 by @che85 (2023-11-08 17:04 UTC)

<p>You can export the segmentation into a labelmap and then save that labelmap as a nifti.</p>

---

## Post #3 by @lvdw (2023-11-08 17:06 UTC)

<p>Thank you for the reply, but I tried that already, and it also generates this exact same random voxel labelmap then, so it doesn’t work</p>

---

## Post #4 by @pieper (2023-11-08 17:08 UTC)

<p>5.2.2 is a bit old - try a more recent release or preview build and if you still have the problem share some example files so people can investigate.</p>

---
