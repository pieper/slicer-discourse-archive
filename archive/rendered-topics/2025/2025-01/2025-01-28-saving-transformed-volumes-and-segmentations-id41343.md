# Saving transformed volumes and segmentations

**Topic ID**: 41343
**Date**: 2025-01-28
**URL**: https://discourse.slicer.org/t/saving-transformed-volumes-and-segmentations/41343

---

## Post #1 by @jps (2025-01-28 19:03 UTC)

<p>Hello, I have a lot of micro-CT scans that were scanned in different orientations. To get them all in the same orientation for facilitating segmentation, I transform the volumes following this tutorial: <a href="https://www.youtube.com/watch?v=GkPHEsB9rOI" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=GkPHEsB9rOI</a></p>
<p>We save the transformed data using the resample scalar volume module. When we open these files, they are not aligned in the same way, but rather we have to change the view from “reformat” to “axial” or to “sagittal” etc. This then aligns our data to our desired view.</p>
<p><strong>My question is</strong> if there is a way to save the data such that the volume is saved in our desired alignment and we avoid having to change the view once loaded? I have tried saving the file as a .nrrd, .nii.gz, and .tif and none have saved the data in my desired view.</p>
<p>The reason I want to save the data in this specific format is to be able to use Biomedisa to interpolate my segmentations and speed up the segmentation process. Biomedisa uses the original voxel data so the segmentation labels end up not matching the volume.</p>
<p>Alternatively, is there a way to make the segmentations created on the transformed volume match the original voxel data?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2025-02-10 19:53 UTC)

<p>Hi - Thanks for pointing out the Biomedisa extension - It was <a href="https://discourse.slicer.org/t/possibility-to-export-only-subset-of-labelled-slices/18255">discussed here a while ago</a>, but really appears to have progressed a lot.</p>
<p>I didn’t watch the video you linked, but if you apply the same transform to the volume and the segmentation and then harden them, you should be able to save and restore them to nrrd and seg.nrrd file and have them reload in Slicer with the correct overlay because the headers will specify the correct orientation.  If you need to change the pixel data you need to use something like the BRAINS Resample module.</p>

---

## Post #3 by @jps (2025-02-24 16:24 UTC)

<p>Thanks for your response! I tried messing around with hardening both the segmentation and volume and then using the brains module. However, every time I saved a new volume with the module, the new volume would just be black (no ct images shown). I tried looking up solutions to this problem with no luck.</p>
<p>I have had success using the resample scalar/vector/DWI Volume module to resample my volume (huge thanks to this <a href="https://www.youtube.com/watch?v=AOqeJtE04YM&amp;list=PLQEnkEp8veGSkzIpLeAuKtr7ij30CvK8o&amp;index=12" rel="noopener nofollow ugc">tutorial</a>).</p>
<p>I am trying to use the same module to resample my segmentations to the new orientation with no luck. Any advice?</p>

---

## Post #4 by @pieper (2025-02-24 19:48 UTC)

<p>For the segmentations, you can export them as labelmaps, and then when you apply the transform be sure to select Nearest Neighbor interpolation.  Then you can re-import them as segmentations.  Note that any resampling, especially of segmentations, will degrade the data, so try to avoid it if you can.</p>

---

## Post #5 by @jps (2025-03-31 17:47 UTC)

<p>Thank you! This solved my problem for transforming segmentations.</p>

---
