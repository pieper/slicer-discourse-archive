# Is it possible to fuse a coregistered MRI and CT scan into one nii file on 3D Slicer?

**Topic ID**: 447
**Date**: 2017-06-06
**URL**: https://discourse.slicer.org/t/is-it-possible-to-fuse-a-coregistered-mri-and-ct-scan-into-one-nii-file-on-3d-slicer/447

---

## Post #1 by @ahoover (2017-06-06 16:43 UTC)

<p>Ultimately, I want to produce a segmentation based on CT and MRI data, so I would like to fuse the CT and MRI data into one nii file. (Both scans are currently nii files)</p>
<p>Alternatively, is it possible to segment two nii files at once in Slicer?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @lassoan (2017-06-06 16:59 UTC)

<p>Yes, you can use any number of files for segmentation. The first volume that you select as master volume will determine spacing and axis directions. You can switch volume any time by selecting another volume as master volume.</p>
<p>Before you start, probably you need to spatially register the volumes. I would recommend to try Elastix extension, but you an also try <code>General registration (BRAINS)</code> module.</p>

---

## Post #3 by @ahoover (2017-06-07 17:08 UTC)

<p>If I change the volume by selecting another volume as the master volume it asks me to create a new label map. Since I want one segmentation file at the end, is it possible to not make a new label map. Or alternatively is there an easy way to merge label maps?</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2017-06-07 21:27 UTC)

<p>Use latest nightly version of Slicer and use the Segment Editor module (not the old Editor module).</p>

---
