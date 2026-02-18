# The saved segmentation file size is different from the original volume nrrd file size

**Topic ID**: 23644
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/the-saved-segmentation-file-size-is-different-from-the-original-volume-nrrd-file-size/23644

---

## Post #1 by @parijat_patel (2022-05-30 15:34 UTC)

<p>Hello, I am using Slicer-4.11.20210226-linux-amd64 to create segmentations data to train a segmentation algorithm to automatically segment the fat depots in CT scan. The dimensions of the saved 3D segmentation file (rows, columns, slices) doesn’t match the original volume nrrd dimensions which is causing problems in my algorithm.</p>
<p>I am a software engineer and do not have much knowledge of Slicer, I tried few solutions available online but they don’t work. Could you please let me know if there is a way to save the segmentation files with same dimensions as the original nrrd volume file in Slicer?</p>
<p>Thank you,<br>
Parijat</p>

---

## Post #2 by @mau_igna_06 (2022-05-30 16:24 UTC)

<p>You just need to set up the referenceVolume argument or the original_geometry_extent flag on the function you are calling.</p>

---

## Post #3 by @parijat_patel (2022-05-31 09:12 UTC)

<p>@ mau_igna_06 Thank you for your response!! I tried setting up the reference volume argument in Slicer and export the labelmaps, but the labelmap file is mostly empty while I have the segmentations labelled in the segmentation nrrd file. And saving the the segmentation file with reference volume set doesn’t update the dimensions. Below are the steps I am following:</p>
<ol>
<li>Load the original volume nrrd and segmentation nrrd files on Slicer</li>
<li>Go to Segmentations &gt; Advanced &gt; Export/Import models and labelmaps, change the reference volume to the original nrrd volume.</li>
<li>Save the segmentation file in nrrd format (at place of seg.nrrd format).</li>
</ol>
<p>Could you please let me know if I am missing any steps, or where exactly on Slicer I have to set up the reference volume to make it work?</p>
<p>Thanks,<br>
Parijat</p>

---

## Post #4 by @mau_igna_06 (2022-05-31 09:59 UTC)

<p>I think you almost have it. Just set up ExportedSegments==All on advanced section, click on the export button and the resulting labelmap will be the volume you want to save as seg.nrrd</p>

---

## Post #5 by @parijat_patel (2022-05-31 10:17 UTC)

<p>Thank you !! ExportedSegments==All, is already set up on Advanced section. But I think I know what is causing the issue, I noticed that the “space directions” and the “space origin” were also different in the two files (original nrrd and the corresponding segmentation nrrd). Maybe that’s why it wasn’t picking up the labels and the resulting labelmap was empty !? I corrected both tags to match on both files and now I am able to export the labelmap fine.</p>

---
