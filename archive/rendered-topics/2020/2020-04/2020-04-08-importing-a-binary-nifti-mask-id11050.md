# Importing a binary nifti mask

**Topic ID**: 11050
**Date**: 2020-04-08
**URL**: https://discourse.slicer.org/t/importing-a-binary-nifti-mask/11050

---

## Post #1 by @lenome (2020-04-08 23:53 UTC)

<p>Hi all,</p>
<p>I have an MR dataset and a related binary mask file, both in nifti format. I have the lh and rh 3d files from freesurfer that I am using to display in 3d alongside the 2d MR as slices. I was able to read the binary mask file using the labelmap option to see it overlaid on the MR slices but I am unable to view the binary mask in the 3D view. Any thoughts on how to accomplish this?</p>
<p>Thank you,<br>
Suraj</p>

---

## Post #2 by @lassoan (2020-04-08 23:58 UTC)

<p>In recent Slicer Preview Releases, you can load a nifti file as segmentation by selecting Description -&gt; Segmentation in Add data dialog (in older Slicer releases, you need to load the nifti file as labelmap and then convert it to segmentation by right-clicking on it in Data module).</p>
<p>To show the segmentation in 3D, go to Segment Editor module and click “Show 3D” button.</p>

---
